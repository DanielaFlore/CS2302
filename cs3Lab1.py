#Course:CS2302
#aAuthor:Daniela Flores
#Lab1
#Instructor:Olac Fuentes
#T.A: Dita Nath
#date of last Mod: 2/8/19
#purpose of program: in this program I had to write recursive methods that'll draw various shapes.
import matplotlib.pyplot as plt
import numpy as np
import math 
#the next two methods draw circles within the previous circle, the center is the radious
def circle(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles(ax,n,center,radius,w):
    if n>0:
        x,y = circle(center,radius)
        #here the radius is added to the center
        ax.plot(x+radius,y,color='k')
        draw_circles(ax,n-1,center,radius*w,w)
#call where 10 circles are drawn        
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 10, [100,0], 100,.6)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')

#call where 40 circles are drawn
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 40, [100,0], 100,.87)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')

#call where 62 circles are drawn
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles(ax, 62, [100,0], 100,.94)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('circles.png')
##########################################################################
#the following methods draw squares in the vertices of the larger square
def draw_squares(ax,n,p,r,c):
       if n>0:
           #i1 = [[c[0]+radius],2,3,0,1]
           newCor = np.array([ [c[0]+r,c[1]+r], [c[0]-r,c[1]+r],[c[0]-r,c[1]-r],[c[0]+r,c[1]-r],[c[0]+r,c[1]+r]])
           #                     0+25 , 0+25  //  0-25 , 0+25  // 0-25 , 0-25 // 0+25 , 0-25//   0+25, 0+25
           #                         (25,25)       (-25,25)        (-25,-25)       (25,-25)         (25,25)
           ax.plot(newCor[:,0],newCor[:,1],color = 'k')
           #with respect to center:
           newR = r//2
           newCenter =  [c[0]+r,c[1]+r]
           newCenter2 = [c[0]-r,c[1]+r] 
           newCenter3 = [c[0]-r,c[1]-r]
           newCenter4 = [c[0]+r,c[1]-r]
 
           draw_squares(ax,n-1,newCor,newR,newCenter)
           draw_squares(ax,n-1,newCor,newR,newCenter2)
           draw_squares(ax,n-1,newCor,newR,newCenter3)
           draw_squares(ax,n-1,newCor,newR,newCenter4)

#call where 2 sets of circles are drawn
plt.close("all") 
radius = 40
center = [0,0]
p = np.array([[-radius,-radius],[-radius,radius],[radius,radius],[radius,-radius],[-radius,-radius]])
fig, ax = plt.subplots()
draw_squares(ax,2,p,radius,center)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')
#call where 3 sets of squares are drawn
plt.close("all") 
radius = 40
center = [0,0]
p = np.array([[-radius,-radius],[-radius,radius],[radius,radius],[radius,-radius],[-radius,-radius]])
fig, ax = plt.subplots()
draw_squares(ax,3,p,radius,center)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')
#call where 4 sets of squares are drawn
plt.close("all") 
radius = 40
center = [0,0]
p = np.array([[-radius,-radius],[-radius,radius],[radius,radius],[radius,-radius],[-radius,-radius]])
fig, ax = plt.subplots()
draw_squares(ax,4,p,radius,center)
ax.set_aspect(1.0)
ax.axis('off')
plt.show()
fig.savefig('squares.png')
##############################################################################
#the following methods draw 5 smaller circles inside the bigger circle
def circle2(center,rad):
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_circles2(ax,n,center,Radius):
    if n>0:
        x,y = circle2(center,Radius)
        ax.plot(x,y,color='k')
        Radius = Radius/3
        newCenterL =np.array( [((1/3)*center[0]),0])

        x,y = circle2(newCenterL,Radius)
        ax.plot(x,y,color='r')
        
        newCenterM = np.array([center[0],0])

        x,y = circle2(newCenterM,Radius)
        ax.plot(x,y,color='m')
        newCenterR = np.array( [(((2/3)*center[0])+center[0]),0])

        x,y = circle2(newCenterR,Radius)
        ax.plot(x,y,color='c')
        newCenterUp =np.array( [center[0],((2/3)*center[0])])

        x,y = circle2(newCenterUp,Radius)
        ax.plot(x,y,color='b')
        newCenterDown =np.array( [center[0],((-2/3)*center[0])])
        x,y = circle2(newCenterDown,Radius)
        ax.plot(x,y,color='g')

        draw_circles2(ax,n-1,newCenterL,Radius)
        draw_circles2(ax,n-1,newCenterM,Radius)
        draw_circles2(ax,n-1,newCenterR,Radius)
        draw_circles2(ax,n-1,newCenterUp,Radius)
        draw_circles2(ax,n-1,newCenterDown,Radius)        
#here 2 sets of circles are drawn      
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles2(ax, 1, np.array([100,0]), 100)  
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')
#here 3 sets of circles are drawn        
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles2(ax, 2, np.array([100,0]), 100)  
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')
#4 sets of circles are drawn
plt.close("all") 
fig, ax = plt.subplots() 
draw_circles2(ax, 3, np.array([100,0]), 100)  
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('circles.png')
#####################################################################
#the following methods draw an upside down tree
def draw_triangle(ax,n,p,len,center):
    leftsubL = [-len,-len]
    rightsubL =[len,-len]
    treeAr = np.array([leftsubL,center,rightsubL])
    if n>0:

           
           LL = ((leftsubL[0]+leftsubL[0]//2),(leftsubL[0]+leftsubL[0]//2))

           
           newRightC = [(leftsubL[0]+leftsubL[1]//-2),(leftsubL[0]+leftsubL[0]//2)]
           new = np.array([leftsubL,LL,leftsubL,newRightC])
          
           ax.plot(new[:,0],new[:,1],color = 'k')

           newLeftR = [(rightsubL[0]-rightsubL[1]//-2),(rightsubL[0]-rightsubL[0]//-2)]

           newRightR = [(rightsubL[0]+rightsubL[0]//2),(rightsubL[0]+rightsubL[1]//2)]
           new2 = np.array([rightsubL,newLeftR,rightsubL,newRightR])
           # ax.plot(new2[:,0],new2[:,1],color = 'k')
           newLen = len+(len//3)
          
          
           draw_triangle(ax,n-1,treeAr,newLen,leftsubL)
           draw_triangle(ax,n-1,treeAr,newLen,rightsubL)
           
#here 2 branches are drawn
plt.close("all") 
length = 25
center = [0,0]
p = np.array([[-length,-length],[center[0],center[1]],[length,-length]])
fig, ax = plt.subplots()
draw_triangle(ax,2,p,length,center)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')
#here three branches are drawn
plt.close("all") 
length = 25
center = [0,0]
fig, ax = plt.subplots()
draw_triangle(ax,3,p,length,center)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')
#here 4 sets of branches are drawn
plt.close("all") 
length = 25
center = [0,0]
fig, ax = plt.subplots()
draw_triangle(ax,4,p,length,center)
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('squares.png')
