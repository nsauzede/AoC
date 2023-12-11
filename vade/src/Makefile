D:=$(shell basename $(PWD))
DAY:=$(subst day,,$(D))
YEAR:=$(shell basename `dirname $(PWD)`)
all: input1

PROX:=unset https_proxy http_proxy HTTPS_PROXY HTTP_PROXY ;
.PHONY:input1
input1:
	$(PROX)aoc download -y $(YEAR) --day $(DAY) --input-file input1 -o
