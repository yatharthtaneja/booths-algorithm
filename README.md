**BOOTH&#39;S IMPLEMENTATION PROJECT**

**DOCUMENTATION**

YATHARTH TANEJA

2019346

About algorithm: The Booth algorithm gives a procedure for **multiplying binary integers** in signed 2&#39;s complement representation **in an efficient way.**

About code:

- The code is written in python and to run in it simply open it in IDE or run from the terminal. The file name is 2019346\_yatharth\_taneja\_Project2.py
- It requires two integer number inputs.
- It then shows you partial products and the final answer in binary and integer.
- If the answer is negative it shows both binary and 2&#39;s complement.

Working of code:

- The code follows the same flow chart for the booth&#39;s algorithm.
- It first checks which number has the biggest absolute value so that it can assign an equivalent number of bits to accumulator and the other number

Eg. input numbers are -7 and 3 therefore 7 can be assigned 4 bits (0111) → (1001 in 2&#39;s complement ) and 3 is assigned 0011 and not 011 and the accumulator is assigned 0000 also sequence counter is also assigned 4.

- The number with bigger absolute value is multiplicand (BR) and the other is the multiplier (QR). QN stores the LSB of QR before the arithmetic right shift.
- While SC is not 0 while loops execute and check the condition of LSB of QR and QN if they are not same i.e 01 or 10 it Subtracts or adds BR to the accumulator respectively. And the right shifts.

Assumptions:

- Input numbers are integers.
- MSB is the sign bit

Limitations:

- The answer in binary representation will always be 2 times the size of the accumulator. Since the final answer is(AC+QR).

Eg. 6 x 6 will give answer 00100100 and not 100100 as accumulator was of 4 bit.
