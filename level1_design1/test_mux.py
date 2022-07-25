# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    #cocotb.log.info('##### CTB: Develop your test here ########')

    input_values=[0,1,2,3]
    inp=[]
    for i in range(31):
        inp.append(random.choice(input_values))
        exec(f'dut.inp{i}.value = {inp[i]}')
    
    for i in range(31):
        dut.sel.value = i
        await Timer(1, units='ns')
        dut._log.info(f"Given input => {eval(f'dut.inp{i}.value')}\n Select line {i}  \n Expected Output => {inp[i]}  \n Output => {int(eval(f'dut.out.value'))} ")
        assert int(dut.out.value) == inp[i], "Incorrect Output"

    

