"""
The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

f_a = 1
f_b = 1
fibonaccis = [f_a, f_b]
while True:
    f_c = f_a + f_b 
    fibonaccis.append(f_c)
    if len(str(f_c))==1000:
        print('Number = {} at index {}'.format(f_c, len(fibonaccis)))
        break
    f_a = f_b
    f_b = f_c