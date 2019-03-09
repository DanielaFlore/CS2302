#Course:CS2302
#aAuthor:Daniela Flores
#Lab3
#Instructor:Olac Fuentes
#T.A: Dita Nath
#date of last Mod: 3/8/19
#purpose of program: in this program I had to write various functions to better understand binary seach trees.
import matplotlib.pyplot as plt 

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def Smallest(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
        
def height(bst):
    if bst is None:
        return 0
    else:
        return 1 + max(height(bst.left), height(bst.right))        
###################################################
        
# traverses thtough a bst iteravely to search for a given value  
def iterativeSearch(T, x): 
    # Base Case  
    if (T == None): 
        return False 
  
    while T != None:
        if x == T.item:
            return True
        #if root is bigger than element given, itll keep iterating left subtree
        elif x < T.item:
            T = T.left
         #if root is smaller than element given, itll keep iterating right subtree    
        elif x > T.item:
            T = T.right
    #if done iterating though tree and element not found, return false        
    return False        
        
########################################################
#prints all elements throught the different depths of bst    
def treeDepth(T):
  #makes a copy of T
  currentL = [T]
  #counter
  i = 0
  #iterates till no more items are added to list
  while len(currentL) != 0:
    print('Keys at depth %d:' % i, end=' ' )
    #create empty list
    nextL = list()
    #iterates through elements of currentL
    for n in currentL:
      print (n.item, end = ' ')
      if n.left is not None:
         nextL.append(n.left)
      if n.right is not None: 
         nextL.append(n.right)
    print('')
    i = i+1
    currentL = nextL 
                    
####################################################        
#The recursive step makes two recursive calls to find the sum of the sub trees.
# When the recursive calls complete, we add the parent and return the total        
def total (T):
    if T is None:
        return 0
    return total(T.left)+ total(T.right) +T.item
###############################################
#gets tree and returns sorted list
def treeToSortedL(tree,A):
    if tree == None: 
        return 0
    treeToSortedL(tree.left,A)
    A.append(tree.item)
    treeToSortedL(tree.right,A)
    return A

#################################################
#draws a tree figure
def treeFig(ax, c, T, dx, dy):
    #checks if theres a left child
	if T.left is not None:
        #line is drawn for left child
		ax.plot([c[0], c[0]-dx], [c[1], c[1]-dy], color='k')
        #recursion call with left child as root
		treeFig(ax, [c[0]-dx, c[1]-dy], T.left, dx*0.9, dy*0.9)
    #checks if theres a right child    
	if T.right is not None:
        #line is drawn for right child
		ax.plot([c[0], c[0]+dx], [c[1], c[1]-dy], color='k')
        #recursive call with right child in parameter
		treeFig(ax, [c[0]+dx+3, c[1]-dy+3], T.right, dx*0.9, dy*0.9)
    #plots a circle at given coordinates    
	plt.plot(c[0], c[1],'wo', markersize=23, markeredgecolor='black') 
    #nodes value is inserted inside drawn circle
	ax.text(c[0]-5, c[1], T.item, size=8, weight='bold') 
###################################################
# when given a list it creates a balanced tree    
def balancedTree(L):
    if L:
        # gets the middle element of the array
        midEl = len(L)//2
        # sets the root of the BTree to middle element
        T = BST(L[midEl])
        T.left = balancedTree(L[:midEl])
        T.right = balancedTree(L[midEl+1:])
        return T
 #################################################       
    
# Code to test the functions above
T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140]
for a in A:
    T = Insert(T,a)
    

B = [70, 50, 90, 130,35,20]
B.sort()  
    

print('original binary search tree:')
InOrderD(T,'')
print()

List=[]
print('bst to sorted list:',treeToSortedL(T,List))
print('')
treeDepth(T)
print('')
print('iteravely searching for 1192:',iterativeSearch(T,1192))
print('iteravely searching for %d:'% A[1],iterativeSearch(T,A[1]))
print('')
#creates and prints out balanced tree
print('balanced tree:')
BT = balancedTree(B)
InOrderD(BT,' ')
#draws Tree figure
plt.close("all")
fig, ax = plt.subplots()
treeFig(ax, [0,0], T, 60, 60)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('trees.png')

