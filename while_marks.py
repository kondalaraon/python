total_marks = 0
continue_entry = 'yes'

while continue_entry.lower() == 'yes':
    marks = float(input(" Enter the studnt's marks for this semester: "))
    total_marks += marks #total_marks = total_marks + marks
    continue_entry = input("Are there more semesters? (yes/no)")
    
print(f"The total marks accumulated over all semesters is : {total_marks}")