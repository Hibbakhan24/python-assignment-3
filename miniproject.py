# Taking input from user
math = int(input("Enter Math marks: "))
english = int(input("Enter English marks: "))
science = int(input("Enter Science marks: "))

# Store in dictionary
marks = {
    "Math": math,
    "English": english,
    "Science": science
}

# Calculate total
total = sum(marks.values())

# Calculate average
average = total / 3

# Display results
print("Total Marks:", total)
print("Average Marks:", average)

# Grade system
if average >= 80:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
else:
    print("Grade: C")