def Marks_report_card():
    num_subj=int(input("Enter a no of Subject:"))
    marks=[]
    for i in range(num_subj):
        mark=int(input("Enter a Subject marks:"))
        marks.append(mark)
    total=sum(marks)
    avg=total/num_subj
    print("\n-----Report Card----")
    for i,mark in enumerate(marks,1):
        print(f"Subject {i}:{mark}")
    print(f"Total Marks:{total}\nAverage:{avg:.2f}")
    if avg>=90:
        grade='A'
    elif avg>=75:
        grade='B'
    elif avg>=65:
        grade='C'
    else:
        grade='F'
    print(f"Grade:{grade}")
    
Marks_report_card()