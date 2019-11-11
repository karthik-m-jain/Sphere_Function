# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:24:03 2019

@author: admin
"""

from matplotlib import pyplot as plt
import Prob_Roulette_wheel as P_R
from Prob_Roulette_wheel import *
import Input
from Input import red_f
from Func import line,n_cand

new_ub=5.12
new_lb=-5.12
x_axis=[]
ub_axis=[]
lb_axis=[]
updated_list=[] 
l2=[] 
l3=[]
c=0
flag=0
while c<1000 and flag==0:
    f_c=[]
    matrix=[]
    c_matrix=[]
    temp_r=new_ub-new_lb
    new_r=temp_r*red_f
    new_ub=new_r/2                          #Find new upper bound
    new_lb=-new_r/2                         #Find new lower bound 
    
    if c==0:
        Input.accept(matrix)
        P_R.prob_rw(c_matrix,matrix,f_c)
        updated_list=P_R.New_range(c_matrix,updated_list,new_r,new_ub,new_lb)
    else:
        Input.Random_accept(matrix,updated_list)
        P_R.prob_rw(c_matrix,matrix,f_c)
        updated_list=P_R.New_range(c_matrix,updated_list,new_r,new_ub,new_lb)
        
    for i in range(n_cand):
       if f_c[i]<=(1e-16):
           if i==(n_cand-1):
               flag=1        
               break
    c=c+1   
    x_axis.append(c)
    ub_axis.append(new_ub)
    lb_axis.append(new_lb)
    l2.append(updated_list[0][0][0])     #Lower Bound of n_cand=0 n_var=0 
    l3.append(updated_list[0][0][1])     #Upper Bound of n_cand=0 n_var=0
  
print("Iterations:",c)
    
plt.plot(x_axis,ub_axis)
plt.plot(x_axis,lb_axis) 

print("\nGlobal Upper_Bound,Lower_Bound v/s Iteration")
plt.show() 

print("\nFunction_Values v/s iteration")
for i in range(n_cand):
    plt.plot(x_axis,line[i])
plt.show()

print("\nLB,UB of Candidate-1 and Variable-1 v/s Iteration")
plt.plot(x_axis,l2)
plt.plot(x_axis,l3)
plt.show()

