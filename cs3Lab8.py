#Course:CS2302
#aAuthor:Daniela Flores
#Lab8
#Instructor:Olac Fuentes
#T.A: Dita Nath
#date of last Mod: 5/11/19
#purpose of program: Discover Trig identities with the help of randomized algorithms. We also
#had to check if a partition exists in a set of numbers with the aid of backtracking.
import random
import numpy as np
from math import *
import math
#this method checks if the two given trig expressions are equal
def isEqual(f1, f2,tries=1000,tolerance=0.0001):
    #checks if theyre equal 1000 different times
    for i in range(tries):
        t = random.uniform(-(math.pi), math.pi)
        #evaluates the two expressions
        e1 = eval(f1)
        e2 = eval(f2)
        #if the solutions of both expressions are not equal,return false
        if np.abs(e1-e2)>tolerance:
            return False
    return True
#method that compares every trig expresion to each other
def comparing(L):
    #count keeps track of trig identites found
    count = 0
    #traverses through whole list containing the expressions
    for i in range(len(L)):
        for j in range(i,len(L)):
            if(isEqual(L[i],L[j])):
                count=count+1
                print(count)
                print(L[i],L[j])
                
#method that computes subset if there is one
def subsetSum(S,last,goal):
    if goal == 0:
        return True, []
    if goal<0 or last<0:
        return False, []
    res, subset = subsetSum(S,last-1,goal-S[last]) 
    if res:
        subset.append(S[last])
        return True, subset
    else:
        return subsetSum(S,last-1,goal) 
#method that computes if the given set's total is even or odd
def partition(S):
    if sum(S)%2 != 0:
        return False
    goal = sum(S)//2
    return goal

#list of all trig identities
L = ['sin(t)','cos(t)','tan(t)','1/cos(t)','-sin(t)','-cos(t)','-tan(t)','sin(-t)','cos(-t)',
     'tan(-t)','sin(t)/cos(t)','2*sin(t/2)*2*cos(t/2)','sin(t)**2','sin(t)**2','1-cos(t)**2',
     '(1-cos(2*t))/2','1/cos(t)']
print('similarities found:')
comparing(L)
print()
print('partition w/ backtracking:')
S = [2, 4, 5, 9, 12]
#stores partition of subset
Par = partition(S)
boo, s1= subsetSum(S,len(S)-1,Par)
if Par:
    s2 = []
    print('subset One',s1)
    for j in S:
        if j not in s1:
            s2.append(j)
    print('subset Two',s2)
else:
    print('no partition exits for this set')

