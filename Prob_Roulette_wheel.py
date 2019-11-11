# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:30:04 2019

@author: admin
"""
from Func import n_cand,n_var,upper_b,lower_b
import Func
import random

def prob_rw(c_matrix,matrix,f_c):
    x=Func.Calculate(matrix,f_c);         #Call calculate function
    Prob_cand=[]                #List of probablity outcome of each candidate
    sum_all=0
    for i in range(n_cand):
        sum_all=sum_all + (1/x[i])              #Sum of all candidates
    for i in range(n_cand):
        Prob_cand.append((1/x[i])/sum_all)      #Calculate maxima for each candidate
    print("\nThe Probability is:",end=" ")    
    for i in range(n_cand):
       print(Prob_cand[i],end=" ")      
       
    #Roulette wheel
    r_v=[]
    sum2=0
    print()
    for i in range(n_cand):
        r_v.append(random.random())             #Generate random values for each candidate
        sum2=sum2+Prob_cand[i]                  #Roulette wheel
        Prob_cand[i]=sum2                       #Redefine the probability list
        
    print("\nRoulette Wheel values")
    for i in range(n_cand):
       print(Prob_cand[i],end=" ") 
        
    print("\nRandom Numbers")
    for i in range(n_cand):
        print(r_v[i])
       
    print("\n")
    for l in range(n_cand):
        for m in range(n_cand):
            if r_v[l]<Prob_cand[m]:             #Compare random values with generated roulette wheel 
                print(l,"follows",m)            #Determine the pattern
                c_matrix.append(matrix[m])
                break
            
    print("\nNew Matrix")      
    for i in range(n_cand):
        for j in range(n_var):
            print(c_matrix[i][j],end=" ")
        print()

def New_range(c_matrix,updated_list,new_r,new_ub,new_lb):                       #Use the new range and determine the updated matrix  
    updated_list=[]
    print("\n New Range:",new_r)
    print("\nNew upper bound:",new_ub, "and lower bound:",new_lb)
    
    for i in range(n_cand):
        cand_list=[]
        for j in range(n_var):
            bound_l=[]
            upd_lb=c_matrix[i][j]+new_lb                #Adding the new bounds
            upd_ub=c_matrix[i][j]+new_ub
            
            if upd_lb<new_lb:                          #Checking the bounds after adding
                bound_l.append(new_lb)
            else:
                bound_l.append(upd_lb)
            if upd_ub>new_ub:
                bound_l.append(new_ub)
            else:
                bound_l.append(upd_ub)
            cand_list.append(bound_l)
        updated_list.append(cand_list)
           
    for i in range(n_cand):
        for j in range(n_var):
            for k in range(2):
                print(updated_list[i][j][k],end=" ")
                
            print("\t",end=" ")
        print()
            
    return updated_list
            
            
                  
        
            
                
                
                
            
            
    
      
        
    