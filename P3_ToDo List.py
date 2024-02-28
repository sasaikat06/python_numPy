myTask = []

title = input("Enter the title of your task : ")
description = input('Add descriptions : ')
dueDate = input('Date ? dd/mm/yyyy : ')
status = input("Completed :")

task = {
    "title" : title,
    "description" : description,
    "date" : dueDate,
    "status" : False
}

myTask.append(task)
print("Task added successfully")



