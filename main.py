print("Enter 1 for Student Module")
print("Enter 2 for Course Module")
print("Enter 3 for Batch Module")
print("Enter 4 for Department Module")
print("Enter 5 for Examination Module")
i=int(input("Enter your choice : "))
print("Please wait\n")

if (i==1) :
	from Student import *
elif (i==2) :
	from Course import *
elif (i==3) :
	from Batch import *
elif (i==4) :
	from Department import *
elif (i==5) :
	from Examination import *
else :
	print("Invalid Choice")