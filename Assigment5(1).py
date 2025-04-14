dictionary = {"Alice":"85","randy":"40"}
names = str(input("Enter student name : "))
if names in dictionary:
    print(f'{names} marks : {dictionary[names]}')
else:
    print("Student not found")