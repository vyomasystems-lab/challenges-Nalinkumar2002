from math import sqrt
import random
from random import randint as rand

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

p = 7
q = 13

def generate_keypair(p, q):

    print(p, q)
    n = p * q
    phi = (p - 1) * (q - 1)

    e=2
    while (e < phi):
        if(gcd(e, phi) == 1):
            break
        else:
            e = e+1
    while True:
        g = gcd(e, phi)
        d = mod_inverse(e, phi)
        if g == 1 and e != d:
            break

    #public key (e,n)
    #private key (d,n)

    return ((e, n), (d, n), phi)


def encrypt(msg_plaintext, package):
    e, n = package
    print(e,n,msg_plaintext)
    msg_ciphertext = pow(msg_plaintext, e, n)
    
    return msg_ciphertext

def decrypt(msg_ciphertext, package):
    d, n = package
    msg_plaintext = pow(msg_ciphertext, d, n)
    return (msg_plaintext)

#if __name__ == "__main__":
def model_rsa(msg,p,q):
    n=p*q
    print("Key Generation....")
    public, private, phi = generate_keypair( p, q)
    print("Public Key: ", public)
    print("Private Key: ", private)
    encrypted_msg = encrypt(msg, public)
    print("Encrypted msg: ")
    print(encrypted_msg)
    print("Decrypted msg: ")
    print(decrypt(encrypted_msg, private))
