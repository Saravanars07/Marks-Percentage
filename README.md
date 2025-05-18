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


 # Marks Report Card
This Python script allows you to enter marks for multiple subjects, calculates the total and average, and assigns a grade based on the average score. The final output is a neatly formatted report card.

***Features***

  - Input the number of subjects and marks for each subject.
  - Calculates total and average marks.
  - Assigns grades based on the average:
    - A: 90 and above
    - B: 75 to 89
    - C: 65 to 74
    - D: Below 65
  - Displays a formatted report card with all details.

***How to Use***
 1. Copy the Script.<br>
     Save the following code in a file named ``` Student marks report card.py ```:
 2. Run in Script<br>
    Open your terminal or cmd and run:
    ```
    python Student Marks report card.py
    ```
3. Input Data

  - Enter the number of subjects.
  - Enter the marks for each subject as prompted.

4. View Your Report Card
  - The script will display:
  - Subject-wise marks
  - Total marks
  - Average marks
  - Grade

***Output***
```
Enter a no of Subject: 4
Enter a Subject marks: 85
Enter a Subject marks: 78
Enter a Subject marks: 92
Enter a Subject marks: 88

-----Report Card----
Subject 1:85
Subject 2:78
Subject 3:92
Subject 4:88
Total Marks:343
Average:85.75
Grade:B

```

***Notes***
  - Please enter valid integer values for marks.
  - The grading scale can be easily adjusted in the script.
  - No input validation is included for negative or non-integer values.
