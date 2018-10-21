#Mod call
import os

#Variable declaration
uName=input("Please enter a name to reference yourself; ")
print("Hello, ",uName)
print('')
uInput=input("Enter 1 for previous file | Enter 2 for new file ")

#User input

if uInput =='1':
    os.listdir() #not listing directory contents...
    fName=input("Choose File Name: ")
    infile=open(fName, "r")
    outPut=infile.read()
    print(outPut)
    infile.close()
    
    cont=input("Continue? ") #Need this nested

elif uInput =='2':
    fileName=input("Enter filename: ");
    fileName=(fileName + ".txt")
    with open(fileName, "w") as f:
        f.write (input ("Input data: "));
        fileOut=open(fileName, "r")
        
        cont=input("Continue? ") #Need this nested
else:

    print("Please Enter either 1 or 2")
