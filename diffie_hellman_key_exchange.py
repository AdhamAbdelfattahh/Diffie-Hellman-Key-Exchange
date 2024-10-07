import random

def generate_private_key(prime):
    """Generate a private key."""
    return random.randint(1, prime - 1)

def generate_public_key(private_key, base, prime):
    """Generate a public key."""
    return pow(base, private_key, prime)

def generate_shared_secret(public_key, private_key, prime):
    """Generate a shared secret."""
    return pow(public_key, private_key, prime)

def main():
    # Larger prime number and a suitable base
    prime = 23  # A prime number
    base = 5    # A primitive root modulo 23

    # Alice generates her private and public keys
    alice_private = generate_private_key(prime)
    alice_public = generate_public_key(alice_private, base, prime)

    # Bob generates his private and public keys
    bob_private = generate_private_key(prime)
    bob_public = generate_public_key(bob_private, base, prime)

    # Exchange public keys and generate the shared secret
    alice_shared_secret = generate_shared_secret(bob_public, alice_private, prime)
    bob_shared_secret = generate_shared_secret(alice_public, bob_private, prime)

    # Display results
    print(f"Alice's Private Key: {alice_private}")
    print(f"Alice's Public Key: {alice_public}")
    print(f"Bob's Private Key: {bob_private}")
    print(f"Bob's Public Key: {bob_public}")
    print(f"Alice's Shared Secret: {alice_shared_secret}")
    print(f"Bob's Shared Secret: {bob_shared_secret}")

if __name__ == "__main__":
    main()
