# For varying message sizes, analyse the performance of the two protocols - MD-5 and SHA-1. Use crypt APIs.

The MD5 and SHA1 are the hashing algorithms where MD5 is better than SHA in terms of speed. However, SHA1 is more secure as compared to MD5. The concept behind these hashing algorithms is that these are used to generate a unique digital fingerprint of data or message which is known as a hash or digest.

The essential features of hash algorithms are:

•	These functions cannot be reversed.

•	Size of the digest or hash is always fixed and does not depend on the size of the data.

•	It is always unique, no two distinct data set are able to produce a similar hash.

Hash algorithm primary purpose is the verification of the files instead of encryption of the file or message. I should not be used for storing the information or securing it.

The crucial difference between MD5 and SHA1 is that MD5 was priorly developed and had several vulnerabilities where one can create the collisions for message digest. On the other hand, SHA1 brought a lot of improvement in hashing and is better than MD5. Although, there are still some issues in SHA1 which got resolved in SHA 256 and SHA 512.

Md5 is supposed to be faster than Sha1 but due to repeated optimizations and updates made to the more frequently used Sha1 libraries it is much faster when compared to the old Md5.
