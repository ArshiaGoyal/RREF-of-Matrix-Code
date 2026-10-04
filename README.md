# RREF-of-Matrix-Code
We learnt RREF of Matrices in class recently (1st year BS-MS) and i thought it would be fun to code it !

## Background:
I haven't really learnt numpy in python yet... I have only explored matrices in Java during 9th and 10th grade (ICSE). So i had to use nested lists. I wanted to do this program on my own but i did need help with syntax. Tried to use minimal libraries and functions. I only have a basic understanding of Python (11th and 12th CBSE).


## Attempt 1
File name : Attempt1_RREF.py <br>
The loops were a little less straight forward than i thought... Turns out my code handled only the happy case scenarios (thankyou AI for pointing it out). Kind of embarrassed that I couldn't spot it out myself, should have tried out more inputs... will try and improve the code myself. <br>
***Issues :***
- wont work if a row becomes zero in the middle
- or if Aii (<---element) is zero
- or if columns is greater than rows


## Attempt 2
File name: Attempt2_RREF.py <br>
Much better... I think I am almost there.. Works well if the Aii element in matrix is zero or the row is zero. <br>
***Issues :***
- wont work if columns is greater than rows
