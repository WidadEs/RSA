import random


# Fonction pour calculer le PGCD (algorithme d'Euclide)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Fonction pour trouver l'inverse modulaire (algorithme d'Euclide étendu)
def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x

    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('L\'inverse modulaire n\'existe pas.')
    else:
        return x % phi


# Fonction pour générer des nombres premiers simples
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime(min_value, max_value):
    while True:
        p = random.randint(min_value, max_value)
        if is_prime(p):
            return p


# Générer les clés
def generate_keys():
    p = generate_prime(50, 100)
    q = generate_prime(50, 100)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)

    return (e, n), (d, n)  # Retourne (clé publique, clé privée)


# Fonction de chiffrement avec mélange
def encrypt(message, public_key):
    e, n = public_key
    r = random.randint(1, n - 1)  # Choisir un nombre aléatoire
    encrypted_message = [(pow(ord(char) + r, e, n), r) for char in message]
    return encrypted_message


# Fonction de déchiffrement avec mélange
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''

    for c, r in encrypted_message:
        m_prime = pow(c, d, n)  # Déchiffrer
        m = (m_prime - r) % n  # Retirer r
        decrypted_message += chr(m)  # Convertir en caractère

    return decrypted_message


# Exemple d'utilisation
public_key, private_key = generate_keys()
print(f"Clé publique: {public_key}")
print(f"Clé privée: {private_key}")

message = "Hello, everyone!"
encrypted_message = encrypt(message, public_key)
print(f"Message chiffré : {encrypted_message}")

decrypted_message = decrypt(encrypted_message, private_key)
print(f"Message déchiffré : {decrypted_message}")

message_3 = "1234!@#$"
encrypted_message_3 = encrypt(message_3, public_key)
print(f"Message chiffré : {encrypted_message_3}")

decrypted_message_3 = decrypt(encrypted_message_3, private_key)
print(f"Message déchiffré : {decrypted_message_3}")
