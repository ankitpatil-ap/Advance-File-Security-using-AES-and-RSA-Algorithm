# Advance-File-Security-using-AES-and-RSA-Algorithm
Django Web App using AES and RSA Algorithm on which you encrypt or decrypt single/multiple files with advance level of encryption and security.

Read Steps file and then run the project.

Two Algorithms are used here for file encryption and decryption are as follows 

1) Advanced Encryption Standard (AES) is a specification for the encryption of electronic data established by the U.S National Institute of Standards and Technology (NIST) in 2001. AES is widely used today as it is a much stronger than DES and triple DES despite being harder to implement.
Points to remember
AES is a block cipher.
The key size can be 128/192/256 bits.
Encrypts data in blocks of 128 bits each.
That means it takes 128 bits as input and outputs 128 bits of encrypted cipher text as output. AES relies on substitution-permutation network principle which means it is performed using a series of linked operations which involves replacing and shuffling of the input data.
Working of the cipher:
AES performs operations on bytes of data rather than in bits. Since the block size is 128 bits, the cipher processes 128 bits (or 16 bytes) of the input data at a time.
The number of rounds depends on the key length as follows:
128 bits key – 10 rounds
192 bits key – 12 rounds
256 bits key – 14 rounds



2) RSA algorithm is asymmetric cryptography algorithm. Asymmetric actually means that it works on two different keys i.e. Public Key and Private Key. As the name describes that the Public Key is given to everyone and Private key is kept private.
An example of asymmetric cryptography :
1.	A client (for example browser) sends its public key to the server and requests for some data.
2.	The server encrypts the data using client’s public key and sends the encrypted data.
3.	Client receives this data and decrypts it.
Since this is asymmetric, nobody else except browser can decrypt the data even if a third party has public key of browser.
The idea! The idea of RSA is based on the fact that it is difficult to factorize a large integer. The public key consists of two numbers where one number is multiplication of two large prime numbers. And private key is also derived from the same two prime numbers. So, if somebody can factorize the large number, the private key is compromised. Therefore, encryption strength totally lies on the key size and if we double or triple the key size, the strength of encryption increases exponentially. RSA keys can be typically 1024 or 2048 bits long, but experts believe that 1024 bit keys could be broken in the near future. But till now it seems to be an infeasible task.



Applications: -

•	Through encryption, AFS helps keep sensitive files safe from hackers or data thieves who gain unauthorized access to a computing network or devices.
•	Commercial Companies which need to deal with third party companies for project contracts need a system where data cannot be steeled or modified.
•	To Share files among trusted clients over any social network where hackers cannot decrypt the file.


Screenshots of Project:


![2022-07-12 (8)](https://user-images.githubusercontent.com/63675385/178553537-92a29bb7-ec44-487c-a0e2-69320cee9e4a.png)
![2022-07-12 (9)](https://user-images.githubusercontent.com/63675385/178553548-2f4432da-b7d2-4794-9413-783338ffb898.png)
![2022-07-12 (10)](https://user-images.githubusercontent.com/63675385/178553551-c52c96c5-d424-4b2d-a3e8-300f216f2e50.png)
![2022-07-12 (11)](https://user-images.githubusercontent.com/63675385/178553560-7e7baf81-2947-4365-b87c-2516468f48b5.png)
![2022-07-12 (12)](https://user-images.githubusercontent.com/63675385/178553564-1e85e3b9-0976-45b1-a96a-699f2b30d7e6.png)
![2022-07-12 (13)](https://user-images.githubusercontent.com/63675385/178553566-4a90387f-15fb-47d3-8645-3fd99fc8c767.png)
![2022-07-12 (14)](https://user-images.githubusercontent.com/63675385/178553571-d578c17a-7435-4659-a66d-820700e0ce98.png)

