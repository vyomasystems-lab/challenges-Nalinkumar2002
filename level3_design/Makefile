# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

export PYTHONPATH := $(PWD):$(PYTHONPATH)


VERILOG_SOURCES = $(PWD)/rsa_snk_corrected.v        
TOPLEVEL := rsa_snk_corrected 

# VERILOG_SOURCES = $(PWD)/rsa_main_bug.v     
# TOPLEVEL := rsa_main_bug   

MODULE   := test_rsa    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 