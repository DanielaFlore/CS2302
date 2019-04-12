#Course:CS2302
#aAuthor:Daniela Flores
#Lab6
#Instructor:Olac Fuentes
#T.A: Dita Nath
#date of last Mod: 4/10/19
#purpose of program: draw a maze with the help of a disjoint set forest to better
#understand this data structure


import matplotlib.pyplot as plt
import numpy as np
import random

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
def wallsAsforests(walls,row,cols):
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
        if find(forest,cellY) != find(forest,cellX):
            #gets both cells to same set
            union(forest,cellX,cellY)
            #removes wall
            walls.pop(d)
    #draws finished maze    
    draw_maze(walls,row,cols)

            
#########################################################            
maze_rows = 10
maze_cols = 15

walls = wall_list(maze_rows,maze_cols)
wallsAsforests(walls,maze_rows,maze_cols)
 