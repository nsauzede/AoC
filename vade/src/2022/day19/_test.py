def load(name):return open(name,"rt").read()

verbose=False
def aprint(s:str):
    if verbose:
        print(s)

class Game:
    def __init__(self):
        self.m={}
        self.air={}
    def load(self,l:list):
        for e in l:
            self.m[tuple(e)]=1
    def collect(self, b:dict, st:dict, minute:int, r:dict)->int:
        aprint(f"== Minute {minute} ==")
        build=None
        ore=st['ore']
        clay=st['clay']
        obsidian=st['obsidian']
        ore_ores=b['ore']['ore']
        clay_ores=b['clay']['ore']
        obsidian_ores=b['obsidian']['ore']
        obsidian_clays=b['obsidian']['clay']
        geode_ores=b['geode']['ore']
        geode_obsidians=b['geode']['obsidian']
        if ore>=geode_ores and obsidian>=geode_obsidians and (st['obsidian-robot']>r['geode_obs_gt']):
            aprint(f"Spend {geode_ores} ore and {geode_obsidians} obsidian to start building a geode-collecting robot.")
            st['ore']-=geode_ores
            st['obsidian']-=geode_obsidians
            build='geode-robot'
        elif ore>=obsidian_ores and clay>=obsidian_clays and (st['obsidian-robot']<r['obs_lt']):
            aprint(f"Spend {obsidian_ores} ore and {obsidian_clays} clay to start building a obsidian-collecting robot.")
            st['ore']-=obsidian_ores
            st['clay']-=obsidian_clays
            build='obsidian-robot'
        elif ore>=clay_ores and (st['clay-robot']<3 or (st['clay-robot']<r['clay_lt'] and st['obsidian-robot']>r['clay_obs_gt'])):
            aprint(f"Spend {clay_ores} ore to start building a clay-collecting robot.")
            st['ore']-=clay_ores
            build='clay-robot'
        elif ore>=ore_ores and (st['ore-robot']<r['ore_lt']):
            aprint(f"Spend {ore_ores} ore to start building a ore-collecting robot.")
            st['ore']-=ore_ores
            build='ore-robot'
        orebotn=st['ore-robot']
        if orebotn>0:
            ore=st['ore']+orebotn
            st['ore']=ore
            aprint(f"{orebotn} ore-collecting robot collects {orebotn} ore; you now have {ore} ore.")
        claybotn=st['clay-robot']
        if claybotn>0:
            clay=st['clay']+claybotn
            st['clay']=clay
            aprint(f"{claybotn} clay-collecting robot collects {claybotn} ore; you now have {clay} clay.")
        obsidianbotn=st['obsidian-robot']
        if obsidianbotn>0:
            obsidian=st['obsidian']+obsidianbotn
            st['obsidian']=obsidian
            aprint(f"{obsidianbotn} obsidian-collecting robot collects {obsidianbotn} ore; you now have {obsidian} obsidian.")
        geodebotn=st['geode-robot']
        if geodebotn>0:
            geode=st['geode']+geodebotn
            st['geode']=geode
            aprint(f"{geodebotn} geode-collecting robot collects {geodebotn} ore; you now have {geode} geode.")
        if build:
            n=st[build]+1
            st[build]=n
            aprint(f"The new {build} is ready; you now have {n} of them.")
        aprint('')
        return st['geode']

    def blueprint(self,b:dict,r=None)->int:
        if not r:r={'obs_lt':2, 'clay_lt':4, 'clay_obs_gt':0, 'ore_lt':1, 'geode_obs_gt':0}
        st={
        'ore':0,
        'clay':0,
        'obsidian':0,
        'geode':0,
        'ore-robot':1,
        'clay-robot':0,
        'obsidian-robot':0,
        'geode-robot':0,
        }
        c=0
        for m in range(24):
            c=self.collect(b,st,m+1,r)
        aprint(f"Blueprint: {b}")
        aprint(f"Rules: {r}")
        aprint(f"Returning c={c}")
        return c

    def collect2(self, b:dict, st:dict, minute:int, r:dict)->int:
        aprint(f"== Minute {minute} ==")
        build=None
        ore=st['ore']
        clay=st['clay']
        obsidian=st['obsidian']
        ore_ores=b['ore']['ore']
        clay_ores=b['clay']['ore']
        obsidian_ores=b['obsidian']['ore']
        obsidian_clays=b['obsidian']['clay']
        geode_ores=b['geode']['ore']
        geode_obsidians=b['geode']['obsidian']
        if ore>=geode_ores and obsidian>=geode_obsidians:
            aprint(f"Spend {geode_ores} ore and {geode_obsidians} obsidian to start building a geode-collecting robot.")
            st['ore']-=geode_ores
            st['obsidian']-=geode_obsidians
            build='geode-robot'
            if st['first-geode']==0:st['first-geode']=minute
        elif ore>=obsidian_ores and clay>=obsidian_clays and (minute>r['obs_after'] and minute<r['obs_before']):
            aprint(f"Spend {obsidian_ores} ore and {obsidian_clays} clay to start building a obsidian-collecting robot.")
            st['ore']-=obsidian_ores
            st['clay']-=obsidian_clays
            build='obsidian-robot'
        elif ore>=clay_ores and (minute>r['clay_after'] and minute<r['clay_before']):
            aprint(f"Spend {clay_ores} ore to start building a clay-collecting robot.")
            st['ore']-=clay_ores
            build='clay-robot'
        elif ore>=ore_ores and (minute>r['ore_after'] and minute<r['ore_before']):
            aprint(f"Spend {ore_ores} ore to start building a ore-collecting robot.")
            st['ore']-=ore_ores
            build='ore-robot'
        orebotn=st['ore-robot']
        if orebotn>0:
            ore=st['ore']+orebotn
            st['ore']=ore
            aprint(f"{orebotn} ore-collecting robot collects {orebotn} ore; you now have {ore} ore.")
        claybotn=st['clay-robot']
        if claybotn>0:
            clay=st['clay']+claybotn
            st['clay']=clay
            aprint(f"{claybotn} clay-collecting robot collects {claybotn} ore; you now have {clay} clay.")
        obsidianbotn=st['obsidian-robot']
        if obsidianbotn>0:
            obsidian=st['obsidian']+obsidianbotn
            st['obsidian']=obsidian
            aprint(f"{obsidianbotn} obsidian-collecting robot collects {obsidianbotn} ore; you now have {obsidian} obsidian.")
        geodebotn=st['geode-robot']
        if geodebotn>0:
            geode=st['geode']+geodebotn
            st['geode']=geode
            aprint(f"{geodebotn} geode-collecting robot collects {geodebotn} ore; you now have {geode} geode.")
        if build:
            n=st[build]+1
            st[build]=n
            aprint(f"The new {build} is ready; you now have {n} of them.")
        aprint('')
        return st['geode']
    def blueprint2(self,b:dict,r=None)->int:
        if not r:r={'ore_after':0, 'ore_before':25, 'clay_after':0, 'clay_before':25, 'obs_after':0, 'obs_before':25}
        #if not r:r={'ore_after':0, 'ore_before':25, 'clay_after':24, 'clay_before':25, 'obs_after':24, 'obs_before':25}
        st={
        'ore':0,
        'clay':0,
        'obsidian':0,
        'geode':0,
        'ore-robot':1,
        'clay-robot':0,
        'obsidian-robot':0,
        'geode-robot':0,
        'first-geode':0
        }
        c=0
        for m in range(24):
            c=self.collect2(b,st,m+1,r)
        aprint(f"Blueprint: {b}")
        aprint(f"Rules: {r}")
        aprint(f"Returning c={c} (first geode at Minute {st['first-geode']})")
        return c

