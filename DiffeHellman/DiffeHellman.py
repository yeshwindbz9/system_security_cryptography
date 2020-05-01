# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:42:43 2020
@author: yeshw
"""
#Diffie Hellman Key exchange algorithm
print('-'*40)
print('Diffie Hellman Key exchange algorithm')
#initially select a very large prime P
P = int(input('ENTER A VERY LARGE PRIME P -> '))
#take a primitive root of P as G
G = int(input('ENTER PRIMITIVE ROOT OF P, G -> '))
#Both sender and reciever agree upon public values of P,G
#input private key for A
x = int(input('ENTER PRIVATE KEY OF A -> '))
#calculate public key R1
R1 =( G ** x) % P #A sends R1 to B
#input private key for B
y = int(input('ENTER PRIVATE KEY OF B -> '))
#calculate public key R2
R2 =( G ** y) % P #B sends R2 to A
#finally calculate secret key K
a = (R2 ** x) % P #for user A
b = (R1 ** y) % P #for user B
K = (G ** (x*y)) % P #secret key
if a == b == K:
    print('\nSECRET KEY SHARED BETWEEN A and B, K-> ',K)
print('-'*40)