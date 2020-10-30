import numpy as np
import random

def KSA(key,iv = None):
    if iv is None:
        iv = []
        for i in range(3):
            iv.append(random.randint(0,255))
    key_packet = iv + key
    key_length = len(key_packet)
    S = list(range(256))
    j = 0
    T = [0] * 256
    for i in range(256):
        T[i] = key_packet[i % key_length]
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap the entries
    return S,iv

def PRGA(S, message):
    i = 0
    j = 0
    key = []
    n = len(message)

    while n > 0:  # With n the length of the message coded in ASCII)
        n = n - 1
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        key.append(K)
    np.array(key)
    return key

def text_to_asc(text):
    return [ord(c) for c in text]
