import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.result import TestFailure
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer


#from model_rsa import *

# Clock Generation



@cocotb.test()
async def test_test1(dut):

    clock = Clock(dut.clk, 1, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    
    dut.out.value <= 0
    await FallingEdge(dut.clk)
    await Timer(10, units='ns')
    await FallingEdge(dut.clk)
    for i in range(10):
        await FallingEdge(dut.clk)

    # obtaining the output
    dut_out = dut.out.value
    cocotb.log.info(f' out --> {int(dut_out)}')
  
    
    # comparison
    # error_message = f'Value mismatch DUT = {(dut_output)} does not match MODEL = {(expected_output)}'
    # assert dut_output == expected_Output, error_message
