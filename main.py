import turtle #The turtle package helps to draw objects on our python window
from turtle import * #the import * means import everything in the package
import random


setup(width=600,height=700)

colorlist=["red","green","orange","yellow","blue"]
speed=60 #Speed is how fast the turtle will move 0 is fastest
pensize=2 #This is for how thin the pen will be

for i in range(200): #we use this for loops so in this case it will repeat this loop 200 times
    circle(150) #150 circles, not exactly 150 but we will do 150*200=300,000 circles(approximately)
    color(colorlist[i%5]) #Colors will be inputted
    left(53) #dataframe object
    
    
