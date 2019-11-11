# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:25:20 2019

@author: admin
"""
import Input
from Input import n_cand,n_var,red_f
upper_b=5.12            #upper bound of sphere
lower_b=-5.12           #Lower bound of sphere

#List of function output for each candidate
line=[]

for i in range(n_cand):
    line.append([])

def Calculate(x,f_c):
      
    for i in range(n_cand):
        sum=0
        for j in range(n_var):          #Function evaluation
            sum=sum+(x[i][j]**2)
        f_c.append(sum)
        line[i].append(sum)
        
    print("The sum is",end=" ")   
    for i in range(n_cand):
        print(f_c[i],end=" ")           #Display the list
        
    return f_c




    
    
    
            