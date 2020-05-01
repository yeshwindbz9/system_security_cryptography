# Implementation of Diffie Hellman Key exchange algorithm.
Asymmetric Encryption of data requires transfer of cryptographic private key. The most challenging part in this type of encryption is the transfer of the encryption key from sender to receiver without anyone intercepting this key in between. This transfer or rather generation on same cryptographic keys at both sides secretively was made possible by the Diffie-Hellman algorithm.

The Diffie-Hellman algorithm was developed by Whitfield Diffie and Martin Hellman in 1976. This algorithm was devices not to encrypt the data but to generate same private cryptographic key at both ends so that there is no need to transfer this key from one communication end to another. Though this algorithm is a bit slow but it is the sheer power of this algorithm that makes it so popular in encryption key generation. The algorithm is given below for three parties : 
1.	The parties agree on the algorithm parameters p and g.
2.	The parties generate their private keys, named a, b, and c.
3.	Alice computes g^a and sends it to Bob.
4.	Bob computes (g^a)^b = g^ab and sends it to Carol.
5.	Carol computes (g^ab)^c = g^abc and uses it as her secret.
6.	Bob computes g^b and sends it to Carol.
7.	Carol computes (g^b)^c = g^bc and sends it to Alice.
8.	Alice computes (g^bc)^a = g^bca = g^abc and uses it as her secret.
9.	Carol computes g^c and sends it to Alice.
10.	Alice computes (g^c)^a = g^ca and sends it to Bob.
11.	Bob computes (g^ca)^b = g^cab = g^abc and uses it as his secret.
An eavesdropper has been able to see g^a, g^b, g^c, g^ab, g^ac, and g^bc, but cannot use any combination of these to efficiently reproduce gabc.
