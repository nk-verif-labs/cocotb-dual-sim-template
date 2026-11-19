SIM ?= verilator
TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(PWD)/rtl/ready_valid_pipe.v
TOPLEVEL = ready_valid_pipe
MODULE = test_ready_valid_pipe
export PYTHONPATH := $(PWD)/tb:$(PYTHONPATH)
include $(shell cocotb-config --makefiles)/Makefile.sim
