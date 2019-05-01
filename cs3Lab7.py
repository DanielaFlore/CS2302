#Course:CS2302
#aAuthor:Daniela Flores
#Lab7
#Instructor:Olac Fuentes
#T.A: Dita Nath
#date of last Mod: 4/30/19
#purpose of program: draw a maze with the help of a disjoint set forest to better
#understand this data structure,draw maze with the help of user input, do an 
#adjacency list based on the maze,and do various types of searches to solve the maze
import matplotlib.pyplot as plt
import numpy as np
import random
import time
from collections import deque
#method that draws maze, provided by Dr.Fuentes
def draw_maze(walls,maze_rows,maze_cols,cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1]-w[0] ==1: #vertical wall
            x0 = (w[1]%maze_cols)
            x1 = x0
            y0 = (w[1]//maze_cols)
            y1 = y0+1
        else:#horizontal wall
            x0 = (w[0]%maze_cols)
            x1 = x0+1
            y0 = (w[1]//maze_cols)
            y1 = y0  
        ax.plot([x0,x1],[y0,y1],linewidth=1,color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0,0,sx,sx,0],[0,sy,sy,0,0],linewidth=2,color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r*maze_cols   
                ax.text((c+.5),(r+.5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('off') 
    ax.set_aspect(1.0)

def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w =[]
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r*maze_cols
            if c!=maze_cols-1:
                w.append([cell,cell+1])
            if r!=maze_rows-1:
                w.append([cell,cell+maze_cols])
    return w
######################################################
#method that craetes a DSF with given size    
def DisjointSetForest(size):
    return np.zeros(size,dtype=np.int)-1
        
def find(S,i):
    # Returns root of tree that i belongs to
    if S[i]<0:
        return i
    return find(S,S[i])

def union(S,i,j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S,i) 
    rj = find(S,j) 
    if ri!=rj: # Do nothing if i and j belong to the same set 
        S[rj] = ri  # Make j's root point to i's root
        
####################################################
#union by compression
def union_by_size(S,i,j):
    ri = findC(S,i)
    rj = findC(S,j)
    if ri!=rj:
        if S[ri] > S[rj]: 
            S[rj] += S[ri]
            S[ri] = rj
        else: 
            S[ri]+=S[rj]
            S[rj] = ri
            

#finds the root using path compression
def findC(S,i):
    if S[i] < 0:
        return i
    r = findC(S,S[i])
    S[i] = r
    return r
          
            
####################################################
#method that returns True if theres more than one set in the disjoint set forest
# and false otherwise        
def numOfSets(forest):
    count = 0
    #counts number of sets
    for i in range(len(forest)):
        if forest[i] == -1:
            count = count +1
    if count>1:
        return True
    else:
        return False        
         
#method that will keep popping walls if the adjacent cells are not in the same set 
#draws maze with standard union
def wallsAsforests(walls,row,cols,bool):
    wList = [ [] for i in range(row*cols)]
    counter = 0
    forest = DisjointSetForest(row*cols)
    #while the disjoint set forest has more than 1 set this loop will keep iterating
    while numOfSets(forest) == True:
        #gets random integer 
        d = random.randint(0,len(walls)-1)
        #stores random wall
        randomWall = walls[d]
        #splits the wall's cordinate to get adjacent cells
        cellX = randomWall[0]
        cellY = randomWall[1]
        #checks if cells are not in same set
        if findC(forest,cellY) != findC(forest,cellX):
            #gets both cells to same set
            union(forest,cellX,cellY)
            #######################
            #creates adjacency list
            wList[cellX].append(cellY)
            wList[cellY].append(cellX)
            counter= counter+1
            #removes wall
            walls.pop(d)
    #draws finished maze
    draw_maze(walls,row,cols,cell_nums = bool)
    #returns adjacency representation of maze
    return wList
#modified version of method above to remove the # of walls provided by user    
def wallsAsForest7(walls,row,cols,wallsP):
    counter = 0
    forest = DisjointSetForest(row*cols)
    #if statement checks if number of walls being removed is bigger than
    #the cumber of cells
    if len(forest)<wallsP:
         while counter !=wallsP:
            #gets random integer 
            d = random.randint(0,len(walls)-1)
            #stores random wall
            randomWall = walls[d]
            #splits the wall's cordinate to get adjacent cells
            cellX = randomWall[0]
            cellY = randomWall[1]
            #checks if all cells are already in one set
            if numOfSets(forest) == False:
                #for loop removes additional walls 
                #to meet the desired number of walls the user
                #wants removed
                for i in range(wallsP-counter):
                    d = random.randint(0,len(walls)-1)
                    counter = counter+1
                    walls.pop(d)    
                break
            if findC(forest,cellY) != findC(forest,cellX):
                #gets both cells to same set
                union(forest,cellX,cellY)
                counter= counter+1
                #removes wall
                walls.pop(d)  
    else:        
        while counter !=wallsP:
            #gets random integer 
            d = random.randint(0,len(walls)-1)
            #stores random wall
            randomWall = walls[d]
            #splits the wall's cordinate to get adjacent cells
            cellX = randomWall[0]
            cellY = randomWall[1]
            #checks if cells are not in same set
            if findC(forest,cellY) != findC(forest,cellX):
                #gets both cells to same set
                union(forest,cellX,cellY)
                counter= counter+1
                #removes wall
                walls.pop(d)  
    #draws finished maze  
    draw_maze(walls,row,cols)
    
#method that does breath first search to solve maze    
def breadthFirst(G,v):
    visited = []
    visited = [False for i in range(len(G))]
    prev = []
    prev = [-1 for i in range(len(G))]
    Q = deque([])
    Q.append(v)
    visited[v] = True
    while Q:
        #popleft removes first element in Q
        u = Q.popleft()
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                Q.append(t)
    #returns solution of this search            
    return prev

#this method does the iterative verison of depth first search to solve maze
def ItDepthFirst(G,v):
    visited = []
    visited = [False for i in range(len(G))]
    prev = []
    prev = [-1 for i in range(len(G))]
    Q = []
    Q.append(v)
    visited[v] = True
    while Q:
        #gets last element
        u = Q.pop()
        for t in G[u]:
            if not visited[t]:
                visited[t] = True
                prev[t] = u
                Q.append(t)
    #returns solution of this search            
    return prev

#this method does the recursive depth first search to solve maze
def depthFirstR(G,source):
    visitedD[source] = True
    for t in G[source]:
        if not visitedD[t]:
            prevD[t] = source
            depthFirstR(G,t)
    #returns solution of this search        
    return prevD   
#this method prints the path solution given the list      
def printPath(prev,v):
    if prev[v] !=-1:
        printPath(prev,prev[v])
        print(" -> ", end=' ')
    print(v,end=' ')    
    
                
##########################################################################################    

maze_rows = 10
maze_cols = 10
cells = maze_rows*maze_cols
walls = wall_list(maze_rows,maze_cols)
print('lenwalls',len(walls))
print('number of cells:',cells)
#aks user how many walls it wants removed and stores answer
userInput = int(input('type number of walls you want to remove\n'))
#checks if users input is valid
if userInput>=0 and userInput<=len(walls):
    if userInput <cells-1:
        print('A path from source to destination is not guaranteed to exist')
    if userInput ==cells-1:
        print(' There is a unique path from source to destination')
    if  userInput >cells-1:
        print('There is at least one path from source to destination')
    plt.close("all")
    #draws maze with x num of walls rempoved, x being the users input     
    wallsAsForest7(walls,maze_rows,maze_cols,userInput,)    
    plt.show()
    walls2 = wall_list(maze_rows,maze_cols)    
    plt.close("all")
    #stores adjacency list representation of maze
    G = wallsAsforests(walls2,maze_rows,maze_cols,True)
    print('adjacency List:',G)
    ########################
    #BREADTH FIRST SEARCH
    print('breadth first')
    bFirst = breadthFirst(G,0)
    printPath(bFirst,len(G)-1)
    print('')
    ##########################
    #DEPTH FIRST SEARCH
    global visitedD
    visitedD = [False for i in range(len(G))]
    global prevD
    prevD = [-1 for i in range(len(G))]
    print('depth first iteravely')
    dFirst = ItDepthFirst(G,0)
    printPath(dFirst,len(G)-1)
    print('')
    ##########################
    #DEPTH FIRST SEARCH USING RECURSION
 
    print('depth first recursively')
    dFirstR = depthFirstR(G,0)
    printPath(dFirstR,len(G)-1)
    print('')
    plt.show()
    #start = time.time()
    #elapsedTime = time.time() - start
    #print('standard:',elapsedTime)     
else:
    print('invalid number of cells')      
   

