import random
import Quiz
import AMOW

### ### Questions ### ###

# Multichoice Questions #
# Type > Difficulty > Question > Options > Answer
mc1 = ["MC", 1, "Which is the correct pseudo code for a while loop:", "WHILE ... ENDWHILE", "While ... Endwhile", "WHILE ... END", "While (...)", 1]
mc2 = ["MC", 1, "Which option applies to a two's comp binaries leftmost bit?", "- Sign", "- Significant bit", "Stores decimals", "8 bit", 2]
mc3 = ["MC", 1, "Which is the best option for storing decimals?", "Float", "Bool", "Int", "Char", 1]
mc4 = ["MC", 1, "Which of the data structures is unordered?", "List", "Tuple", "Stacks", "Set", 4]
mc5 = ["MC", 2, "Which debugging tool would be best to find the error in this pseudo code?\nSET age 18\nIF age > 18 THEN\n  SET can_vote True\nENDIF", "Breakpoints", "Watches", "IDE Debug", "Output Statements", 4]
mc6 = ["MC", 1, "Which error doesn't throw an error message?", "Syntax", "Import", "Logic", "Runtime", 3]
mc7 = ["MC", 2, "What is the decimal value of the green channel in this hexadecimal RGBA value?\n#a3fff101", "241", "255", "163", "256", 2]
mc8 = ["MC", 2, "The two following unsigned bytes are added together. What is the resulting value in decimal?\n1111 1111 + 0000 0001", "0", "255", "256", "1", 1]
mc9 = ["MC", 2, "Which data type would be most appropriate for storing a phone number?", "Int", "Float", "String", "Text", 3]
mc10 = ["MC", 2, "Which is the decimal value of this two's comp binary: 1100?", "24", "-24", "8", "-8", 4]

# Fill in the Blank Questions #
# Type > Difficulty > Question > Answer
fib1 = ["FIB", 2, "A _____ is a python built-in data structure that follows LIFO.", "Stack"]
fib2 =["FIB", 3, "The time complexity of linear search is represented in big \"O\" notation as_____.", "O(n)"]
fib3 = ["FIB", 3, "The _________ symbol is used on an algorithm flow chart to indicate the beginning and end of an algorithm.", "Terminator"]
fib4 = ["FIB", 2, "A ___ - Test Loop always executes at least once.", "Post"]
fib5 = ["FIB", 3, "A _____ is a keyword often used to create custom data structures", "Class"]

# Rank in order Questions #
# Type > Difficulty > Question > Order
rio1 = ["RIO", 1, "Rank in order of largest to smallest for the max value:", ["Double", "Float", "Int64"]]
rio2 = ["RIO", 2, "Rank the order of the last three steps in the waterfall software design approach:", ["Implementation", "Verification", "Maintenance"]]
rio3 = ["RIO", 2, "Rank in the order of reliability for help in programming for:", ["W3 Schools", "Stack Overflow", "Reddit"]]
rio4 = ["RIO", 1, "Rank the order in which these If statements would appear:", ["If", "Else If", "Else"]]
rio5 = ["RIO", 3, "Rank the order of the sorting algorithms from most efficient to least:", ["Merge Sort", "Bubble Sort", "Bogo Sort"]]

# Creates a list containing all the questions, displays the all the questions in random order, then runs the AMOW.amow function\
# Inputs the Dict dictionary
# Outputs the Dict dictionary to AMOW.amow and run_quiz functions as well as outputting the list of questions to run_quiz
def random_questions(Dict):
    questions = [mc1, mc2, mc3,mc4 , mc5, mc6, mc7, mc8, mc9, mc10,
                 fib1, fib2, fib3, fib4, fib5,
                 rio1, rio2, rio3, rio4, rio5]
    # Loops through the list of questions, removing each question as it goes to avoid repeats
    while len(questions) > 0:
        questions = run_quiz(Dict, questions)
    AMOW.amow(Dict)

# Randomly selects and displays a question from the list, removes it and loops until all questions have been randomly shown
# Inputs Dict dictionary and questions list
# Outputs Dict dictionary and question (A singular list from the questions list)
# Returns questions list
def run_quiz(Dict, questions):
    # Grabs a random item from the list
    sample = random.sample(questions, 1)
    # The sample itself is a list so this undoes that
    question = sample[0]
    # Displays the question based on its type (MC, FIB or RIO)
    match question[0]:
        case "MC":
            Quiz.mc_question(Dict, question)
        case "FIB":
            Quiz.fib_question(Dict, question)
        case "RIO":
            Quiz.rio_question(Dict, question)
    questions.remove(question)
    return questions
