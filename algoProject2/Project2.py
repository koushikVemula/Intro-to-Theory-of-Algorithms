#I am solving this problem assuming the given inputs as vertices of the graph.
#All the points reachable from a given point as its directed edges which will be stored in a adjcencyList 
#Using DFS algorithm to solve the problem
#Using 2d representation to represent vertices to have similarities with input data for easy referencing

#------Increasing recursion limit to run for large files--------
import sys
sys.setrecursionlimit(10**4)


#------Support Functions for the Code-------
#-------------------------------------------
#Function to get the number of steps taken by graph to go from point x to point y 
def value(x,y) :
    return max(abs(x[0]-y[0]),abs(x[1]-y[1]))

#Function to convert directions to values
# Value associated with direction
# W  - (-1,0)
# N  - (0,1)
# S  - (0,-1)
# E  - (1,0)
def values(str):
    row,col=0,0
    if "N" in str :
        row-=1
    elif "S" in str:
        row+=1
    if "W" in str:
        col-=1
    elif "E" in str:
        col+=1
    return row,col
#-------------------------------------------

#---Reading command Line arguments----------
#-------------------------------------------
#Reading Input and OutputFile names from command prompt
import sys
fileInput =sys.argv[-2]
fileOutput = sys.argv[-1]

#Reading InputFile using csv techniques
import csv
reader = open(fileInput,"r")
#-------------------------------------------

#Using rows and columns to get vertices for better representation of the graph
FirstLine = reader.readline()
rows,cols =[int(i) for i in FirstLine.split(" ")] #Getting number of rows and columns from first line in input

#Splitting Direction and colorValue of a vertices to graphDir and graphData for easy caculation
graphDir = []
graphData = []
r=-1

#Initializing inputs from inputFile to graphDir and graphData
#For Example R-S will be saved as R in graphData and S in graphDir
for row in reader:
    r+=1
    c=0
    rowData=[]
    rowDir=[]
    for i in row.split(' ') :
        if(i!="") :
            if(i=="\n"):
                continue
            if(i=="O") :
                rowData.append("O")
                rowDir.append("T")
                continue
            data=i.split("-")
            rowData.append(data[0])
            rowDir.append(data[1])
            c+=1
    graphData.append(rowData)
    graphDir.append(rowDir)
#Creation of Adjacency List instead
adjacenceyList = []
cellData=[]
for i in range(0,rows) :
    adjacencyRow=[] # Adjacency List for given row
    for j in range(0,cols) :
        data=[] #Adjacency List for given element
        if(graphData[i][j]=="R") :
            x,y=values(graphDir[i][j])
            l=(i+x)
            m=(j+y)
            while((l>=0 and l<rows) and ((m>=0) and m<cols)) : #Condition to stop index-out of bounds
                if(graphData[l][m]=="B" or graphData[l][m]=="O") :
                    data.append([l,m]) #Adding directed edge
                l=l+x
                m=m+y    
        elif(graphData[i][j]=="B") : #Same Logic as above simply replacing colors R and B
            x,y=values(graphDir[i][j])
            l=(i+x)
            m=(j+y)
            while((l>=0 and l<rows) and ((m>=0) and m<cols)) : #Condition to stop index-out of bounds
                if(graphData[l][m]=="R" or graphData[l][m]=="O") :
                    data.append([l,m]) #Adding directed edge 
                l=l+x
                m=m+y 
        adjacencyRow.append(data)#Appending cell value to row
    adjacenceyList.append(adjacencyRow)#Appending row to AdjacencyList


#Reference to below program - https://www.geeksforgeeks.org/find-paths-given-source-destination/
#The below recurrence function originally prints all the paths from source to destination
#It has been modified to stop running after first path has been calculated


#Using ----DFS----
def getPathDFS(u,v,path) :
    visited[u[0]][u[1]] = 1
    path.append(u)
    if(u[0]==v[0] and u[1] == v[1]) :#Condition to check that we reached destination
        #writing path in the required format to the output file which is given by user
        f=open(fileOutput,"w")
        n=len(path)
        ans=""
        for i in range(0,n-1) :
            k=value(path[i],path[i+1]) 
            ans=ans+str(k)+graphDir[path[i][0]][path[i][1]]+" "
        ans.strip()
        f.write(ans)
        #We have gotten the path, terminating further execution of program to avoid time wastage by returning value '0' 
        return 0
    else:
        for i in adjacenceyList[u[0]][u[1]]:
            if visited[i[0]][i[1]] == 0 :
                getPathDFS(i,v,path)
    path.pop()


    
visited = [ [0] * cols for _ in range(rows)] #visited array with all values as 0 at start
#[0,0] - Start of graph
#[rows-1,cols-1] - Destination of graph
#visited - List for applying DFS
#[] - Empty List for path
#adjacencyList - For providing information on edges for created graph
getPathDFS([0,0],[rows-1,cols-1],[])