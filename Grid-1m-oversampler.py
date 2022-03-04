#INPUT FORMAT E N DEPTH
#OUTPUT CSV AT METRE ONLY

try:
    from math import *
except:
    print "import error"

#T = int(1) #flag for while loop - removed depricated code


#E = [] #new array to read from the RPL file - depricated
#N = []
#KP = []

gridE = [] #new array to write logfile values to
gridN = []
gridZ = []





    
OUTPUT1 = open("D:/temp/OUTPUT2.TXT", "w")

previous = str("0")



fileGRID = open("D:/SHEFA_acceptedXYZ/XYZExportFanoe.xyz", "r") #filename of grid file being processed
for line in fileGRID:
    splitline = line.split(" ")#split on space because of supplied data, might be comma or semicolon in future

    gridE = int(float((splitline[0])))
    gridN = int(float((splitline[1])))
    gridZ = float((splitline[2]))

    checker = str(gridE)#+str(gridN)

    if checker == previous:
        pass
    else:
        OUTPUT1.write(str(gridE)+","+str(gridN)+","+str(gridZ)+"\n\r")
        previous = str(gridE)#+str(gridN)
        #print "new line written to file"

    
fileGRID.close()
              

OUTPUT1.close()



        