inp00={
1:{'ore':{'ore':4},'clay':{'ore':2},'obsidian':{'ore':3,'clay':14},'geode':{'ore':2,'obsidian':7}},
2:{'ore':{'ore':2},'clay':{'ore':3},'obsidian':{'ore':3,'clay':8},'geode':{'ore':3,'obsidian':12}},
}

res00_1 = 9
res00_2 = 12
res0 = 33
res1 = 0
res0_2 = 0
res1_2 = 0

import unittest
#@unittest.skip
class T000(unittest.TestCase):
    def test_010_blueprint1(self):
        g=Game()
        res=g.blueprint(inp00[1])
        self.assertEqual(res00_1,res)
    def Ztest_011_blueprint2(self):
        g=Game()
        global verbose
        verbose=True
        res=g.blueprint(inp00[2], {'obs_lt':5, 'clay_lt':4, 'clay_obs_gt':0, 'ore_lt':2, 'geode_obs_gt':0})
        verbose=False
        self.assertEqual(res00_2,res)
    def Ztest_011_blueprint2(self):
        g=Game()
        global verbose
        verbose=True
        res=g.blueprint2(inp00[2])
        verbose=False
        self.assertEqual(res00_2,res)

    def test_120_sweep_blueprint1(self):
        g=Game()
        max=0
        combo=()
        MX=5
        for i in range(0,MX):
            for j in range(0,MX):
                for k in range(0,MX):
                    for l in range(0,MX):
                        for m in range(0,MX):
                            res=g.blueprint(inp00[1], {'obs_lt':i, 'clay_lt':j, 'clay_obs_gt':k, 'ore_lt':l, 'geode_obs_gt':m})
                            if res>max:
                                max=res
                                combo=(i,j,k,l,m)
        res=max
        print(f"Found max={max} for combo {combo}")
        self.assertEqual(res00_1,res)
    def Ztest_121_sweep_blueprint2(self):
        g=Game()
        max=0
        combo=()
        MX=5
        for i in range(0,MX):
            for j in range(0,MX):
                for k in range(0,MX):
                    for l in range(0,MX):
                        for m in range(0,MX):
                            res=g.blueprint(inp00[2], {'obs_lt':i, 'clay_lt':j, 'clay_obs_gt':k, 'ore_lt':l, 'geode_obs_gt':m})
                            if res>max:
                                max=res
                                combo=(i,j,k,l,m)
        res=max
        print(f"Found max={max} for combo {combo}")
        self.assertEqual(res00_2,res)
    def Ztest_122_sweep_blueprint2(self):
        g=Game()
        max=0
        combo=()
        MX=24
        for i in range(0,MX):
            for j in range(0,MX):
                if j<=i:continue
                for k in range(0,MX):
                    for l in range(0,MX):
                        if l<=k:continue
                        for m in range(0,MX):
                            for n in range(0,MX):
                                if n<=m:continue
                                res=g.blueprint2(inp00[2], {'ore_after':i, 'ore_before':j, 'clay_after':k, 'clay_before':l, 'obs_after':m, 'obs_before':n})
                                if res>max:
                                    max=res
                                    combo=(i,j,k,l,m,n)
                                    print(f"combo {combo} => {max}")
        res=max
        print(f"Found max={max} for combo {combo}")
        self.assertEqual(res00_2,res)
    def Ztest_123_sweep2_blueprint1(self):
        g=Game()
        max=0
        combo=()
        MX=24
        for i in range(0,MX):
            for j in range(0,MX):
                if j<=i:continue
                for k in range(0,MX):
                    for l in range(0,MX):
                        if l<=k:continue
                        for m in range(0,MX):
                            for n in range(0,MX):
                                if n<=m:continue
                                res=g.blueprint2(inp00[1], {'ore_after':i, 'ore_before':j, 'clay_after':k, 'clay_before':l, 'obs_after':m, 'obs_before':n})
                                if res>max:
                                    max=res
                                    combo=(i,j,k,l,m,n)
                                    print(f"combo {combo} => {max}")
        res=max
        print(f"Found max={max} for combo {combo}")
        self.assertEqual(res00_2,res)

