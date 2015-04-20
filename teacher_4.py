lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}
students = [lloyd, alice, tyler]
for student in students:
   # for k, v in student.items(): 
      #  print k, v
    #continue            dan's code to show you don't need all the code below to create same thing
    print student["name"] #lists and dictionaries use [] unless you are creating a dictionary then it is the {}
    
    print "homework"
    print student["homework"]
    print "quizzes"
    print student["quizzes"]
    print "tests"
    print student["tests"]