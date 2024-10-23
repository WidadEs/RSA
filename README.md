# The Encryption/Decryption Algorithm Inspired by RSA
## **1. Génération des clés**
- Choisir deux grands nombres premiers **p** et **q**.
- Calculer **𝑛 = 𝑝 × 𝑞** (utilisé dans la clé publique et la clé privée).
- Calculer **𝜙(𝑛) = (𝑝−1) × (𝑞−1)**.
- Choisir un entier **𝑒** tel que **1 < 𝑒 < 𝜙(𝑛)** et **gcd(𝑒, 𝜙(𝑛)) = 1**.
- Calculer **𝑑** comme l'inverse modulaire de **𝑒** modulo **𝜙(𝑛)** : **𝑑 × 𝑒 ≡ 1 (mod 𝜙(𝑛))**.

## **2. Chiffrement**
Pour un message :
- Représenter le message sous forme numérique (par exemple, ASCII).
- Chiffrer chaque caractère du message avec la clé publique : **𝑐 = 𝑚^𝑒 (mod 𝑛)**.
- Le résultat **𝑐** est le message chiffré.

## **3. Déchiffrement**
Pour déchiffrer un message chiffré **𝑐** :
- Utiliser la clé privée pour récupérer le message : **𝑚 = 𝑐^𝑑 (mod 𝑛)**.
- Convertir le résultat numérique en caractères pour retrouver le message original.

## **4. Modification : Ajout d'une Phase de Mixage**
Pour renforcer la sécurité, nous allons introduire une phase de mixage qui mélangera les résultats avant le chiffrement et après le déchiffrement. Cela se fera en ajoutant un nombre aléatoire **𝑟** au message avant chiffrement et en le retirant après déchiffrement.
- **Chiffrement avec mélange** :
  - Choisir un nombre aléatoire **𝑟** tel que **0 < 𝑟 < 𝑛**.
  - Modifier le message avant le chiffrement : **𝑚′ = (𝑚 + 𝑟) (mod 𝑛)**.
  - Chiffrer **𝑚′** :   **𝑐 = 𝑚′^𝑒 (mod 𝑛)**.
- **Déchiffrement avec mélange** :
  - Déchiffrer comme d'habitude : **𝑚′ = 𝑐^𝑑 (mod 𝑛)**.
  - Retirer le nombre aléatoire pour retrouver le message original : **𝑚 = (𝑚′ − 𝑟) (mod 𝑛)**.
