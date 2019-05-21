with open("scoretable.txt", "r") as filehandle:
    l1 = filehandle.readline()
    l2 = filehandle.readline()
    l3 = filehandle.readline()
    l4 = filehandle.readline()
    l5 = filehandle.readline()

from cardmain import winninglist
x = 0

if x == 0 and len(winninglist) > len(l1):
    with open("scoretable.txt", "w") as filehandle:
        filehandle.write("%s" %winninglist)
        filehandle.write("%s" %l2)
        filehandle.write("%s" %l3)
        filehandle.write("%s" %l4)
        filehandle.write("%s" %l5)
        x = 1

elif x == 0 and len(winninglist) > len(l2):
    with open("scoretable.txt", "w") as filehandle:
        filehandle.write("%s" %l1)
        filehandle.write("%s" %winninglist)
        filehandle.write("%s" %l3)
        filehandle.write("%s" %l4)
        filehandle.write("%s" %l5)
        x = 1

elif x == 0 and len(winninglist) > len(l3):
    with open("scoretable.txt", "w") as filehandle:
        filehandle.write("%s" %l1)
        filehandle.write("%s" %l2)
        filehandle.write("%s" %winninglist)
        filehandle.write("%s" %l4)
        filehandle.write("%s" %l5)
        x = 1

elif x == 0 and len(winninglist) > len(l4):
    with open("scoretable.txt", "w") as filehandle:
        filehandle.write("%s" %l1)
        filehandle.write("%s" %l2)
        filehandle.write("%s" %l3)
        filehandle.write("%s" %winninglist)
        filehandle.write("%s" %l5)
        x = 1

elif x == 0 and len(winninglist) > len(l5):
    with open("scoretable.txt", "w") as filehandle:
        filehandle.write("%s" %l1)
        filehandle.write("%s" %l2)
        filehandle.write("%s" %l3)
        filehandle.write("%s" %l4)
        filehandle.write("%s" %winninglist)
        x = 1

elif x == 0:
    with open("scoretable.txt", "w") as filehandle:
        filehandle.write("%s" %l1)
        filehandle.write("%s" %l2)
        filehandle.write("%s" %l3)
        filehandle.write("%s" %l4)
        filehandle.write("%s" %l5)

