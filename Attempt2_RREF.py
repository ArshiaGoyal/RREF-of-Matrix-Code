import copy
A = []

#----------------------------------------------------------------------------------------------

def printMatrix(A):
    for i in A:
        for e in i:
            print(e,end="\t")
        print()

def r2subxr1(x,r1,r2,A):                    #   row transformation --> r2 = r2 - xr1
    c = len(A[1])
    for j in range(0,c):
        temp = A[r2][j] - x*A[r1][j]
        A[r2][j] = temp

def switchRow(r1,r2, A):                       #   r1<--->r2
    temp = A[r1]
    A[r1] = A[r2]
    A[r2] = temp


def checkreturnN0C1(A,c, row):
# given a particular column finding the first non zero character row including and after given row
# returns wether there is a non zero element and the row (if it doesnt exist it returns null)
    r = None
    for i in range(row, len(A)):
        if A[i][c] != 0:
            r = i
            break
    if r == None:
        status = False
    else:
        status = True
    return status, r

# -----------------------------------------------------------------------------------------------

rows = int(input("Number of Rows : "))
colm = int(input("Number of Columns : "))

for i in range(0,rows):                                                 #taking user's matrix
    prompt = str(i+1) + "row (elements separated by spaces): "
    r = [float(x) for x in input(prompt).split()]
    A.append(r)

cA = copy.deepcopy(A)


for i in range(0,rows):
    statusNZ, r = checkreturnN0C1(cA,i,i)
    if statusNZ == True:
        switchRow(i,r,cA)
    if statusNZ == False:
        continue

    e1 = cA[i][i]
    for j in range(0,colm):         
        temp= (cA[i][j])/e1
        cA[i][j] = temp                 #making the e1 --> 1
    printMatrix(cA)
    
    r = i+1
    while True:
        if r>=rows:
            r-=rows
        if r == i:
            break
        
        ce=cA[r][i]
        r2subxr1(ce,i,r,cA)
        r+=1
        
print()    
printMatrix(cA)
