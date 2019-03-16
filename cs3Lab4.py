#Course:CS2302
#aAuthor:Daniela Flores
#Lab4
#Instructor:Olac Fuentes
#T.A: Dita Nath
#date of last Mod: 3/15/19
#purpose of program: in this program I had to write various functions to better understand BTrees.
import math
class BTree(object):
    # Constructor
    def __init__(self,item=[],child=[],isLeaf=True,max_items=5):  
        self.item = item
        self.child = child 
        self.isLeaf = isLeaf
        if max_items <3: #max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items%2 == 0: #max_items must be odd and greater or equal to 3
            max_items +=1
        self.max_items = max_items

def FindChild(T,k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree    
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)
             
def InsertInternal(T,i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T,i)
    else:
        k = FindChild(T,i)   
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k,m) 
            T.child[k] = l
            T.child.insert(k+1,r) 
            k = FindChild(T,i)  
        InsertInternal(T.child[k],i)   
            
def Split(T):
    #print('Splitting')
    #PrintNode(T)
    mid = T.max_items//2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid]) 
        rightChild = BTree(T.item[mid+1:]) 
    else:
        leftChild = BTree(T.item[:mid],T.child[:mid+1],T.isLeaf) 
        rightChild = BTree(T.item[mid+1:],T.child[mid+1:],T.isLeaf) 
    return T.item[mid], leftChild,  rightChild   
      
def InsertLeaf(T,i):
    T.item.append(i)  
    T.item.sort()

def IsFull(T):
    return len(T.item) >= T.max_items

def Insert(T,i):
    if not IsFull(T):
        InsertInternal(T,i)
    else:
        m, l, r = Split(T)
        T.item =[m]
        T.child = [l,r]
        T.isLeaf = False
        k = FindChild(T,i)  
        InsertInternal(T.child[k],i)          
        
def Search(T,k):
    # Returns node where k is, or None if k is not in the tree
    if k in T.item:
        return T
    if T.isLeaf:
        return None
    return Search(T.child[FindChild(T,k)],k)
                  
def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t,end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i],end=' ')
        Print(T.child[len(T.item)])    
 
def PrintD(T,space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
    else:
        PrintD(T.child[len(T.item)],space+'   ')  
        for i in range(len(T.item)-1,-1,-1):
            print(space,T.item[i])
            PrintD(T.child[i],space+'   ')
    
def SearchAndPrint(T,k):
    node = Search(T,k)
    if node is None:
        print(k,'not found')
    else:
        print(k,'found',end=' ')
        print('node contents:',node.item)
######################################################################
####################################################    
#returns height of BTree by adding 1 till leaves are reached        
def height(T):
    if T.isLeaf:
        return 0
    return 1 + height(T.child[0])
####################################################  
#returns smallest element in BTree       
def smallAtDepth(T,d):
#when reaching desired depth, itll return its first element 
  if d == 0:
    return T.item[0]    
#checks if given depth 'd' is the one were leaves are, if it is continue
# if not, that means given depth 'd' is greater than height of tree, therefore return inf
  if T.isLeaf:
    if d != 0:
        return math.inf

  else:
    return smallAtDepth(T.child[0],d-1)
#######################################################
#returns largest element in BTree    
def largestAtDepth(T,d):
#checks if given depth 'd' is the one were leaves are, if it is continue
# if not, that means given depth 'd' is greater than height of tree, therefore return inf
  if T.isLeaf:
    if d != 0:  
        return math.inf
#when reaching desired depth, the last element will be returned 
  if d == 0:
    return T.item[-1]
  else:
    return largestAtDepth(T.child[-1],d-1)
######################################################
#when given a key, this method will return the depth the key was found or -1 if it wasnt found    
def depthOfKey(T,k,h):
    #checks if k is in elements of current depth
    if k in T.item:
        return 0
    if T.isLeaf:
        #if statement checks if key wasnt found in leaves
        if k not in T.item:
        # since it has already traversed through whole tree without finding the key,depth would be 
        #equal to the height of tree, therefore to make it return -1, I subtracted the height of tree
        #to make it equal 0, then added -1
          return -h+-1
    else:
      #one is added every time it goes down Btree to keep track of which depth is operating at.
      return 1+ depthOfKey(T.child[FindChild(T,k)],k,h)
#########################################################3
#turns BTree to sorted list
def BTreeToList(T,L):
    #it appends leaves elements into list
    if T.isLeaf:
        for t in T.item:
            L.append(t)
    else:
        #traverses through the children
        for i in range(len(T.item)):
            BTreeToList(T.child[i],L)
            #appends items into list
            L.append(T.item[i])
        BTreeToList(T.child[len(T.item)],L)
   #sorted list is returned     
    return L
#######################################################
#returns the number of leaves that are full    
def fullLeaves(T):
    # counter to keep track of full leaves
    counter = 0
    if T.isLeaf:
        #checks if leaf node is full or not
        if len(T.item) ==T.max_items:
            return 1
        else:
            return 0
    #tarverses through children     
    for i in range(len(T.child)):
        counter+= fullLeaves(T.child[i])
    return counter    
########################################################
#returns how many nodes are at given depth    
def nodesAtDepth(T,d):
    counter = 0
    #if node is found at depth d, return 1 
    if d == 0:
        return 1
    #returns 0 if the depth leaves are isnt the depth wanted
    if T.isLeaf:
        return 0
    #traverses through children
    for i in range(len(T.child)):
        counter += nodesAtDepth(T.child[i],d-1)
    return counter
##########################################################
#prints items at given depth
def itemsAtDepth(T,d):
    #prints out items when desired depth is reached
    if d == 0:
        for j in range(len(T.item)):
         print(T.item[j],end=' ')

    #returns 0 if depth of leaves isnt the one wanted
    if T.isLeaf:
        return 0
    #traverses through children
    for i in range(len(T.child)):
        itemsAtDepth(T.child[i],d-1)
#####################################################
#returns number of nodes in BTree that are full        
#length 2 = 5
#length 3 = 4
#length 1 = 1        
def numFullNodes(T,L):

    if T.isLeaf:
        #checks if leaf nodes are full or not
        if len(T.item) ==T.max_items:
            L.append(T.item)

    #checks if current node is full or not
    elif len(T.item) == T.max_items:
        L.append(T.item)

    #traverses children
    for i in range(len(T.child)):
        numFullNodes(T.child[i],L)
    #returns length of L, which has all full nodes stored in it
    return len(L)
                

############################################################################
L = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5,105, 115, 200, 2, 45, 6]
T = BTree()    
for i in L:
    Insert(T,i)
    
PrintD(T,'') 
print('height:',height(T))
print('')
hT = height(T)
print('')
print('depth of key %d:'%L[0],depthOfKey(T,L[0],hT))
print('depth of key 1:',depthOfKey(T,1,hT))
print('depth of key 60:',depthOfKey(T,60,hT))
print('depth of key 300:',depthOfKey(T,300,hT))
print()


print('smallest at depth %d: '%2,end = '')
print(smallAtDepth(T,2))
print('largest at depth %d: '%2,end = '')
print(largestAtDepth(T,2))
print('')
    
L = []
print('Btree to sorted list: ',BTreeToList(T,L))    
print('')    

print('num of full leaves:',fullLeaves(T))

print('nodes at depth %d:'%1,nodesAtDepth(T,1))
print('items at depth 1:',end = ' ') 
itemsAtDepth(T,1)
print()
M = []
print('Number of full nodes in Tree:', numFullNodes(T,M))



