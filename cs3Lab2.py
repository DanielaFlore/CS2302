#Course:CS2302
#aAuthor:Daniela Flores
#Lab2
#Instructor:Olac Fuentes
#T.A: Dita Nath
#date of last Mod: 2/26/19
#purpose of program: in this program I had to write methods thatll sort a non native python list. I had to implement 
#bubble sort, quick sort, merge sort and a modified version of quick sort 
import random 
 #Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
     #inserts element given at the beginning of linked list       
def Prepend(L,x):
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:    
        L.head=Node(x,L.head)   
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 

def PrintRec(L):
    # Prints list L's items in order using recursion
    PrintNodes(L.head)
    print() 
    
def Remove(L,x):
    # Removes x from list L
    # It does nothing if x is not in L
    if L.head==None:
        return
    if L.head.item == x:
        if L.head == L.tail: # x is the only element in list
            L.head = None
            L.tail = None
        else:
            L.head = L.head.next
    else:
         # Find x
         temp = L.head
         while temp.next != None and temp.next.item !=x:
             temp = temp.next
         if temp.next != None: # x was found
             if temp.next == L.tail: # x is the last node
                 L.tail = temp
                 L.tail.next = None
             else:
                 temp.next = temp.next.next
         
def PrintReverse(L):
    # Prints list L's items in reverse order
    PrintNodesReverse(L.head)
    print()
    # empties L to en empty list
def emptying(L):

    L.head = None
    L.tail = None        
###########################################################
def bubbleSort(L):
    #O(n^2)
    change = True
    while change:
        t = L
        t = L.head
        change = False
        count = 0
        while t.next is not None:
            count +=1
            if t.item > t.next.item:
                temp = t.item
                t.item = t.next.item
                t.next.item = temp
                change = True
            t = t.next
########################################################## 
def mergeSort(L):
    #checks if list is long enough
    if getLength(L) > 1:
        p1 = List()
        p2 = List()
        t = L.head
        #splits list into halves
        for i in range(getLength(L) //2):
            Append(p1, t.item)
            t=t.next
        while t != None:   
            Append(p2, t.item)
            t = t.next
        #merge sorts the two halves
        mergeSort(p1)
        mergeSort(p2)
        #restores L to an empty list
        emptying(L)
        #puts together lists into L
        mergeTgthr(L, p1, p2)
        
        
        
def mergeTgthr(L,p1, p2):
    #temp var for split lists
    firstH = p1.head
    secH = p2.head
    #brings together list in order by comparing elements of both split lists
    while firstH != None and secH != None:
        if firstH.item < secH.item:
            Append(L, firstH.item)
            firstH = firstH.next
        else:
            Append(L, secH.item)
            secH = secH.next
    # if statements cover if the halves arent of same length        
    if secH is None:
        while firstH != None:
            Append(L, firstH.item)
            firstH = firstH.next
    if firstH is None:
        while secH != None:
            Append(L, secH.item)
            secH = secH.next
##########################################################
# populates list of size n with random intergers 
def randomListGen(n):
    #i = 0
    R = List()
    for i in range(n):
       Append(R,random.randrange(101))
        # L.append(random.randrange(101))
    return R  
#gets length of given list
def getLength(L):
    temp = L.head
    count = 0
    while temp is not None:
        temp = temp.next
        count += 1
    return count
######################################################
# copies list given into a new one    
def copyList(N):
    # Prints list L's items in order using a loop
        clone = List()
        te = N.head
       #clone = List()
        while te is not None:
            Append(clone,te.item)
            te = te.next
        return clone  
######################################################
# finds median        
def findMiddle(t,halfIndex):
    iter = t.head
    for i in range(halfIndex):
        midElement = iter.item
        iter = iter.next
    return midElement
###########################################
def quickSort(L):
    # cheks that LL that is passed is large enough
    if getLength(L) > 1:
        # pivot is head of list
        pivot = L.head.item
        # lists that are going to store the two halves of the original list
        p1 = List()
        p2 = List()
        #stores the element after head into 't' because its already the pivot
        t = L.head.next
        while t != None:
            # if element is smaller than pivot its stored in p1 list
            if t.item < pivot:
                Append(p1, t.item)
             # if element is bigger than pivot its stored in p2 list    
            else:
                Append(p2, t.item)
            t = t.next
        #recursively sorts the halves
        quickSort(p1)
        quickSort(p2)
        # inserts pivot into p1 if p1 is empty
        if IsEmpty(p1):
            Append(p1, pivot)
        #inserts pivot into p2s head if p1 is not empty    
        else:
            Prepend(p2, pivot)
        #reconnects the halves of the list
        if IsEmpty(p1):
            L.head = p2.head
            L.tail = p2.tail
        else:     
            p1.tail.next = p2.head
            L.head = p1.head
            L.tail = p2.tail
#####################################################        
###################################################### 
#length of list            
numOfLLElements = 10
# half of list length
half = numOfLLElements //2
M = List()
M = randomListGen(numOfLLElements)
print('original list:') 
Print(M)
print('')
C = List()
C = copyList(M)
D = List()
D = copyList(M)
E = List()
E = copyList(M)
print('list sorted though bubble sort:')
bubbleSort(C)
Print(C)
print('middle element of Linked List sorted by BubbleSort',findMiddle(C,half))
print('')
quickSort(D)
print('list sorted though Quick sort:')
Print(D)
print('middle element of Linked List sorted by QuickSort',findMiddle(D,half))
print('')
print('list sorted though merge sort:')
mergeSort(E)
Print(E)
print('middle element of Linked List sorted by merge Sort',findMiddle(E,half))
print('')

            
    