#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 11:25:55 2022

@author: arjun
"""

import pennylane as qml
from pennylane import numpy as np

message=input('Type your message: ')
message_array=np.array([])
for i in message:
    message_array = np.append(message_array, bin(ord(i))[2:])
#%%
Answer=''


for i in message_array:
    i=str(i)
    dev=qml.device('default.qubit',wires=len(i)+1)
    @qml.qnode(dev)
    def BV_solver(a):
        for i in range(len(a)):
            qml.Hadamard(wires=i)
        qml.PauliX(wires=len(a))
        qml.Hadamard(wires=len(a))
        for j in range(len(a)):
            if int(a[j]):
                qml.CNOT(wires=[j,len(a)]) #Unitary operator corresponding to classical BV oracle function
        for k in range(len(a)):    
            qml.Hadamard(wires=k)
        qml.PauliZ(wires=len(a))
        qml.Hadamard(wires=len(a))
        return qml.state()
    a_cracked=bin(np.argmax(BV_solver(i)))[2:-1]
    while len(a_cracked) != len(i):
        a_cracked = '0' + a_cracked
    Answer = Answer + chr(int(a_cracked,2))
print('Hidden message: %s'%Answer)            
        
    
    
    