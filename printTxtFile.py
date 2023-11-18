
def createTxtFile(distance: int):
    fileName: str = "textFile.txt"
    f = open(fileName, 'w')
    f.write("Bot ID - 1")
    f.write(f"Total Distance travelled - {distance}")
    f.write(f"Predicted End Time - {distance * 40 + (2 * 5)}")
    f.write("Handoffs - 0")
    f.close
