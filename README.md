# RREF-of-Matrix-Code
We learnt RREF of Matrices in class recently (1st year BS-MS) and i thought it would be fun to code it !

## Background:
I haven't really learnt numpy in python yet... I have only explored matrices in Java during 9th and 10th grade (ICSE). So i had to use nested lists. I wanted to do this program on my own but i did need help with syntax. Tried to use minimal libraries and functions. I only have a basic understanding of Python (11th and 12th CBSE).


## Attempt 1
File name : Attempt1_RREF.py <br>
The loops were a little less straight forward than i thought... Turns out my code didnt handle all the scenarios (thankyou AI for pointing it out). Kind of embarrassed that I couldn't spot it myself, should have tried out more inputs... will try and improve the code myself. <br>
***Issues :***
- wont work if a row becomes zero in the middle
- or if Ai[i][i] (<---element) is zero
- or if columns is greater than rows


## Attempt 2
File name: Attempt2_RREF.py <br>
Much better... I think I am almost there... Works well if the Aii element in matrix is zero or the row is zero. <br>
<br>
To fix the error which would arise when A[i][i] is zero , i was first thinking of just switching the rows with the next row till i found a non-zero A[i][i] element. Then i realised that the loop will end up running infinitely if even the next row's A[i+1][i] element is zero... I couldn't just blindly exchange rows i needed to find the row where the ith column element is zero. I defined a new function for that: checkreturnN0C1(A,c, row). Then i switched this new foun row with my ith row.
<br>
***Issues :***
- wont work if columns is greater than rows (because i keep focusing on the A[i][i] element)
