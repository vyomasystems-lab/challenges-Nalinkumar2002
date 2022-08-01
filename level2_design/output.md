make -f Makefile results.xml
make[1]: Entering directory '/workspace/challenges-Nalinkumar2002/level2_design'
MODULE=test_mkbitmanip    TESTCASE= TOPLEVEL=mkbitmanip_snk_corrected TOPLEVEL_LANG=verilog \
         /home/linuxbrew/.linuxbrew/bin/vvp -M /workspace/.pyenv_mirror/user/3.8.13/lib/python3.8/site-packages/cocotb/libs -m libcocotbvpi_icarus   sim_build/sim.vvp 
     -.--ns INFO     cocotb.gpi                         ..mbed/gpi_embed.cpp:76   in set_program_name_in_venv        Did not detect Python virtual environment. Using system-wide Python interpreter
     -.--ns INFO     cocotb.gpi                         ../gpi/GpiCommon.cpp:99   in gpi_print_registered_impl       VPI registered
     0.00ns INFO     Running on Icarus Verilog version 11.0 (stable)
     0.00ns INFO     Running tests with cocotb v1.6.2 from /workspace/.pyenv_mirror/fakeroot/versions/3.8.13/lib/python3.8/site-packages/cocotb
     0.00ns INFO     Seeding Python random module with 1659338881
     0.00ns WARNING  Pytest not found, assertion rewriting will not occur
     0.00ns INFO     Found test test_mkbitmanip.run_test
     0.00ns INFO     running run_test (1/1)

--ANDN 1
     0.01ns INFO     DUT OUTPUT=0x800c001
     0.01ns INFO     EXPECTED OUTPUT=0x800c001
--ORN 2
     0.01ns INFO     DUT OUTPUT=0x1ea7dfe5d
     0.01ns INFO     EXPECTED OUTPUT=0x1ea7dfe5d
--XNOR 3
     0.01ns INFO     DUT OUTPUT=0x1e27d3e5d
     0.01ns INFO     EXPECTED OUTPUT=0x1e27d3e5d
--SLO  4
     0.01ns INFO     DUT OUTPUT=0x106ffffff
     0.01ns INFO     EXPECTED OUTPUT=0x106ffffff
--SRO  5
     0.01ns INFO     DUT OUTPUT=0x1ffffff91
     0.01ns INFO     EXPECTED OUTPUT=0x1ffffff91
--ROL  6
     0.02ns INFO     DUT OUTPUT=0x106e4186d
     0.02ns INFO     EXPECTED OUTPUT=0x106e4186d
--ROR  7
     0.02ns INFO     DUT OUTPUT=0x61b41b91
     0.02ns INFO     EXPECTED OUTPUT=0x61b41b91
--SH1ADD  8
     0.02ns INFO     DUT OUTPUT=0x16613cfc7
     0.02ns INFO     EXPECTED OUTPUT=0x16613cfc7
--SH2ADD  9
     0.02ns INFO     DUT OUTPUT=0xf67583df
     0.02ns INFO     EXPECTED OUTPUT=0xf67583df
--SH3ADD  10
     0.02ns INFO     DUT OUTPUT=0x1738ec0f
     0.02ns INFO     EXPECTED OUTPUT=0x1738ec0f
--SBCLR   11
     0.02ns INFO     DUT OUTPUT=0x1c830da0d
     0.02ns INFO     EXPECTED OUTPUT=0x1c830da0d
--SBSET   12
     0.02ns INFO     DUT OUTPUT=0x1c930da0d
     0.02ns INFO     EXPECTED OUTPUT=0x1c930da0d
--SBINV  13
     0.02ns INFO     DUT OUTPUT=0x1c930da0d
     0.02ns INFO     EXPECTED OUTPUT=0x1c930da0d
--SBEXT  14
     0.02ns INFO     DUT OUTPUT=0x1
     0.02ns INFO     EXPECTED OUTPUT=0x1
--GORC 15 (check)
     0.03ns INFO     DUT OUTPUT=0x1ffffffff
     0.03ns INFO     EXPECTED OUTPUT=0x1ffffffff
--GREV  16 (should check)
     0.03ns INFO     DUT OUTPUT=0x16cc04e31
     0.03ns INFO     EXPECTED OUTPUT=0x16cc04e31
--CMIX  17
     0.03ns INFO     DUT OUTPUT=0x1ea3c3e5d
     0.03ns INFO     EXPECTED OUTPUT=0x1ea3c3e5d
