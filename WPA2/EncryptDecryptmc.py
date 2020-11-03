import AESmc
import AESmcInverse

if __name__ == "__main__":
    unencrypted_vector = [0xdb, 0x13, 0x53, 0x45]

    encrypted_vector = AESmc.algo(unencrypted_vector)
    decrypted_vector = AESmcInverse.algo(encrypted_vector)

    print(unencrypted_vector)
    print(encrypted_vector)
    print(decrypted_vector)