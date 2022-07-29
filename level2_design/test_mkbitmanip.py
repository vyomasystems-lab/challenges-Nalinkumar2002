# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

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
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############

    # Bug in AND - 1 Instruction => '40007033',   '41ffffb3',

    ins = [ '40006033', '40004033', '20001033', '20005033', '60001033', '60005033', '20002033', '20004033', '20006033', '48001033', '28001033', '68001033', '48005033', '28005033', '68005033', '6001033', '6005033', '4001033', '4005033', '60001013', '60101013', '60201013', '60401013', '60501013', '61001013', '61101013', '61201013', '61801013', '61901013', '61a01013', 'a001033', 'a003033', 'a002033', 'a004033', 'a005033', 'a006033', 'a007033', '48006033', '8006033', '8004033', '48004033', '8007033', '20001013', '20005013', '60005013', '48001013', '28001013', '68001013', '48005013', '8001033', '8005033', '8001013', '8005013', '28005013', '68005013', '4005013', '48007033',
             '41ffefb3', '41ffcfb3', '21ff9fb3', '21ffdfb3', '61ff9fb3', '61ffdfb3', '21ffafb3', '21ffcfb3', '21ffefb3', '49ff9fb3', '29ff9fb3', '69ff9fb3', '49ffdfb3', '29ffdfb3', '69ffdfb3', 'ffff9fb3', 'ffffdfb3', 'fdff9fb3', 'fdffdfb3', '600f9f93', '601f9f93', '602f9f93', '604f9f93', '605f9f93', '610f9f93', '611f9f93', '612f9f93', '618f9f93', '619f9f93', '61af9f93', 'bff9fb3', 'bffbfb3', 'bffafb3', 'bffcfb3', 'bffdfb3', 'bffefb3', 'bffffb3', '49ffefb3', '9ffefb3', '9ffcfb3', '49ffcfb3', '9ffffb3', '27ff9f93', '23ffdf93', '63ffdf93', '4fff9f93', '2fff9f93', '6fff9f93', '4fffdf93', '9ff9fb3', '9ffdfb3', 'bff9f93', 'bffdf93', '2bffdf93', '6bffdf93', 'ffffdf93', '49ffffb3']
    
    for i in ins:
        # input transaction
        mav_putvalue_src1 = random.randint(0, pow(2,32)-1)
        mav_putvalue_src2 = random.randint(0, pow(2,32)-1)
        mav_putvalue_src3 = random.randint(0, pow(2,32)-1)


        mav_putvalue_instr = int(i,16)

        # expected output from the model
        expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

        # driving the input transaction
        dut.mav_putvalue_src1.value = mav_putvalue_src1
        dut.mav_putvalue_src2.value = mav_putvalue_src2
        dut.mav_putvalue_src3.value = mav_putvalue_src3
        dut.EN_mav_putvalue.value = 1
        dut.mav_putvalue_instr.value = mav_putvalue_instr
    
        yield Timer(1) 

        # obtaining the output
        dut_output = dut.mav_putvalue.value

        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        assert dut_output == expected_mav_putvalue, error_message
