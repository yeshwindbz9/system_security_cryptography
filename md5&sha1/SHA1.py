# importing the hashlib module
import hashlib
import time
t1 = time.time()
def gen_hash(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""
   
   # make a hash object
   h = hashlib.sha1()
   
   # open file for reading in binary mode
   with open(filename,'rb') as file:
       # loop till the end of the file
       chunk = 0       
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)
           
   # return the hex representation of digest
   return h.hexdigest()


# Input the same file as MD5 and analyze on the hash size and
# time required (speed) for MD5 & SHA1

message = gen_hash("galax.txt")
t2 = time.time()

print("Length of Hash code SHA1 in bits = ", len(message) * 4)
print("Digest = ", message, " Time required = ", t2-t1)
