'''
Dictionary for Students marks
'''
try:
    Students_info = {"Bob" : "75", "Jack" : "66","Tom": "89","Alice":"78"}
    StudentName = input("Enter the Student's Name: ")
    print(f'''{StudentName}'s Marks: {Students_info[StudentName]}''')
except KeyError:
    print("Student not found.")
