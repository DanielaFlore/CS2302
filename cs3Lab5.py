
import numpy as np
import time
import math
""""""""""""
class HashTableC(object):
	# Builds a hash table of size 'size'
	# Item is a list of (initially empty) lists
	# Constructor
	def __init__(self,size):
		self.item = []
		self.num_items = 0
		for i in range(size):
			self.item.append([])
""""""""""""
class BST(object):
    # Constructor
    def __init__(self, item=[], left=None, right=None):
        self.item = item
        self.left = left
        self.right = right
""""""""""""
#Build HashTable
def ht(f, f2):
	print("\nBuilding hush table.\n")
	print("Hash Table stats:")
	H = HashTableC(19) #create Hash Table of length 17
	print("Initail table size", len(H.item))
	start = int(time.time()) #starting time
	for line in f: #read line by line, glove
		data = line.split(' ')
		if data[0].isalpha():
			H = InsertC(H, data) #insert data
	end = int(time.time()) #ending time
	print("Total elements: ", H.num_items)
	print("Final table size: ", len(H.item))
	print("Load factor: ", H.num_items/len(H.item))
	c, d = infolist(H)
	print("Percentage of empty lists:", c/len(H.item)*100)
	print("Standard deviation of the lengths of the lists:", d)
	print(H.item[int(d)+1])
	print("Running time for Hash Table construction:", (end-start))
	print("\nReading word file to determine similarities.\n")
	start2 = int(time.time()*1000)
	for line2 in f2: #read line by line, word_pair
		data2 = line2.split(',')
		e0 = FindC(H, data2[0]) #return array if string found
		e1 = FindC(H, data2[1]) #return array if string found
		print("Similarity", data2[0:2], " = ", round(np.sum(e0*e1)/(math.sqrt(np.sum(e0*e0))*math.sqrt(np.sum(e1*e1))),4)) #compute the similarity
	end2 = int(time.time()*1000) #ending time
	print("\nRunning time for hash table query processing: ", (end2-start2))
#HT: return # of empty list and standard deviation of lengths of lists
def infolist(H):
	c=0
	m = H.num_items/len(H.item)
	k=0
	for a in H.item:
		k += (len(a)-m)*(len(a)-m)
		if a==[]: #[] found
			c+=1
	return c, math.sqrt(k*(1/(len(H.item))))
#HT:double the size of hashtable
def doubleSize(H):
	H2 = HashTableC(2*len(H.item)+1) #size = 2*length+1
	for a in H.item: #traverse table
		if a!=[]: #not empty
			for i in a: #traverse node since chaining
				H2.item[h(i[0], len(H2.item))].append([i[0], i[1]])
				H2.num_items+=1
	return H2
#HT: insert k in H
def InsertC(H,k):
	# Inserts k in appropriate bucket (list)
	# Does nothing if k is already in the table
	if H.num_items//len(H.item)==1: #recize table
		H = doubleSize(H)
	b = h(k[0],len(H.item)) #get the right index
	H.item[b].append([k[0], np.array(k[1:]).astype(np.float)])
	H.num_items+=1 #keep up with elements
	return H
#HT: return the index to insert
def h(s,n):
	r = 0
	t=0
	"""for p in s:
		t += (n*math.sin(math.radians(3.599999*(ord(p)-97))))
	return int(t//len(s))"""
	for c in s:
		r = (r*60 + ord(c))% n
	return r
#HT: find k and return array if found
def FindC(H,k):
    # Returns bucket (b) and index (i)
    # If k is not in table, i == -1
    b = h(k,len(H.item)) #get index
    for i in range(len(H.item[b])): #traverse the node
        if H.item[b][i][0] == k: #found
            return H.item[b][i][1] #return array
    return -1

#Build BST
def bst(f, f2):
	print("\nBuilding binary search tree.\n")
	T = None
	start = int(time.time()) #starting time
	for line in f: #get line by line
		data = line.split(' ') #array separated by ' '
		if data[0].isalpha():
			T = Insert(T, [data[0], np.array(data[1:]).astype(np.float)]) #insert word+embeddings
	end = int(time.time()) #ending time
	print("Binary Search Tree stats:")
	print("Number of nodes: ", count_nodes(T)) #num of nodes
	print("Height: ", find_height(T)) #num of height
	print("Running time for binary search tree construction:", (end-start))
	print("\nReading word file to determine similarities.\n")
	start = int(time.time()*1000) #starting time
	for line2 in f2: #word pairs
		data2 = line2.split(' ') #words pair separated by ','
		e0 = search_word(T, data2[0]) #search the 1st word, return array
		e1 = search_word(T, data2[1]) #search the 2nd word, return array
		print("Similarity", data2[1], " = ", round(np.sum(e0*e1)/(math.sqrt(np.sum(e0*e0))*math.sqrt(np.sum(e1*e1))),4)) #compute the similarity
	end = int(time.time()*1000) #ending time
	print("\nRunning time for binary search tree query processing: ", (end-start))
#BST: insert newitem into T
def Insert(T, newItem):
	if T == None:
		T =  BST(newItem)
	elif T.item[0] > newItem[0]:
		T.left = Insert(T.left, newItem)
	else:
		T.right = Insert(T.right, newItem)
	return T
#BST: find the height of a tree
def find_height(T):
	if T is not None: #base case
		return (1+max([(find_height(T.left)), find_height(T.right)])) #1 + (the higher number)
	else:
		return -1
#BST: count the number of nodes in T
def count_nodes(T):
	if T is not None:
		return 1 + count_nodes(T.left) + count_nodes(T.right)
	return 0
#BST: search a string in the tree T, return array if it was found, None otherwise
def search_word(T, k):
	temp = T #temporary variable for T
	while temp is not None: #iterate through necessary nodes
		if temp.item[0] == k: #found
			temp.item[1]
			return temp.item[1]
		elif temp.item[0] > k: #smaller
			temp = temp.left
		else: #larger
			temp = temp.right
	return None #not found


c = input("Type 1 for binary search tree or 2 for hush table with chaining\nChoice: ")
f = open('glove.6B.50d.txt',encoding='utf-8')  #file with vectors
f2 = open('similarityFile.txt', encoding='utf-8') #file with pairs
if c=='1': #binary search tree
	bst(f, f2)
elif c=='2': #hash table
	ht(f, f2)
f.close()
f2.close()
print()  