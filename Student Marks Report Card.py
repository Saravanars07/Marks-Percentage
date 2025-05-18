def Marks_report_card():
    num_subj=int(input("Enter a no of Subject:"))
    marks=[]
    Pass_marks=35
    for i in range(num_subj):
        mark=int(input("Enter a Subject marks:"))
        marks.append(mark)
    total=sum(marks)
    avg=total/num_subj
    print("\n-----Report Card----")
    for i,mark in enumerate(marks,1):
        status="Pass" if mark>=Pass_marks else "Fail"
        print(f"Subject {i}:{mark}-{status}")
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