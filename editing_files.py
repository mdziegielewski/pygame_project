#variableName = open("fileName.extension", ""editingType")

out = open("firstFile.txt", "w")    # w - writing , if doesn't exist create one
                                    # overwrites the file
intOut = 7
out.write(str(intOut))      #only string type
out.close()


out = open("firstFile.txt", "a")    # a - appending

out.write("appendingTest")
out.close()


with open("firstFile.txt", "a") as out:     #out-variable
    out.write("\ntest with")                #not necessary to close()

#files reading
inputFile = open("firstFile.txt", "r")      #r - read
                                            # not necessary to use "r"
fileContent = inputFile.read()
print(fileContent)
inputFile.close()

print("-----------------")
inputFile = open("firstFile.txt", "r")
for line in inputFile:
    print(line) #end=""
inputFile.close()


print("-----------------")
with open("firstFile.txt", "r") as inputFile:
    line = inputFile.readline()
    line = inputFile.readline()
    print(line)


#file position

print("-----------------")
with open("firstFile.txt", "rb") as inputFile:  #b-byte
    line = inputFile.readline()
    line = inputFile.readline()
    print(line)
    inputFile.seek(1,0)    #offset, [from] /0-beginning, 1-current, 2-end
    print(inputFile.read(5))

    inputFile.seek(3,1)
    print(inputFile.read(3))

    inputFile.seek(-5,2)
    print(inputFile.read())
    print(inputFile.tell())     #current position

