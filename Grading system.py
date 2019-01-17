
#grading system
print("grading system")
s=float(input("Enter marks of the student"))
if(s>90 and s<=100):
    print("grade=A")
elif(s>80 and s<=90):    
    print("grade=B")
elif(s>70 and s<=80):    
    print("grade=c")
elif(s>60 and s<=70):    
    print("grade=d")
elif(s>50 and s<=60):    
    print("grade=e") 
elif(s<40):    
    print("grade=fail")
else:
    print("invalid input")