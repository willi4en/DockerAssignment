import os
import io
import socket
from collections import Counter

dir_list = os.listdir(".")

resultFile = open("result.txt", "w")
resultString = ""
resultString += "Files in /home/data:\n"
resultString += f"{dir_list}" + "\n\n"

totalCount = 0
resultString += "Text Files:\n"
for file in dir_list:
    if file.endswith('.txt'):
        count = 0
        with open(file, 'r') as file:
            data = file.read()
            words = data.split()
            counterObj = Counter(words)
            count += len(words)
            totalCount += count
            countString = f"File: {file.name}  Word Counts: {counterObj.most_common(3)}" + "\n"
            resultString += countString

resultString += "\n"

hostName = socket.gethostname()
resultString += "Computer Name: " + hostName + "\n"
resultString += "IP Address: " + socket.gethostbyname(hostName)
resultString += "\n"
resultFile.write(resultString)
resultFile.close()
resultFile = open("result.txt", "r")
print("\n" + resultFile.read())
resultFile.close()
