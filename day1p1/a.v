import os
import strconv
c:=os.read_lines('input')?
mut last:=-1
mut incr:=0
for l in c {
 i:=strconv.atoi(l)?
 mut d:=0
 if last!=-1 {
  d = i-last
 }
 if d>0 {
  incr++
 }
 last = i
 println(l)
}

println('increased=$incr')
