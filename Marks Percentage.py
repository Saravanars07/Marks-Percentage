#First collect a numbers of Subject ex:5,4,3

Total_Subject=int(input("Enter a No of Subject:"))

Total_marks=0
Subject_marks=[]

for i in range(Total_Subject):
    mark=int(input(f"Enter a Subject mark {i+1}:"))
    Total_marks +=mark
    Subject_marks.append(mark)

#Assuming each subject is out of 100 marks
max_total_marks=Total_Subject*100

#calculate percentage
Percentage=Total_marks/max_total_marks*100

#list a Subject marks
print("Its a Subject marks:",Subject_marks)

#count a Subject
print("Total no of Subject:",len(Subject_marks))

print("Its a Your Total Marks:",Total_marks)

print(f"Its  your total marks Perecntage:{Percentage:.2f}%")
