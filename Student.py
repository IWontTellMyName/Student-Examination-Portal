import pandas
from prettytable import PrettyTable as PT
df=pandas.read_csv("Student.csv") 

def createStudent(studentName) :
	df=pandas.read_csv("Batch.csv")
	print()
	for i in range (len(df)) :
		print("Enter",(i+1),"to choose",df.iat[i,1])
	i=int(input("Select a batch : ")) -1
	if str(df.iat[i,4])=="nan" :
		rollNo=1
		studentID=df.iat[i,0]+"01"
		df.iat[i,4]=studentID
	else :
		rollNo=str(int(df.iat[i,4][-2:])+1)
		studentID=df.iat[i,0]+(rollNo if int(rollNo)>9 else "0"+rollNo)
		df.iat[i,4]=df.iat[i,4]+":"+studentID
	df.to_csv("Batch.csv", index=False)
	with open("Student.csv", "a") as file :
		file.write(studentID+","+studentName+","+str(rollNo)+","+df.iat[i,0]+"\n")
	print("Generated Student ID is",studentID)
	print("Generated Class Roll number is",rollNo)

def deleteStudent() :
	batchID=""
	studentList=[]
	studentID=input("Enter current Student ID : ")
	df=pandas.read_csv("Student.csv")
	for i in range (len(df)) :
		if (df.iat[i,0]==studentID) :
			batchID=df.iat[i,3]
			studentName=df.iat[i,1]
			(df.drop(i)).to_csv("Student.csv", index=False)
			break
	
	df=pandas.read_csv("Batch.csv")
	for i in range (len(df)) :
		if (df.iat[i,0]==batchID) :
			studentList=df.iat[i,4].split(":")
			break
	studentList.remove(studentID)
	df.iat[i,4]=studentList[0]
	for index in range(len(studentList)) :
		df.iat[i,4]+=":"+studentList[index]
	df.to_csv("Batch.csv", index=False)
	return studentName

def updateStudent() :
	ch=int(input("Enter 1 to change Student Name or 2 to change Batch of a student : "))
	if (ch==1) :
		studentID=input("Enter Student ID : ")
		for i in range (len(df)) :
			if (df.iat[i,0]==studentID) :
				df.iat[i,1]=input("Enter correct Student Name : ")
				df.to_csv("Student.csv", index=False)
				print("Name corrected")
	
	elif (ch==2) :
		studentName=deleteStudent()
		createStudent(studentName)
		print("Batch changed")
	else :
		print("Invalid Input")

def gradeFunction(marks) :
	if marks>=90 :
		return "A"
	elif marks>=80 :
		return "B"
	elif marks>=70 :
		return "C"
	elif marks>=60 :
		return "D"
	elif marks>=50 :
	 	return "E"
	else :
	 	return "F"
	 
def reportCard() :
	studentID=input("Enter Student ID : ")
	file=open(studentID+".txt", "w")
	df=pandas.read_csv("Student.csv") 
	for i in range (len(df)) :
		if (df.iat[i,0]==studentID) :
			batchID=df.iat[i,3]
			file.write("Student Name : "+df.iat[i,1])
			file.write("\nStudent ID : "+studentID)
			file.write("\nBatch ID : "+batchID)
			file.write("\nRoll Number : "+str(df.iat[i,2])+"\n")
			Table=PT(["Course","Percentage","Grade","Pass/Fail"])
			break
	
	df=pandas.read_csv("Course.csv")
	fail=False
	for i in range (len(df)) :
		marksList=df.iat[i,2].split("-")
		for element in marksList :
			pair=element.split(":")
			if (pair[0]==studentID) :
				grade=gradeFunction(int(pair[1]))
				Table.add_row([df.iat[i,1],pair[1]+"%",grade,"Failed" if grade=="F" else "Passed"])
				if grade=="F" :
					fail=True
	file.write(Table.get_string())
	file.write("\n\nOverall Failed" if fail else "\n\nOverall Passed")
	print("\nReport Card generated with filename "+studentID+".txt")


print("Enter 1 for adding a new Student")
print("Enter 2 to update existing Student details")
print("Enter 3 to delete a student")
print("Enter 4 to generate individual report card")
i=int(input("Enter your choice : "))
print()
if (i==1) :
	createStudent(input("Enter Student Name : "))
elif (i==2) :
	updateStudent()
elif (i==3) :
	sName=deleteStudent()
	print(sName+" has been removed from batch and his records have been deleted")
elif (i==4) :
	reportCard()
else :
	print("Invalid Choice")