--CMOV 18
     0.03ns INFO     DUT OUTPUT=0x1c830da0d
     0.03ns INFO     EXPECTED OUTPUT=0x1c830da0d
--FSL 19
     0.03ns INFO     DUT OUTPUT=0x106bf9f1b
     0.03ns INFO     EXPECTED OUTPUT=0x106bf9f1b
--FSR  20(check)
     0.03ns INFO     DUT OUTPUT=0x7c69f791
     0.03ns INFO     EXPECTED OUTPUT=0x7c69f791
--CLZ   21
     0.03ns INFO     DUT OUTPUT=0x1
     0.03ns INFO     EXPECTED OUTPUT=0x1
--CTZ    22
     0.03ns INFO     DUT OUTPUT=0x3
     0.03ns INFO     EXPECTED OUTPUT=0x3
--PCNT   23
     0.03ns INFO     DUT OUTPUT=0x1b
     0.03ns INFO     EXPECTED OUTPUT=0x1b
--SEXT.B  24
     0.03ns INFO     DUT OUTPUT=0xd
     0.03ns INFO     EXPECTED OUTPUT=0xd
--SEXT.H  25
     0.04ns INFO     DUT OUTPUT=0xda0d
     0.04ns INFO     EXPECTED OUTPUT=0xda0d
--CRC32.B 26
     0.04ns INFO     DUT OUTPUT=0x1d30f7ab1
     0.04ns INFO     EXPECTED OUTPUT=0x1d30f7ab1
--CRC32.H  27
     0.04ns INFO     DUT OUTPUT=0xcab2bcf7
     0.04ns INFO     EXPECTED OUTPUT=0xcab2bcf7
--CRC32.W  28
     0.04ns INFO     DUT OUTPUT=0x8031732f
     0.04ns INFO     EXPECTED OUTPUT=0x8031732f
--CRC32C.B 29
     0.04ns INFO     DUT OUTPUT=0x4c8bff0b
     0.04ns INFO     EXPECTED OUTPUT=0x4c8bff0b
--CRC32C.H  30
     0.04ns INFO     DUT OUTPUT=0x16e42d537
     0.04ns INFO     EXPECTED OUTPUT=0x16e42d537
--CRC32C.W  31
     0.04ns INFO     DUT OUTPUT=0xcfa2d845
     0.04ns INFO     EXPECTED OUTPUT=0xcfa2d845
--CLMUL  32
     0.04ns INFO     DUT OUTPUT=0x4d0a7fe5
     0.04ns INFO     EXPECTED OUTPUT=0x4d0a7fe5
--CLMULH  33
     0.04ns INFO     DUT OUTPUT=0xa246b167
     0.04ns INFO     EXPECTED OUTPUT=0xa246b167
--CLMULR  34
     0.04ns INFO     DUT OUTPUT=0x1448d62cd
     0.04ns INFO     EXPECTED OUTPUT=0x1448d62cd
--MIN  35
     0.04ns INFO     DUT OUTPUT=0x1c830da0d
     0.04ns INFO     EXPECTED OUTPUT=0x1c830da0d
--MAX 36
     0.05ns INFO     DUT OUTPUT=0x1d5b21baf
     0.05ns INFO     EXPECTED OUTPUT=0x1d5b21baf
--MINU  37
     0.05ns INFO     DUT OUTPUT=0x1c830da0d
     0.05ns INFO     EXPECTED OUTPUT=0x1c830da0d
--MAXU 38
     0.05ns INFO     DUT OUTPUT=0x1d5b21baf
     0.05ns INFO     EXPECTED OUTPUT=0x1d5b21baf
--BDEP 39
     0.05ns INFO     DUT OUTPUT=0x530100d
     0.05ns INFO     EXPECTED OUTPUT=0x530100d
--BEXT 40
     0.05ns INFO     DUT OUTPUT=0xe1b8d
     0.05ns INFO     EXPECTED OUTPUT=0xe1b8d
--PACK 41
     0.05ns INFO     DUT OUTPUT=0x1baeda0d
     0.05ns INFO     EXPECTED OUTPUT=0x1baeda0d
--PACKU 42
     0.05ns INFO     DUT OUTPUT=0x1d5b3c831
     0.05ns INFO     EXPECTED OUTPUT=0x1d5b3c831
