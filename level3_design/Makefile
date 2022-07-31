# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

export PYTHONPATH := $(PWD):$(PYTHONPATH)

VERILOG_SOURCES = $(PWD)/rsa_main.v               # provide your design path

TOPLEVEL := rsa_main          # design file
MODULE   := test_rsa    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
