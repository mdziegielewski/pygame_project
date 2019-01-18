#variableName = open("fileName.extension", ""editingType")

out = open("firstFile.txt", "w")    # w - writing , if doesn't exist create one
                                    # overwrites the file
intOut = 7
out.write(str(intOut) + "_")      #only string type
out.close()


out = open("firstFile.txt", "a")    # a - appending

out.write("\nappendingTest")
out.close()


with open("firstFile.txt", "a") as out:     #out-variable
    out.write("\ntest with")                #not necessary to close()
