import random
import Quiz

# Multichoice Questions
# Type > Difficulty > Question > Options > Answer
mc1 = ["MC", 2, "Which is the correct pseudo code for a while loop:", "WHILE … ENDWHILE", "While … Endwhile", "WHILE … END", "While (…)" , 1]
mc2 = ["MC", 1, "Which option applies to two’s comp?", "- Sign", "- Significant bit", "Decimal", "8 bit", 2]
mc3 = []
mc4 = []
mc5 = []
mc6 = []
mc7 = []
mc8 = []
mc9 = []
mc10 = []
# Fill in the Blank Questions
# Type > Difficulty > Question > Answer
fib1 = ["FIB", 2, "root.____", "destroy()"]
fib2 =[]
fib3 = []
fib4 = []
fib5 = []
# Rank in order Questions
# Type > Difficulty > Question > Order
rio1 = ["RIO", 3, "Rank in order of smegma", ["Goon Ward", "Aiden", "Max"]]
rio2 = []
rio3 = []
rio4 = []
rio5 = []

def random_questions():
    questions = {mc1, mc2, mc3,mc4 , mc5, mc6, mc7, mc8, mc9, mc10,
                 fib1, fib2, fib3, fib4, fib5,
                 rio1, rio2, rio3, rio4, rio5
                 }

    