--PACKH 45
     0.05ns INFO     DUT OUTPUT=0x1ae0d
     0.05ns INFO     EXPECTED OUTPUT=0x1ae0d
--SLOI  46
     0.05ns INFO     DUT OUTPUT=0x1c830da0d
     0.05ns INFO     EXPECTED OUTPUT=0x1c830da0d
--SROI 47
     0.06ns INFO     DUT OUTPUT=0x1c830da0d
     0.06ns INFO     EXPECTED OUTPUT=0x1c830da0d
--RORI  48
     0.06ns INFO     DUT OUTPUT=0x1c830da0d
     0.06ns INFO     EXPECTED OUTPUT=0x1c830da0d
--SBCLRI   49
     0.06ns INFO     DUT OUTPUT=0x1c830da0d
     0.06ns INFO     EXPECTED OUTPUT=0x1c830da0d
--SBSETI   50
     0.06ns INFO     DUT OUTPUT=0x1c830da0f
     0.06ns INFO     EXPECTED OUTPUT=0x1c830da0f
--SBINVI  51
     0.06ns INFO     DUT OUTPUT=0x1c830da0f
     0.06ns INFO     EXPECTED OUTPUT=0x1c830da0f
--SBEXTI  52
     0.06ns INFO     DUT OUTPUT=0x1
     0.06ns INFO     EXPECTED OUTPUT=0x1
--SHFL  53
     0.06ns INFO     DUT OUTPUT=0x152c0516d
     0.06ns INFO     EXPECTED OUTPUT=0x152c0516d
--UNSHFL  54
     0.06ns INFO     DUT OUTPUT=0x18548c365
     0.06ns INFO     EXPECTED OUTPUT=0x18548c365
--SHFLI  55 (check)
     0.06ns INFO     DUT OUTPUT=0x1c830da0d
     0.06ns INFO     EXPECTED OUTPUT=0x1c830da0d
--UNSHFLI  56  (check)
     0.06ns INFO     DUT OUTPUT=0x1c830da0d
     0.06ns INFO     EXPECTED OUTPUT=0x1c830da0d
--GORCI 57
     0.07ns INFO     DUT OUTPUT=0x1c830da0d
     0.07ns INFO     EXPECTED OUTPUT=0x1c830da0d
--GREVI  58
     0.07ns INFO     DUT OUTPUT=0x1c830da0d
     0.07ns INFO     EXPECTED OUTPUT=0x1c830da0d
--_FSRI  59
     0.07ns INFO     DUT OUTPUT=0x1c830da0d
     0.07ns INFO     EXPECTED OUTPUT=0x1c830da0d
--BFP  60
--SLO function
     0.07ns INFO     DUT OUTPUT=0x15c30da0d
     0.07ns INFO     EXPECTED OUTPUT=0x15c30da0d

--ANDN 1
     0.07ns INFO     DUT OUTPUT=0x800c001
     0.07ns INFO     EXPECTED OUTPUT=0x800c001
--ORN 2
     0.07ns INFO     DUT OUTPUT=0x1ea7dfe5d
     0.07ns INFO     EXPECTED OUTPUT=0x1ea7dfe5d
--XNOR 3
     0.07ns INFO     DUT OUTPUT=0x1e27d3e5d
     0.07ns INFO     EXPECTED OUTPUT=0x1e27d3e5d
--SLO  4
     0.07ns INFO     DUT OUTPUT=0x106ffffff
     0.07ns INFO     EXPECTED OUTPUT=0x106ffffff
--SRO  5
     0.07ns INFO     DUT OUTPUT=0x1ffffff91
     0.07ns INFO     EXPECTED OUTPUT=0x1ffffff91
--ROL  6
     0.07ns INFO     DUT OUTPUT=0x106e4186d
     0.07ns INFO     EXPECTED OUTPUT=0x106e4186d
--ROR  7
     0.07ns INFO     DUT OUTPUT=0x61b41b91
     0.07ns INFO     EXPECTED OUTPUT=0x61b41b91
--SH1ADD  8
     0.08ns INFO     DUT OUTPUT=0x16613cfc7
     0.08ns INFO     EXPECTED OUTPUT=0x16613cfc7
--SH2ADD  9
     0.08ns INFO     DUT OUTPUT=0xf67583df
     0.08ns INFO     EXPECTED OUTPUT=0xf67583df
--SH3ADD  10
     0.08ns INFO     DUT OUTPUT=0x1738ec0f
     0.08ns INFO     EXPECTED OUTPUT=0x1738ec0f
