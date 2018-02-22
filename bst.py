"""
@author : Pratik kulkarni
Binary search tree with following features:
-Insertion
-Inorder traversal and printing
-Depth/Height of a tree
-Search and return height of a particular node

"""
####################################################
from random import *

"""INPUT SEQUENCE 1"""
input1 = list()
for i in range (500):
    input1.append(randint(1, 100))

"""INPUT SEQUENCE 2"""
input2 = list()
for i in range(1,100):
    if i%2!=0:
        input2.append(i)
for i in range(1,100):
    if i%2==0:
        input2.append(i)
for i in range(401):
    input2.append(randrange(1,100))


"""Class for a node"""
class BSTnode:

    def __init__(self,keyval):
        self.leftchild = None
        self.keyval = keyval
        self.rightchild = None
        self.count = 1


"""Class for a tree"""
class BST:

    def __init__(self):
        self.rootelement = None

    def insertelement(self,keyval):
        global keycomp
        keycomp = 1
        if self.rootelement==None:                 #check if root exists node exists
            self.rootelement = BSTnode(keyval)
        else:
            global currentel
            currentel = self.rootelement
            while 1:
                if keyval==currentel.keyval:
                    currentel.count +=1
                    keycomp = currentel.count
                    break;
                elif keyval < currentel.keyval:    #check if node to be inserted is less than root
                    if currentel.leftchild:    #if left child present update the currentel
                        currentel = currentel.leftchild   #create a node with that key value
                    else:
                        currentel.leftchild = BSTnode(keyval) #create a new node
                        break;
                elif keyval > currentel.keyval:
                    if currentel.rightchild: #if
                        currentel = currentel.rightchild
                    else:
                        currentel.rightchild = BSTnode(keyval)

                        break;



    def iorder(self,node):
        if node != None:
            self.iorder(node.leftchild)
            print node.keyval
            self.iorder(node.rightchild)
"""End of class"""

##################################################################
"""Search for a key"""

"""returns: The height of that element multiplied by the count"""

def search(node,keyval,counter):

    if node==None:                 #check if root exists node exists
        return 0
    else:

        counter = counter+1         #COUNTER DENOTES HEIGHT OF THAT ROOT
        if keyval == node.keyval:
            global freq             #DENOTES NO OF TIMES THE ELEMENT WAS INSERTED
            freq = node.count
            #print "COUNT of 10 IS:" , cnt
            return counter * freq
        elif keyval<node.keyval:
            return search(node.leftchild,keyval,counter)
        elif keyval>node.keyval:
            return search(node.rightchild,keyval,counter)

def depth(node):
    if node==None:
        return 0
    else:
        leftD = depth(node.leftchild)
        rightD = depth(node.rightchild)
        if (leftD > rightD):
            return leftD+1
        else:
            return rightD+1

###################################################
obj1 = BST()
testarr = [10,10,20,20,1,15,17,40,50,60]

print "---A Binary Search Tree----"

for i in input1:
    obj1.insertelement(i)

print "Elements Inserted for: INPUT SEQUENCE 1"

avg=0.0
for i in range(1,100):
    a = search(obj1.rootelement,i,0)
    avg = avg +a
avg = avg/500

print "Average key comparisons:", avg

##################################################
#Uncomment this to print the elements inorder
# print "Inorder is :"
# obj1.iorder(obj1.rootelement)

##################################################
print "Height of tree " ,(depth(obj1.rootelement))
##################################################
