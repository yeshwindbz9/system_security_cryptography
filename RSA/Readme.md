# Implementation and analysis of RSA cryptosystem and Digital signature scheme using RSA.

RSA (Rivest–Shamir–Adleman) is one of the first public-key cryptosystems and is widely used for secure data transmission. In such a cryptosystem, the encryption key is public and distinct from the decryption key which is kept secret (private).

In RSA, this asymmetry is based on the practical difficulty of factoring the product of two large prime numbers, the "factoring problem". The acronym RSA is the initial letters of the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman, who publicly described the algorithm in 1977.

A user of RSA creates and then publishes a public key based on two large prime numbers, along with an auxiliary value. The prime numbers must be kept secret. Anyone can use the public key to encrypt a message, but only someone with knowledge of the prime numbers can decode the message.

RSA Algorithm


•	Step-1: Choose two prime number p and q

•	Step-2: Compute n and phi(n)

•	Step-3: If not given find public key e such that 1<=e<=n

•	Step-4: Compute private key d for the given public key e

•	Step-5: Perform encryption or decryption

RSA CRYPTOSYSTEM

Encryption: C = Me mod n

Decryption: M = Cd mod n

Where (e, d) are senders public and recievers private keys respectively.


RSA DIGITAL SIGNATURE

Encryption: C = Md mod n

Decryption: M = Ce mod n

Where (e, d) are senders public and private keys
