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
async def test_rsa1(dut):

    clock = Clock(dut.clk, 1, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    
    dut.Input.value <= 0
    dut.prime_p.value <= 0
    dut.prime_q.value <= 0
    dut.start.value <= 0
    dut.start1.value <= 0
    dut.start2.value <= 0
    await FallingEdge(dut.clk)
    await Timer(100, units='ns')
    dut.Input.value <= 65
    dut.prime_p.value <= 7
    dut.prime_q.value <= 13
    await FallingEdge(dut.clk)
    await Timer(100, units='ns')
    dut.start.value <= 1
    await FallingEdge(dut.clk)
    await Timer(50, units='ns')
    dut.start.value <= 0
    await FallingEdge(dut.clk)
    await Timer(400, units='ns')
    dut.start1.value <= 1
    await FallingEdge(dut.clk)
    await Timer(100, units='ns')
    dut.start1.value <= 0
    await FallingEdge(dut.clk)
    await Timer(300, units='ns')
    dut.start2.value <= 1
    await FallingEdge(dut.clk)
    await Timer(100, units='ns')
    dut.start2.value <= 0
    await FallingEdge(dut.clk)
    await Timer(100, units='ns')
    await FallingEdge(dut.clk)

    expected_output = 39   
    

    # obtaining the output
    dut_publicKey = dut.publicKey.value
    dut_privateKey = dut.privateKey.value
    dut_n = dut.n.value
    dut_output =dut.Output.value
    
    cocotb.log.info(f' Public Key --> {(dut_publicKey)}')
    cocotb.log.info(f' Private Key --> {(dut_privateKey)}')
    cocotb.log.info(f'DUT OUTPUT={(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={(expected_output)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {(dut_output)} does not match MODEL = {(expected_output)}'
    assert dut_output == expected_Output, error_message
