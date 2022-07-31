# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

export PYTHONPATH := $(PWD):$(PYTHONPATH)

VERILOG_SOURCES = $(PWD)/rsa_main_bug.v               # provide your design path

TOPLEVEL := rsa_main_bug    # design file
MODULE   := test_rsa    # test file

# TOPLEVEL := test1         # design file
# MODULE   := test_test1    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 