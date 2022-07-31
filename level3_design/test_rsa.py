import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

#from model_rsa import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def run_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.Input.value <= 0
    dut.prime_p.value <= 0
    dut.prime_q.value <= 0
    dut.start.value <= 0
    dut.start1.value <= 0
    dut.start2.value <= 0
    yield Timer(100) 
    dut.Input.value <= 65
    dut.prime_p.value <= 7
    dut.prime_q.value <= 13
    yield Timer(100)
    dut.start.value <= 1
    yield Timer(50)
    dut.start.value <= 0
    yield Timer(400)
    dut.start1.value <= 1
    yield Timer(100)
    dut.start1.value <= 0
    yield Timer(300)
    dut.start2.value <= 1
    yield Timer(100)
    dut.start2.value <= 0

    expected_output = 39   

    # obtaining the output
    dut_publicKey = dut.publicKey.value
    dut_privateKey = dut.privateKey.value
    dut_n = dut.n.value
    dut_output =dut.Output.value

    cocotb.log.info(f' Public Key --> {int(dut_publicKey)}')
    cocotb.log.info(f' Private Key --> {int(dut_privateKey)}')
    cocotb.log.info(f'DUT OUTPUT={int(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={(expected_output)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {(dut_output)} does not match MODEL = {(expected_output)}'
    assert dut_output == expected_Output, error_message
