# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 19:43:24 2020
@author: yeshw
"""
import string
import math
import time
print('-'*40)
print('Product Cipher Using Substitution and Transposition')
#input the plain text
msg  = input('ENTER MESSAGE TO ENCRYPT -> ')
#input key for substitution
keySub = int(input('ENTER INT KEY FOR SUBSTITUTION -> '))
#input key for permutation
keyPer = input('ENTER STRING KEY FOR PERMUTATION -> ')
#substitutionBox function
def sbox(msg,keySub):
    #creating dictionary of alphabets
    all_letters= string.ascii_letters
    dictSub = {} #dictionary acts as a substitution element
    for i in range(len(all_letters)): 
        dictSub[all_letters[i]] = all_letters[(i+keySub)%len(all_letters)]
    cipherLst = [] #empty list for generated cipher
    for char in msg:
        if char in all_letters:
            temp = dictSub[char] #substitute char for the element from dict
            cipherLst.append(temp)
        else:
            cipherLst.append(char)# append whitespace
    return ''.join(cipherLst)
#permutationBox encrypt function
def pboxEncrypt(msg,keyPer):
    cipher = ''
    k_index = 0 #to track key indices
    msg_len = float(len(msg))
    msg_lst = list(msg) #converting msg to list
    key_lst = sorted(list(keyPer)) #sorted list of key chars
    col = len(keyPer) #column of matrix
    row = int(math.ceil(msg_len/col)) # row of matrix
    fill_null = int((row*col)-msg_len) #adds padding char _ in empty cell
    msg_lst.extend('_'*fill_null)
    #create matrix and insert message and padding row-wise
    matrix = [msg_lst[i:i+col] for i in range(0,len(msg_lst),col)]
    #create cipher text by reading col-wise and permutation k
    for _ in range(col): #permutation encrpytion
        curr_index = keyPer.index(key_lst[k_index])
        cipher += ''.join([row[curr_index] for row in matrix])
        k_index += 1
    return cipher
#permutationBox decrypt function
def pboxDecrypt(cipher,keyPer):
    msg = ''
    k_index = 0 #to track key indices
    msg_index = 0 #to track msg index
    msg_len = float(len(cipher))
    msg_lst = list(cipher) #converting msg to list
    key_lst = sorted(list(keyPer)) #sorted list of key chars
    col = len(keyPer) #column of matrix
    row = int(math.ceil(msg_len/col)) # row of matrix
    dec_cipher = [] #empty list to store deciphered message
    for _ in range(row): #creates the structure of the msg_lst
        dec_cipher += [[None]*col]
    #arrange matrix column wise to permutation order
    for _ in range(col):
        curr_index = keyPer.index(key_lst[k_index])
        for j in range(row):
            dec_cipher[j][curr_index] = msg_lst[msg_index]
            msg_index += 1
        k_index += 1
    msg = ''.join(sum(dec_cipher, []))
    null_count = msg.count('_')
    if null_count > 0:
        return msg[:- null_count]
    else:
        return msg
print('-'*50)
time.sleep(1)#encrypting
print('ENCRYPTION')
encipherOne = sbox(msg,keySub)
print('CIPHERTEXT FROM SUBSTITUTION -> ',encipherOne)
encipherTwo = pboxEncrypt(encipherOne,keyPer)
print('CIPHERTEXT FROM TRANSPOSITION -> ',encipherTwo)
print('-'*50)
print('FINAL CIPHER TEXT FROM PRODUCT CIPHER -> ',encipherTwo)
time.sleep(1)#decryption
print('DECRYPTION')
decipherTwo = pboxDecrypt(encipherTwo,keyPer)
print('DECIPHERED TEXT FROM TRANSPOSITION -> ',decipherTwo)
decipherOne = sbox(decipherTwo,-keySub)
print('DECIPHERED TEXT FROM SUBSTITUTION -> ',decipherOne)
print('-'*50)