--SBCLR   11
     0.08ns INFO     DUT OUTPUT=0x1c830da0d
     0.08ns INFO     EXPECTED OUTPUT=0x1c830da0d
--SBSET   12
     0.08ns INFO     DUT OUTPUT=0x1c930da0d
     0.08ns INFO     EXPECTED OUTPUT=0x1c930da0d
--SBINV  13
     0.08ns INFO     DUT OUTPUT=0x1c930da0d
     0.08ns INFO     EXPECTED OUTPUT=0x1c930da0d
--SBEXT  14
     0.08ns INFO     DUT OUTPUT=0x1
     0.08ns INFO     EXPECTED OUTPUT=0x1
--GORC 15 (check)
     0.08ns INFO     DUT OUTPUT=0x1ffffffff
     0.08ns INFO     EXPECTED OUTPUT=0x1ffffffff
--GREV  16 (should check)
     0.08ns INFO     DUT OUTPUT=0x16cc04e31
     0.08ns INFO     EXPECTED OUTPUT=0x16cc04e31
--CMIX  17
     0.09ns INFO     DUT OUTPUT=0x1ea3c3e5d
     0.09ns INFO     EXPECTED OUTPUT=0x1ea3c3e5d
--CMOV 18
     0.09ns INFO     DUT OUTPUT=0x1c830da0d
     0.09ns INFO     EXPECTED OUTPUT=0x1c830da0d
--FSL 19
     0.09ns INFO     DUT OUTPUT=0x106bf9f1b
     0.09ns INFO     EXPECTED OUTPUT=0x106bf9f1b
--FSR  20(check)
     0.09ns INFO     DUT OUTPUT=0x7c69f791
     0.09ns INFO     EXPECTED OUTPUT=0x7c69f791
--CLZ   21
     0.09ns INFO     DUT OUTPUT=0x1
     0.09ns INFO     EXPECTED OUTPUT=0x1
--CTZ    22
     0.09ns INFO     DUT OUTPUT=0x3
     0.09ns INFO     EXPECTED OUTPUT=0x3
--PCNT   23
     0.09ns INFO     DUT OUTPUT=0x1b
     0.09ns INFO     EXPECTED OUTPUT=0x1b
--SEXT.B  24
     0.09ns INFO     DUT OUTPUT=0xd
     0.09ns INFO     EXPECTED OUTPUT=0xd
--SEXT.H  25
     0.09ns INFO     DUT OUTPUT=0xda0d
     0.09ns INFO     EXPECTED OUTPUT=0xda0d
--CRC32.B 26
     0.09ns INFO     DUT OUTPUT=0x1d30f7ab1
     0.09ns INFO     EXPECTED OUTPUT=0x1d30f7ab1
--CRC32.H  27
     0.10ns INFO     DUT OUTPUT=0xcab2bcf7
     0.10ns INFO     EXPECTED OUTPUT=0xcab2bcf7
--CRC32.W  28
     0.10ns INFO     DUT OUTPUT=0x8031732f
     0.10ns INFO     EXPECTED OUTPUT=0x8031732f
--CRC32C.B 29
     0.10ns INFO     DUT OUTPUT=0x4c8bff0b
     0.10ns INFO     EXPECTED OUTPUT=0x4c8bff0b
--CRC32C.H  30
     0.10ns INFO     DUT OUTPUT=0x16e42d537
     0.10ns INFO     EXPECTED OUTPUT=0x16e42d537
--CRC32C.W  31
     0.10ns INFO     DUT OUTPUT=0xcfa2d845
     0.10ns INFO     EXPECTED OUTPUT=0xcfa2d845
--CLMUL  32
     0.10ns INFO     DUT OUTPUT=0x4d0a7fe5
     0.10ns INFO     EXPECTED OUTPUT=0x4d0a7fe5
--CLMULH  33
     0.10ns INFO     DUT OUTPUT=0xa246b167
     0.10ns INFO     EXPECTED OUTPUT=0xa246b167
--CLMULR  34
     0.10ns INFO     DUT OUTPUT=0x1448d62cd
     0.10ns INFO     EXPECTED OUTPUT=0x1448d62cd
--MIN  35
     0.10ns INFO     DUT OUTPUT=0x1c830da0d
     0.10ns INFO     EXPECTED OUTPUT=0x1c830da0d
