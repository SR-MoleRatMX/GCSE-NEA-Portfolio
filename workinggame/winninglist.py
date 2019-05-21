from cardmain import winninglist

#l1 = 

#print( "----------" )
#winnername = input( "What is the name of the winner?\n>" )

#winninglist.append( winnername )

filehandle = open("scoretable.txt", "a")

#with open("scoretable.txt", "a") as filehandle:

for i in range(5):
    if len(winninglist) > len(filehandle.readline(i)):
        string.replace(winninglist)
        break
        
