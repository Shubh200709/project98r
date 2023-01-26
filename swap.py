file1 = "E Drive/JituTemp/Project98/sampleFile1.txt"
file2 = "E Drive/JituTemp/Project98/sampleFile2.txt"

def swapFile(x,y):
    with open(x,"r") as a :
        data_a = a.read()
    with open(y,"r") as b :
        data_b = b.read()
    
    with open(x,'w') as a :
        a.write(data_b)
    with open(y,"w") as b :
        b.write(data_a)

print("1. file1")
print("2. file2")

ask = int(input("Enter file (enter the number)")) 
do = int(input("Enter file to swap with(enter the number)"))

if(ask or do in range(1,3)):
    #print("Invalid Input! '\n' Retry")
    if(ask == 1 and do == 2):
        ask = file1
        do = file2
        swapFile(ask,do)
        print("File swaped")
    elif(ask == 2 and do == 1):
        ask = file2
        do = file1
        swapFile(ask,do)
        print("File swaped")
else:
    print("Invalid Input '\n' Retry")