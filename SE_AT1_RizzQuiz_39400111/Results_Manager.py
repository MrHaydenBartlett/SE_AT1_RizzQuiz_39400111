filepath = "../Task1_Results.txt"

# Adds the results to the above file, creates the file if it doesn't exist
def AddResults(Dict):
    CreateFile(filepath)
    WriteToFile(Dict, filepath)

def CreateFile(filepath):
    try:
        f = open(filepath, "x")
    except:
        pass

def WriteToFile(Dict, filepath):
    with open(filepath, "a") as f:
        f.write(str(Dict))