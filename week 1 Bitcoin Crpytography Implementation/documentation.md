WEEK 1 WEB-3

1.Transaction_Hasher

1. used hashlib library for sha256 hashing.
2. taking hash string and it should of even length and we have to convert it to raw bytes format as hashlib library takes raw bytes.
3. double hashing the transaction hex and reversing it as bitcoin or ECDA use big endian (taking from the last ) usually.  
4. now converting it to hexadecimal format from raw byte format and we got out our TXID (Transaction ID).
-----

2.Signature Simulator

1. using hashlib, secrets , ecdsa library of python
2. a inversre mod function for returning inverse of k (k is a random no between 1 to order-1 and order is subgroup of points in elleptic curve. yah, little bit confusing).
3. now come to main signing transaction function which takes transaction hex in bytes format and user private key to sign the transaction
3. hashing transaction firstly and then taking its integer format in z in big endian format 
4. calculating k which is any random no between 1 to order-1 and this is also called nounce 
5. now calculating R and taking its x component for calculation of r 
6. now the calculation of s is done using the complex formula of ecdsa.
7. we can get public key by multiplying private key with genrator and converting there x and y coordinate to hexadecimal format by merging them . 
8. now we have got our r, s , public key in hexadecimal format 
9. all the formulas and variables are refered from https://cryptobook.nakov.com/digital-signatures/ecdsa-sign-verify-messages#ecdsa-sign

----

3.Signature Verifier

1. now we have to verify that siganture that it is real or not so for that we need transaction in raw bytes and signature and the public key and return a bool value either it is real or not.
2. importing libraries required and defining the curve which is used by us or given by ecdsa , generator , and order of G .
3. destructuring signature to get r,s and checking for there condition of greator than 1 and smaller than order n and s should be greator than halve of order.
4. now we have to recover x and y from public key so converting them to integer vai big endian format and calculating point P which is a public key.
5. now converting transaction hash into integer as ecdsa formula needs integer and calculating required things which is written in https://cryptobook.nakov.com/digital-signatures/ecdsa-sign-verify-messages#ecdsa-sign
6. now comparing the formula and if (R.x() % n) == r is true then the transaction is valid else not a valid transaction.

----

<img width="1132" alt="shapes at 25-05-19 20 40 34" src="https://github.com/user-attachments/assets/790685e1-0a60-496f-ba7f-958abe83d227" />


