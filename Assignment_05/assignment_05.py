#Task 1: Create a Dictionary of Student Marks
student = {
    "lionel" : 91,
    "cristiano" : 69,
    "neymar" : 43,
    "haaland" : 58,
    "lewandowski" : 70,
}
user = input ("Enter the student's name: ").lower()
if user in student:
    print (f'{user.title()}\'s marks: {student[user]}')
else:
    print("Student not found")


# Task 2: Demonstrate List Slicing
my_list  = list(range(1, 11))
first_five = my_list[:5]
reverse_five = first_five[::-1]
print(f'Original list: {my_list}\nExtracted first five element: {first_five}\nReversed extracted elements: {reverse_five}')
