# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/seq_detect_1011_snk_corrected.v
TOPLEVEL := seq_detect_1011_snk_corrected

# TOPLEVEL := seq_detect_1011        
# VERILOG_SOURCES = $(PWD)/seq_detect_1011.v


MODULE   := test_seq_detect_1011     # test

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
