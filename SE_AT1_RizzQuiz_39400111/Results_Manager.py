# Name / Filepath of where the results will be saved
filepath = "../Task1_Results.txt"

# Appends the users name, SID, results, and time they started quiz to the above file, creates the file if it doesn't exist also divides Dict["Score"] by 100, undoing the RAM manipulation protection measure
# Inputs Dict dictionary
# Outputs Dict dictionary to WriteToFile function
def AddResults(Dict):
    Dict["Score"] = Dict["Score"]//100
    CreateFile()
    WriteToFile(Dict)

# Creates the file to store results if it doesn't already exist
# Outputs creating a file based of filepath variable
def CreateFile():
    try:
        f = open(filepath, "x")
    except:
        return

# Appendss theusers name, SID, results, and time they started quiz to the txt file
# Inputs Dict dictionary
# Outputs Dict dictionary as a string to txt file
def WriteToFile(Dict):
    with open(filepath, "a") as f:
        f.write(str(Dict))