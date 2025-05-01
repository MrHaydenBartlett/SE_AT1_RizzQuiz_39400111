import random
import Quiz

# Multichoice Questions
# Type > Difficulty > Question > Options > Answer
mc1 = ["MC", 2, "Which is the correct pseudo code for a while loop:", "WHILE … ENDWHILE", "While … Endwhile", "WHILE … END", "While (…)" , 1]
mc2 = ["MC", 1, "Which option applies to two’s comp?", "- Sign", "- Significant bit", "Stores decimals", "8 bit", 2]
mc3 = ["MC", 1, "Which is the best option for storing decimals?", "Float", "Bool", "Int", "Char", 1]
mc4 = ["MC", 1, "Which of the data structures is unordered?", "List", "Tuple", "Stacks", "Set", 4]
mc5 = ["MC", 1, "Which isn’t a debugging tool?", "Breakpoints", "Watches", "IDE Debug", "Half-Search", 4]
mc6 = ["MC", 2, "Which error doesn’t throw an error message?", "Syntax", "Import", "Logic", "Runtime", 2]
mc7 = ["MC", 2, "Which of the following isn’t hexadecimal?", "10", "3h", "ff", "a0", 2]
mc8 = ["MC", 2, "Which is not a software development approach?", "Zip", "Waterfall", "Agile", "Rad", 2]
mc9 = ["MC", 1, "Which data type can hold the largest number?", "Int", "Float", "Double", "Binary Tree", 2]
mc10 = ["MC", 1, "Which is the correct value of this two’s comp binary: 1100?", "192", "-192", "64", "-64", 4]
# Fill in the Blank Questions
# Type > Difficulty > Question > Answer
fib1 = ["FIB", 3, "A _____ is a data type that follows LIFO.", "Stack"]
fib2 =["FIB", 3, "The big “O” notation for linear time is represented as _____.", "O(n)"]
fib3 = ["FIB", 3, "The _________ symbol is used on an algorithm flow chart to indicate the beginning and end of an algorithm.", "Terminator"]
fib4 = ["FIB", 2, "A ___ - Test Loop always executes at least once.", "Post"]
fib5 = ["FIB", 2, "A _____ is a keyword often used to create custom data structures", "Class"]
# Rank in order Questions
# Type > Difficulty > Question > Order
rio1 = ["RIO", 1, "Rank in order of largest to smallest for the max value:", ["Double", "Float", "Int"]]
rio2 = ["RIO", 3, "Rank the order of the last three steps in the waterfall software design approach:", ["Implementation", "Verification", "Maintenance"]]
rio3 = ["RIO", 2, "Rank in the order of reliability for help in programming for:", ["W3 Schools", "Stack Overflow", "Reddit"]]
rio4 = ["RIO", 1, "Rank the order in which these If statements would appear:", ["If", "Else If", "Else"]]
rio5 = ["RIO", 3, "Rank the order of the sorting algorithms from most efficient to least:", ["Merge Sort", "Bubble Sort", "Bogo Sort"]]

def random_questions():
    questions = {mc1, mc2, mc3,mc4 , mc5, mc6, mc7, mc8, mc9, mc10,
                 fib1, fib2, fib3, fib4, fib5,
                 rio1, rio2, rio3, rio4, rio5
                 }

    