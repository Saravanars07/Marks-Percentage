# Marks-Percentage-
## Subject Marks Percentage Calculator
This Python script allows you to input marks for a number of subjects, calculates the total marks, and computes the percentage. It also displays the marks for each subject and the total number of subjects.

***Features***<br>
  - Accepts the number of subjects as user input.
  - Collects marks for each subject.
  - Calculates the total marks and percentage (assuming each subject is out of 100).
  - Displays all subject marks, total marks, and percentage.

***How to Use***
 1. Run the Script.
    
     Make sure you have Python installed. Save the script as marks_calculator.py and run it:
    ```
    python Marks Percentage.py
    ```
 2. Input the number of subjects.
    
    You will be prompted to enter the total number of subjects (e.g., 3, 4, 5).
    
 3. Input marks for each subject.

    Enter the marks for each subject when prompted.
    
 4. View results.
    
    The script will print:

      - The list of marks for each subject

     - The total number of subjects
    
     - The total marks obtained
    
     - The percentage.


***Code***

 ```
Total_Subject = int(input("Enter a No of Subject: "))

Total_marks = 0
Subject_marks = []

for i in range(Total_Subject):
    mark = int(input(f"Enter a Subject mark {i+1}: "))
    Total_marks += mark
    Subject_marks.append(mark)

# Assuming each subject is out of 100 marks
max_total_marks = Total_Subject * 100

# Calculate percentage
Percentage = Total_marks / max_total_marks * 100

# List subject marks
print("Its a Subject marks:", Subject_marks)

# Count subjects
print("Total no of Subject:", len(Subject_marks))

print("Its a Your Total Marks:", Total_marks)

print(f"Its your total marks Percentage: {Percentage:.2f}%")

 ```

***Output***
```
  Enter a No of Subject: 3
  Enter a Subject mark 1: 80
  Enter a Subject mark 2: 90
  Enter a Subject mark 3: 85
  Its a Subject marks: [80, 90, 85]
  Total no of Subject: 3
  Its a Your Total Marks: 255
  Its  your total marks Percentage:85.00%
```

***Notes***
 - This script assumes each subject is out of 100 marks.
 - Input validation is not included; entering non-integer values will cause an error.
