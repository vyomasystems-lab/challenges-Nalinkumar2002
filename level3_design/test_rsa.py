import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.result import TestFailure
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.triggers import Timer


from model_rsa import *

# Clock Generation



@cocotb.test()
async def test_rsa1(dut):

    clock = Clock(dut.clk, 1, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    msg_in = 65
    prime1 = 7
    prime2 = 13

    msg,e,d,n,phin,encrypted_msg,decrypted_msg = model_rsa(msg_in,prime1,prime2)
      
    
    dut.Input.value = 0
    dut.prime_p.value = 0
    dut.prime_q.value = 0
    dut.start.value = 0
    dut.start1.value = 0
    dut.start2.value = 0
    await Timer(100, units='ns')
    dut.Input.value = msg_in
    dut.prime_p.value = prime1
    dut.prime_q.value = prime2
    await Timer(100, units='ns')
    dut.start.value = 1
    await Timer(50, units='ns')
    dut.start.value = 0
    await Timer(400, units='ns')
    dut.start1.value = 1
    await Timer(100, units='ns')
    dut.start1.value = 0
    await Timer(300, units='ns')
    dut.start2.value = 1
    await Timer(100, units='ns')
    dut.start2.value = 0
    await Timer(100, units='ns')



    # obtaining the output
    dut_publicKey = int(dut.publicKey.value)
    dut_privateKey = int(dut.privateKey.value)
    dut_n = int(dut.n.value)
    dut_encrypt = int(dut.Output.value)
    dut_phin = int(dut.phin.value)
    
    cocotb.log.info(f'Expected Public key --> {e}  DUT Public Key --> {(dut_publicKey)}')
    cocotb.log.info(f'Expected Private key --> {d}  DUT Private Key --> {(dut_privateKey)}')
    cocotb.log.info(f'Expected N : --> {n}  DUT N : --> {(dut_n)}')
    cocotb.log.info(f'Expected Phi(n) : --> {phin}  DUT Phi(n) : --> {(dut_phin)}')
    cocotb.log.info(f'\nEncryption...')
    cocotb.log.info(f'EXPECTED ENCRYPTED OUTPUT ==> {(encrypted_msg)}  DUT ENCRYPTED OUTPUT ==> {(dut_encrypt)} ')

    dut.Input.value = 1
    dut.prime_p.value = 0
    dut.prime_q.value = 0
    dut.start.value = 0
    dut.start1.value = 0
    dut.start2.value = 0
    await Timer(100, units='ns')
    dut.Input.value = dut_encrypt
    dut.prime_p.value = prime1
    dut.prime_q.value = prime2
    await Timer(100, units='ns')
    dut.start.value = 1
    await Timer(50, units='ns')
    dut.start.value = 0
    await Timer(400, units='ns')
    dut.start1.value = 1
    await Timer(100, units='ns')
    dut.start1.value = 0
    await Timer(300, units='ns')
    dut.start2.value = 1
    await Timer(100, units='ns')
    dut.start2.value = 0
    await Timer(100, units='ns')

    dut_decrypt = int(dut.Output.value)
    cocotb.log.info(f'\nDecryption...')
    cocotb.log.info(f'EXPECTED DECRYPTED OUTPUT ==> {int(decrypted_msg)}  DUT DECRYPTED OUTPUT ==> {int(dut_decrypt)}\n ')
    
    # comparison
    
    error_message1 = f'Expected Public key --> {e}  DUT Public Key --> {int(dut_publicKey)}'
    error_message2 = f'Expected Private key --> {d}  DUT Private Key --> {(dut_privateKey)}'
    error_message3 = f'Expected N : --> {n}  DUT N : --> {(dut_n)}'
    error_message4 = f'Expected Phi(n) : --> {phin}  DUT Phi(n) : --> {(dut_phin)}'
    error_message5 = f'EXPECTED ENCRYPTED OUTPUT ==> {(encrypted_msg)}  DUT ENCRYPTED OUTPUT ==> {(dut_encrypt)} '
    error_message6 = f'EXPECTED DECRYPTED OUTPUT ==> {int(decrypted_msg)}  DUT DECRYPTED OUTPUT ==> {int(dut_decrypt)} '
    assert e == dut_publicKey, error_message1
    assert d == dut_privateKey, error_message2
    assert n == dut_n, error_message3
    assert phin == dut_phin, error_message4
    assert encrypted_msg == dut_encrypt, error_message5
    assert decrypted_msg == dut_decrypt, error_message6