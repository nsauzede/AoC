from datetime import timedelta, datetime

OTHER="[other]"

class MonitorTimer(object):
    def __init__(self, name = None):
        self.duration = timedelta()
        self.name = name

    def resume(self, date = None):
        if date != None:
            self.last_start = date
        else:
            self.last_start = datetime.now()
#        if self.name != None:
#            print("++tresume %s" % self.name)
        return self.last_start

    def stop(self, date = None):
        if date == None:
            date = datetime.now()
        self.duration += (date - self.last_start)
#        if self.name != None:
#            print("--tstop %s" % self.name)
        return date

class MonitorDisabled:
    def resume(self, key):
        pass
    def stop(self, key):
        pass
    def print_all(self):
        pass

class Monitor:
    def __init__(self):
        self.timers = {}

        self.timer_total = None
        self.timer_other = None
        self.last_timer = []

#        self.timer_total = MonitorTimer( "[total]")
#        self.timer_other = MonitorTimer( "[other]")
#        date = self.timer_total.resume()
#        self.timer_other.resume( date)

    def resume(self, key, date = None):
#        print("==mresume %s" % key)
        if key not in self.timers:
            if self.timer_total == None:
                self.timer_total = MonitorTimer( "[total]")
                self.timer_other = MonitorTimer( "[other]")
                date = self.timer_total.resume( date)
                self.timer_other.resume( date)

            self.timers[key] = MonitorTimer( key)
        date = self.timer_other.stop( date)
        self.timers[key].resume( date)

    def stop(self, key, date = None):
#        print("==mstop %s" % key)
        date = self.timers[key].stop( date)
        self.timer_other.resume( date)
        return date

    def enter(self, key):
        #print(">>enter %s" % key)
        if key not in self.timers:
            if self.timer_total == None:
                self.timer_total = MonitorTimer( "[total]")
                self.timer_other = MonitorTimer( "[other]")
                date = self.timer_total.resume()
                self.timer_other.resume( date)
                self.timers[OTHER] = MonitorTimer( OTHER)
                self.timers[OTHER].resume( date)
                self.last_timer.append( OTHER)

            self.timers[key] = MonitorTimer( key)

#        print("last_timer=%s" % self.last_timer)
        date = self.stop( self.last_timer[len(self.last_timer) - 1])
        self.last_timer.append( key)
        self.timers[key].resume( date)

    def exit(self, key):
        #print("<<exit %s" % key)
        date = self.stop( key)
        self.resume( self.last_timer.pop(), date)

    def print_all(self):
        date = self.timer_total.stop()
        self.timer_other.stop( date)
        self.stop( self.last_timer.pop(), date)
        total = self.timer_total.duration.total_seconds()
        other = self.timer_other.duration.total_seconds()
        print('----------------------- MONITORS -----------------------')
        percent = other / total * 100.0
        print('Other Time : %s %4.1f%%' % (str(self.timer_other.duration), percent))
        for key, timer in sorted(self.timers.items()):
            percent = timer.duration.total_seconds() / total * 100.0
            print('%5s Time : %s %4.1f%%' % (key, str(timer.duration), percent))
        print('==========')
        print('Total Time : %s 100 %%' % str(self.timer_total.duration))

"""
<macro-spec use-bo-parameter="yes" acemodel-version="3.0.14" simumodel-version="3.0.14" schema-version="1.0">
<bo-parameter/>
</macro-spec>
"""
