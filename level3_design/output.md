make -f Makefile results.xml
make[1]: Entering directory '/workspace/challenges-Nalinkumar2002/level3_design'
/home/linuxbrew/.linuxbrew/bin/iverilog -o sim_build/sim.vvp -D COCOTB_SIM=1 -s rsa_main_bug    -f sim_build/cmds.f -g2012   /workspace/challenges-Nalinkumar2002/level3_design/rsa_main_bug.v     
MODULE=test_rsa     TESTCASE= TOPLEVEL=rsa_main_bug    TOPLEVEL_LANG=verilog \
         /home/linuxbrew/.linuxbrew/bin/vvp -M /workspace/.pyenv_mirror/user/3.8.13/lib/python3.8/site-packages/cocotb/libs -m libcocotbvpi_icarus   sim_build/sim.vvp 
     -.--ns INFO     cocotb.gpi                         ..mbed/gpi_embed.cpp:76   in set_program_name_in_venv        Did not detect Python virtual environment. Using system-wide Python interpreter
     -.--ns INFO     cocotb.gpi                         ../gpi/GpiCommon.cpp:99   in gpi_print_registered_impl       VPI registered
     0.00ns INFO     Running on Icarus Verilog version 11.0 (stable)
     0.00ns INFO     Running tests with cocotb v1.6.2 from /workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb
     0.00ns INFO     Seeding Python random module with 1659340727
     0.00ns WARNING  Pytest not found, assertion rewriting will not occur
     0.00ns INFO     Found test test_rsa.test_rsa1
     0.00ns INFO     running test_rsa1 (1/1)
7 13
5 91 65
  1250.00ns INFO     Expected Public key --> 5  DUT Public Key --> 5
  1250.00ns INFO     Expected Private key --> 29  DUT Private Key --> 29
  1250.00ns INFO     Expected N : --> 91  DUT N : --> 91
  1250.00ns INFO     Expected Phi(n) : --> 72  DUT Phi(n) : --> 72
  1250.00ns INFO     
                     Encryption...
  1250.00ns INFO     EXPECTED ENCRYPTED OUTPUT ==> 39  DUT ENCRYPTED OUTPUT ==> 39 
  2500.00ns INFO     
                     Decryption...
  2500.00ns INFO     EXPECTED DECRYPTED OUTPUT ==> 65  DUT DECRYPTED OUTPUT ==> 65
                      
  2500.00ns INFO     test_rsa1 passed
  2500.00ns INFO     **************************************************************************************
                     ** TEST                          STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     **************************************************************************************
                     ** test_rsa.test_rsa1             PASS        2500.00           0.30       8330.56  **
                     **************************************************************************************
                     ** TESTS=1 PASS=1 FAIL=0 SKIP=0               2500.00           0.31       8059.02  **
                     **************************************************************************************
                     
make[1]: Leaving directory '/workspace/challenges-Nalinkumar2002/level3_design'