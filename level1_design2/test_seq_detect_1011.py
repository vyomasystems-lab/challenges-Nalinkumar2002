# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
 
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)
    dut.reset.value = 0
    await FallingEdge(dut.clk)

   # cocotb.log.info('#### CTB: Develop your test here! ######')

  
    for i in range(1):

      #  a=format(i, '08b')
        a='10111011'
        inp=list(a)
        l=a.find('1011')
        m=a.rfind('1011')
        out = [0]*8
        if l == m :
            if (l != -1) :
                out[l+3]=1
        elif l+3 == m :
            out[l+3]=1
        else:
            out[l+3]=1
            out[m+3]=1

        for j in range(8):

            dut.inp_bit.value = int(inp[j])
            await FallingEdge(dut.clk)
            dut._log.info(f'DUT input = > {dut.inp_bit.value} \n Expected Output => {out[j]} \n Output => {dut.seq_seen.value}')
           
        
   

    