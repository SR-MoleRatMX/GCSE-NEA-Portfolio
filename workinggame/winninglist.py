from cardmain import winninglist

f = open ("highscore.txt", "r")
scoretable = f.read()

#l1 = f.readline(1)
#l2 = f.readline(2)
#l3 = f.readline(3)
#l4 = f.readline(4)
#l5 = f.readline(5)

#for comparison in range(0,5):
#    if len(winninglist) > len(f.readline(comparison)):
#        with open ("highscore.txt", "a") as filehandle:
#            filehandle.write("%s\n" % winninglist)
#    else:
#        with open ("highscore.txt", "a") as filehandle:
#            filehandle.write("%s\n" % comparison)
            

#code to add the newest winner to the high-score table
#with open ("highscore.txt", "a") as filehandle:
#    filehandle.write("%s\n" % winninglist)
