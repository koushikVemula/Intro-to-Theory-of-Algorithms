#Dynamic memoized function
def totalPossibilities(b,n,k) :
    memo = [] #Array for memoization
    for i in range(b+1) :
        memo.append([-2]*(n+1)) #Putting -2's to let system know if its yet to be calculated or not
        
    
    def instance(b,ni) : # It represents the instnace where we run 'b' robots and 'ni' stacks
        if b>(ni)*k : #robots more than places to place them
            return 0
        if b==(ni)*k: # robots equal to number of stacks multiplied by size to arrange them
            return 1
        if memo[b][ni] != -2 : #return if already calculated
            return memo[b][ni]
        
        z = ni-1 #caclculating required amount of high, low to use dynamic for the current points
        mini=0
        if (z*k)<b : #analyzing when to change low value
            mini = b-(z*k)
        max = min(b,k)
        ct = 0
        
        for j in range(b-max,b-mini+1,1) : #dynamic programming for the given program
            ct+=instance(j,ni-1)
        memo[b][ni] = ct
        return(memo[b][ni])
    
    print("(",b,",",n,",",k,") = ",instance(b,n),sep='')

#Read Filename from command prompt
import sys
filename =sys.argv[-1]

#Reading file using csv techniques
import csv
reader = csv.reader(open(filename), delimiter="\t")

#Iterating for each row in inputFile
for row in reader:
        for i in row :
            [b,n,k]=[int(x) for x in i.split()]
            totalPossibilities(b,n,k)