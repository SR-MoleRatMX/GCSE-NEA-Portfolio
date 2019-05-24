phrase = input(">")
counter = -1


with open ("scoretable.txt", "r") as filehandle:
    #filehandle.write("%s\n" %phrase)
    for line in filehandle:
        counter += 1

        if counter >! 4:
            while compare == ("y"):
                if line > winninglist:
                    filehandle.write(line)
                    compare = ("y")

                else:
                    filehandle.write(winninglist)
                    compare = ("n")

            while compare == ("n"):
                filehandle.write(line)
            

