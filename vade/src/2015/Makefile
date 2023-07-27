D:=$(shell basename $(PWD))
DAY:=$(subst day,,$(D))
YEAR:=$(shell basename `dirname $(PWD)`)
all: input1

.PHONY:input1
input1:
	aoc download -y $(YEAR) --day $(DAY) --input-file input1 -o
