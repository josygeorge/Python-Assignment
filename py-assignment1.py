# PYTHON FUNDAMENTALS ASSIGNMENT
print('--------- PYTHON FUNDAMENTALS - ASSIGNMENT -----------')

# Part 1: User Input

# Declare a variable to accept the input
num_of_courses = input("How many courses did you finish? ")
# variable with integer value
num_of_course = int(num_of_courses)

# Declaring an empty list
course_marks = []

# 'While' iteration
i = 1
while (i <= num_of_course):
    # Populating/updating the list with values on each iteration
    course_marks.append(int(input(f"Enter your mark for the course {i}: ")))
    i += 1

# 'For' iteration to print the items of course_marks list
for mark in course_marks:
    print(mark)


# Part 2: Find the average / mean

# loop through the marks to find the total marks
total_marks = 0
for x in range(len(course_marks)):
    total_marks += course_marks[x]

# finding average
average = total_marks / num_of_course

# formatting average for 2 decimal places
avg = format(average, '.2f')
print(f"Your average for your {num_of_course} courses is: {avg}")


# Part 3: Output the grade using 'if - elif' condition
if (average >= 90 and average <= 100):
    print("Your grade is A+")
elif (average >= 80 and average <= 89):
    print("Your grade is B")
elif (average >= 70 and average <= 79):
    print("Your grade is C")
elif (average >= 60 and average <= 69):
    print("Your grade is D")
elif average < 60:
    print("Your grade is F")

print('--------- PYTHON ASSIGNMENT By Josy George -----------')
