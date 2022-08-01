</br>

# 📚 Multiplexer Design Verification - Level 1 -- Design 1
</br>

![](Images/vs.png)

## 📝 Verification Environment

Vyoma's UpTickPro Tool is used to setup the Verification Environment. Multiplexer design is verified using this Verification Environment

The CoCoTb based Python Test is used to drive inputs to `Design Under Test ( DUT )`


```python
    input_values=[0,1,2,3]
    inp=[]
    for i in range(31):
        inp.append(random.choice(input_values))
        exec(f'dut.inp{i}.value = {inp[i]}')
```

It take 31 inputs - `inp[0]` --> `inp[30]` with any of these two values ` 00 , 01 , 10 , 11  `.

The assert statement is used for comparing the  DUT Output with the Expected Output value.

```python
assert int(dut.out.value) == inp[i], "Incorrect Output"
```
## :bug: Bugs 

## 📋 Test Scenario - 1

```python
for i in range(31):
        dut.sel.value = i
        await Timer(1, units='ns')     
```
Initially, Select lines are looped from 0 - 30. During this the Expected values and DUT values are verified using following command

```python
dut._log.info(f"Given input => {eval(f'dut.inp{i}.value')}\n Select line => {i} \n
                Expected Output => {inp[i]}  \n Output => {int(eval(f'dut.out.value'))} ")
```

## --- :ant: :mag:  Bug --- 1

![](Images/bug1.png)

During Execution Assertion Error is raised when Select line value = 12.

```verilog
 begin
    case(sel)
    5'b01101: out = inp12;           ===> BUG 1
    5'b01101: out = inp13;
    endcase
  end
```

## --- :ant: :wrench:  Bug Fix --- 1

This Bug is fixed by replacing `5'01101: out = 12`  with  `5'b01100: out = inp12;`

```verilog
 begin
    case(sel)
    5'b01100: out = inp12;           ===> BUG FIX 1
    5'b01101: out = inp13;
    endcase
  end
```

## 📋 Test Scenario - 2

```python
    dut.inp30.value = 1
    dut.sel.value = 30
    await Timer(1, units='ns')  
```
## --- :ant: :mag:  Bug --- 2

After the First Bug is fixed, Assertion Error is raised when Select line input = 30

![](Images/bug2.png)

```verilog
 begin
    case(sel)
    5'b11101: out = inp29;
                                     ===> BUG 2
    default: out = 0;
    endcase
  end
  ```
## --- :ant: :wrench:  Bug Fix --- 2

This Bug is fixed by including Select line input statement of 30.

```verilog
 begin
    case(sel)
    5'b11101: out = inp29;
    5'b11110: out = inp30;          ===> BUG FIX 2
    default: out = 0;
    endcase
  end
```
## -- :bug: :hammer: Bug Fixed --

![img](Images/l1d1_3.png)

## 📝 Verification Strategy

- Initially All 30 Input lines are assigned with different values
- All possible combination of inputs were tested by varying select line from 0 to 30
- DUT outputs are compared with expected values and design is verified


## 📝 Is the verification complete ?

 - [x] All Possible Select lines Combinations are tested and design bugs are fixed.
 - [x] Test cases are Passed Sucessfully
 
 <details>
 <summary> Test Cases => Also available in `Output.md` </summary>
    
 ```  

```
</details>

 
:heavy_check_mark: Design Verification is Complete
