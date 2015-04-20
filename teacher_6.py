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

# Add your function below!
#define function called average with argument numbers
def average(numbers):
    #add the numbers together by calling function sum to create total
    total = sum(numbers)
    #make the total a decimal number using float
    total = float(total)
    #divide total by length of number list using len()
    total = total / len(numbers)
    return total
 #using average from above, you can then create a weighted average   
def get_average(student):
    # variable = function(arguement["list in dictionary"])
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    # 0.1 is 10% of the weight that needs to be added - eg, homework only makes up 10%, quizzes are 30% and 60% is for tests. \ = code continues to the next line MAKE SURE YOU DONT USE /!!
    return 0.1 * average(student["homework"]) \
           +  0.3 * average(student["quizzes"]) \
           + 0.6 * average(student["tests"])
    