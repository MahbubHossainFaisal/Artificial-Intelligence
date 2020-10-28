studentID=input("Give your student id:")

if (studentID[2] == '-' and studentID[8]=='-' and len(studentID)==10 ):
    print("It is a valid ID")
    a=1
else:
    print("It is not a valid id")
    a=0
if a==1:
    if(studentID[0]=='2'):
        print("Student is in the 1st year")
    elif(studentID[0]=='1' and studentID[1]=='9'):
        print("Student is in the 2nd year")
    elif(studentID[0]=='1' and studentID[1]=='8'):
        print("Student is in the 3rd year")
    elif(studentID[0]=='1' and studentID[1]=='7'):
        print("Student is in the 4th year")

    
    
    
