import copy
"""
NAME: YATHARTH TANEJA 
ROLL NO: 2019346
CO PROJECT 2
BOOTH'S IMPLEMENTATION ALGORITHM  
"""


# HELPER FUNCTION TO CONVERT TO BINARY RETURN A LIST WITH INDEX BASED BINARY NUMBERS



def to_binary(s,arr):
    x=int(s)
    sum=0
    exp=1
    while(x>0):
        digit=x%2
        x=x//2
        arr.append(digit)
        sum+=digit*exp
        exp*=10
    # sum='0'*(8-len(str(sum)))+str(sum)
    return sum
#HELPER FUNCTION TO ADD
def To_Decimal(n): 
    return int(n,2) 
def add(ac,x,qrn):
    c=0
    for k in range(qrn):
        # print("ac "+ str(ac[k]))
        ac[k]+=x[k]+c
        # print("ac 2 " + str(ac[k]))
        if(ac[k]>1):
            ac[k]=ac[k]%2
            c=1
        else:
            c=0
#FUNCTION TO TAKE TWOS COMPLEMENT
def comp2(a,n):
    x=[]
    for k in range(n):
        x.append(0)
    x[0]=1
    # print(x)
    for k in range(n):
        a[k]=(a[k]+1)%2
    # print(a)
    add(a,x,n)
#TO MAKE RIGHT SHIFT
def rightshift(ac,qr,qrn):
    temp=ac[0]
    global qn
    qn=qr[0]
    for k in range(qrn-1):
        ac[k]=ac[k+1]
        qr[k]=qr[k+1]
    qr[qrn-1]=temp
#PRINT ARRAY FUNCTION
def printarr(ac,qrn):
    for k in range(qrn-1,-1,-1):
        print(ac[k],end="")
    print(end=" ")

def giveans(ac,qrn,s):
    for k in range(qrn-1,-1,-1):
        s+=str(ac[k])
    # print(" sss ")
    # print(s)
    return s
#FUNCTION TO REVERSE ARRAY
def revarr(ac):
    x=len(ac)
    for k in range(x//2):
        t=ac[k]
        ac[k]=ac[x-k-1]
        ac[x-k-1]=t
#FUNCTION TO REVERSE ARRAY
def makeequal(ac,x):
    w=len(ac)
    y=len(x)
    z=w-y
    for k in range(z):
        x.append(0)
#TO INITIALISE ACCUMILATOR
def makeacc(ac,qrn):
    for k in range(qrn):
        ac.append(0)
#MAIN ALGORITHM
def boots(ac,br,qr,br2,qrn,sc):
    global qn
    flag=0
    print("ACCUMILATOR: ",end=" ")
    printarr(ac,qrn)
    print("QR: ",end=" ")
    printarr(qr,qrn)
    print("QN: "+str(qn),end=" ")
    print("SC: "+str(sc),end=" ")
    print()
    
    while(sc!=0):
        # add subtract condition
        if(qn+qr[0]==1 and flag==0): #AC-BR
            add(ac,br2,qrn)
            print("subtacting BR \n ACCUMILATOR: ",end=" ")
            printarr(ac,qrn)
            print()
            flag=1
        elif(qn+qr[0]==1 and flag==1): #AC+BR
            add(ac,br,qrn)
            print("adding BR \n ACCUMILATOR: ",end=" ")
            printarr(ac,qrn)
            print()
            flag=0
        rightshift(ac,qr,qrn) #RIGHT SHIFT CONDITION
        sc-=1
        print("ACCUMILATOR: ",end=" ")
        printarr(ac,qrn)
        print("QR: ",end=" ")
        printarr(qr,qrn)
        print("QN: "+str(qn),end=" ")
        print("SC: "+str(sc),end=" ")
        print()
        
br=[]
qr=[]
ac=[]
global qn
qn=0
x1=int(input("INPUT NUMBER 1: "))
x2=int(input("INPUT NUMBER 2: "))
if abs(x1)<abs(x2):
    x1,x2=x2,x1

to_binary(abs(x1),br)
br.append(0)
# br.append(0)
to_binary(abs(x2),qr)
makeequal(br,qr)
brn=len(br)
qrn=len(qr)

if(x1<0):
    comp2(br,brn)
if(x2<0):
    comp2(qr,qrn)
 
br2=[]
br2=copy.deepcopy(br)

# for k in range(brn):
#     br2[k].append(br[k])
comp2(br2,brn)

makeacc(ac,brn)
sc=qrn
boots(ac,br,qr,br2,qrn,sc)
if ac[qrn-1]==1:
    revarr(ac)
    revarr(qr)
    ans=ac+qr
    revarr(ans)
    print()
    print("ANSWER IN 2's complement: ",end=" ")
    printarr(ans,brn+qrn)
    print()

    comp2(ans,brn+qrn)
    print("ANSWER (negative):",end=" ")
    printarr(ans,brn+qrn)
    print()
    print("INTEGER REPRESENTATION : -",end="")
    print(To_Decimal(giveans(ans,brn+qrn,"")))
else:
    revarr(ac)
    revarr(qr)
    ans=ac+qr
    revarr(ans)
    print()
    # print(ans)
    print("ANSWER:",end=" ")
    printarr(ans,brn+qrn)
    print()
    print("INTEGER REPRESENTATION : ",end=" ")
    print(To_Decimal(giveans(ans,brn+qrn,"")))

        


            







