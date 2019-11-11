# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:23:36 2019

@author: admin
"""
#Number of candidates
import random
n_cand=int(input("Number of candidates:"))

#Number of variables
n_var=int(input("Number of variables:"))

#Reduction factor
red_f=float(input("Reduction factor:"))

#Accept function to accept data from user

def accept(matrix):
    for i in range(n_cand):
        a=[]
        for j in range(n_var):
            val=random.uniform(-5.12,5.12)
            a.append(val)   
        matrix.append(a)
           
    for i in range(n_cand):                     #Display the input matrix
        for j in range(n_var):
            print(matrix[i][j],end=" ")
        print()

    return matrix

def Random_accept(matrix,updated_list):
    for i in range(n_cand):
        a=[]
        for j in range(n_var):
            val=random.uniform(updated_list[i][j][0],updated_list[i][j][1])
            a.append(val)
        matrix.append(a)
        
    return matrix
    

