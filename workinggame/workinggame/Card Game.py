with open("scoretable.txt", "r") as filehandle:
    l1 = filehandle.readline(1)
    l2 = filehandle.readline(2)
    l3 = filehandle.readline(3)
    l4 = filehandle.readline(4)
    l5 = filehandle.readline(5)

from cardmain import winninglist
x = 0

if x == 0 and len(winninglist) > len(l1):
    with open("scoretable.txt", "w") as filehandle:
        filehandle.write("%s" %winninglist)
        filehandle.write("%s" %l1)
        filehandle.write("%s" %l2)
        filehandle.write("%s" %l3)
        filehandle.write("%s" %l4)
        x = 1

elif x == 0 and len(winninglist) > len(l2):
    with open("scoretable.txt", "w") as filehandle:
        filehandle.write("%s" %l1)
        filehandle.write("%s" %winninglist)
        filehandle.write("%s" %l2)
        filehandle.write("%s" %l3)
        filehandle.write("%s" %l4)
        x = 1

elif x == 0 and len(winninglist) > len(l3):
    with open("scoretable.txt", "w") as filehandle:
        filehandle.write("%s" %l1)
        filehandle.write("%s" %l2)
        filehandle.write("%s" %winninglist)
        filehandle.write("%s" %l3)
        filehandle.write("%s" %l4)
        x = 1

elif x == 0 and len(winninglist) > len(l4):
    with open("scoretable.txt", "w") as filehandle:
        filehandle.write("%s" %l1)
        filehandle.write("%s" %l2)
        filehandle.write("%s" %l3)
        filehandle.write("%s" %winninglist)
        filehandle.write("%s" %l4)
        x = 1

elif x == 0 and len(winninglist) > len(l5):
    with open("scoretable.txt", "w") as filehandle:
        filehandle.write("%s" %l1)
        filehandle.write("%s" %l2)
        filehandle.write("%s" %l3)
        filehandle.write("%s" %l4)
        filehandle.write("%s" %winninglist)
        x = 1

else:
    with open("scoretable.txt", "w") as filehandle:
        filehandle.write("%s" %l1)
        filehandle.write("%s" %l2)
        filehandle.write("%s" %l3)
        filehandle.write("%s" %l4)
        filehandle.write("%s" %l5)