--MAX 36
     0.10ns INFO     DUT OUTPUT=0x1d5b21baf
     0.10ns INFO     EXPECTED OUTPUT=0x1d5b21baf
--MINU  37
     0.10ns INFO     DUT OUTPUT=0x1c830da0d
     0.10ns INFO     EXPECTED OUTPUT=0x1c830da0d
--MAXU 38
     0.11ns INFO     DUT OUTPUT=0x1d5b21baf
     0.11ns INFO     EXPECTED OUTPUT=0x1d5b21baf
--BDEP 39
     0.11ns INFO     DUT OUTPUT=0x530100d
     0.11ns INFO     EXPECTED OUTPUT=0x530100d
--BEXT 40
     0.11ns INFO     DUT OUTPUT=0xe1b8d
     0.11ns INFO     EXPECTED OUTPUT=0xe1b8d
--PACK 41
     0.11ns INFO     DUT OUTPUT=0x1baeda0d
     0.11ns INFO     EXPECTED OUTPUT=0x1baeda0d
--PACKU 42
     0.11ns INFO     DUT OUTPUT=0x1d5b3c831
     0.11ns INFO     EXPECTED OUTPUT=0x1d5b3c831
--PACKH 45
     0.11ns INFO     DUT OUTPUT=0x1ae0d
     0.11ns INFO     EXPECTED OUTPUT=0x1ae0d
--SLOI  46
     0.11ns INFO     DUT OUTPUT=0xffffffff
     0.11ns INFO     EXPECTED OUTPUT=0xffffffff
--SROI 47
     0.11ns INFO     DUT OUTPUT=0x1ffffffff
     0.11ns INFO     EXPECTED OUTPUT=0x1ffffffff
--RORI  48
     0.11ns INFO     DUT OUTPUT=0x19061b41b
     0.11ns INFO     EXPECTED OUTPUT=0x19061b41b
--SBCLRI   49
     0.12ns INFO     DUT OUTPUT=0xc830da0d
     0.12ns INFO     EXPECTED OUTPUT=0xc830da0d
--SBSETI   50
     0.12ns INFO     DUT OUTPUT=0x1c830da0d
     0.12ns INFO     EXPECTED OUTPUT=0x1c830da0d
--SBINVI  51
     0.12ns INFO     DUT OUTPUT=0xc830da0d
     0.12ns INFO     EXPECTED OUTPUT=0xc830da0d
--SBEXTI  52
     0.12ns INFO     DUT OUTPUT=0x3
     0.12ns INFO     EXPECTED OUTPUT=0x3
--SHFL  53
     0.12ns INFO     DUT OUTPUT=0x152c0516d
     0.12ns INFO     EXPECTED OUTPUT=0x152c0516d
--UNSHFL  54
     0.12ns INFO     DUT OUTPUT=0x18548c365
     0.12ns INFO     EXPECTED OUTPUT=0x18548c365
--SHFLI  55 (check)
     0.12ns INFO     DUT OUTPUT=0x178e20529
     0.12ns INFO     EXPECTED OUTPUT=0x178e20529
--UNSHFLI  56  (check)
     0.12ns INFO     DUT OUTPUT=0x184c34965
     0.12ns INFO     EXPECTED OUTPUT=0x184c34965
--GORCI 57
     0.12ns INFO     DUT OUTPUT=0x1ffffffff
     0.12ns INFO     EXPECTED OUTPUT=0x1ffffffff
--GREVI  58
     0.12ns INFO     DUT OUTPUT=0xc16c304f
     0.12ns INFO     EXPECTED OUTPUT=0xc16c304f
--_FSRI  59
     0.12ns INFO     DUT OUTPUT=0x19061b41b
     0.12ns INFO     EXPECTED OUTPUT=0x19061b41b
--BFP  60
--SLO function
     0.13ns INFO     DUT OUTPUT=0x15c30da0d
     0.13ns INFO     EXPECTED OUTPUT=0x15c30da0d
     0.13ns INFO     run_test passed
     0.13ns INFO     **************************************************************************************
                     ** TEST                          STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
                     **************************************************************************************
                     ** test_mkbitmanip.run_test       PASS           0.13           0.05          2.81  **
                     **************************************************************************************
                     ** TESTS=1 PASS=1 FAIL=0 SKIP=0                  0.13           0.06          2.13  **
                     **************************************************************************************
                     
make[1]: Leaving directory '/workspace/challenges-Nalinkumar2002/level2_design'
