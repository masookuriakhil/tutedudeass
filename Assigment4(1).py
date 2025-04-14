
try:
    with open("sample.txt","r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: the file 'sample.txt' does not exist.")
finally:
    print("Execution as been done")



