import sympy

def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)

    # Choose a private exponent d
    d = sympy.randprime(2, phi)

    # Calculate the public exponent e such that it is coprime with phi
    e = sympy.mod_inverse(d, phi)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key

def sign(message, private_key):
    n, d = private_key
    signature = pow(message, d, n)
    return signature

def verify(message, signature, public_key):
    n, e = public_key
    decrypted_signature = pow(signature, e, n)
    return decrypted_signature == message

def main():
    # Input prime numbers p and q
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))

    public_key, private_key = generate_keypair(p, q)

    message = int(input("Enter a message to sign: "))

    # Signing
    signature = sign(message, private_key)
    print("Signature:", signature)

    # Verification
    is_verified = verify(message, signature, public_key)
    if is_verified:
        print("Signature is verified.")
    else:
        print("Signature verification failed.")

if __name__ == "__main__":
    main()
