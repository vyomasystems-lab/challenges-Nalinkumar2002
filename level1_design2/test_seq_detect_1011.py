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

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # Nalinkumar S
    # ------------

    # Loop for all possible 8 bit combinations

    for i in range(256):

        # Reset
        dut.reset.value = 1
        await FallingEdge(dut.clk)
        dut.reset.value = 0
        await FallingEdge(dut.clk)

        # Logic to Detect the Sequence
        a=format(i, '08b')
        dut._log.info(f"Sequence : {a} ")
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

        # Loop for A 8 Bit Combination
        for j in range(8):

            await Timer(10, units='ns')
            dut.inp_bit.value = int(inp[j])
            await FallingEdge(dut.clk)

            # DUT Values
            dut._log.info(f'DUT input = > {dut.inp_bit.value} \n Expected Output => {out[j]} \n Output => {dut.seq_seen.value} \n \
            Current State => {dut.current_state.value} , Next State = >  {dut.next_state.value}')

            # Checking for Errors
            assert out[j] == dut.seq_seen.value, f"Incorrect => Expected : {out[j]} Got : {dut.seq_seen.value}"
        
        # Reset input bit to 0
        dut.inp_bit.value = 0 


    