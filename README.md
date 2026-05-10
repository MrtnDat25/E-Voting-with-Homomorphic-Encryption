# E-Voting-with-Homomorphic-Encryption
Research and develop small demo of homomorphic encryption algorithm

##  Introduction

This project is a mini implementation of a secure electronic voting (E-Voting) system using the Paillier Homomorphic Encryption cryptosystem.

The system demonstrates how encrypted ballots can be aggregated and counted without decrypting individual votes, preserving voter privacy while maintaining election integrity.

The project simulates a simplified real-world homomorphic voting architecture including:

* Voting Authority
* Voter Client
* Homomorphic Tally Server
* Public Bulletin Board

---

#  Main Features

✅ Paillier Homomorphic Encryption
✅ Secure encrypted ballots
✅ Homomorphic tallying
✅ Election authority separation
✅ Public bulletin board
✅ Vote receipt verification
✅ End-of-election workflow
✅ Bit-packing vote encoding

---

#  Homomorphic Property

The Paillier cryptosystem supports additive homomorphism:

[
    E(m_1) \cdot E(m_2) = E(m_1 + m_2)
]

This allows the server to count encrypted votes without decrypting them individually.

---

#  System Architecture

```text
+-------------------+
|   Voter Client    |
|     vote.py       |
+-------------------+
          |
          v
+-------------------+
| Encrypted Ballots |
| encrypted_vote.txt|
+-------------------+
          |
          v
+---------------------------+
| Homomorphic Tally Server  |
| homomorphic_server.py     |
+---------------------------+
          |
          v
+---------------------------+
| homomorphic_vote.txt      |
| Aggregated Ciphertext     |
+---------------------------+
          |
          v
+---------------------------+
| Voting Authority          |
| vote_authority.py         |
+---------------------------+
          |
          v
+---------------------------+
| Final Election Result     |
+---------------------------+
```

---

#  Project Structure

```text
project/
│
├── config.py
├── vote.py
├── vote_authority.py
├── homomorphic_server.py
├── vote_end.py
├── bulletin_board.py
│
├── public.txt
├── private.txt
├── voter.txt
├── encrypted_vote.txt
├── homomorphic_vote.txt
├── bulletin_board.txt
├── vote_status.txt
│
└── README.md
```

#  How to Run

---

## Step 1 — Generate Election Data and Keys

Run:

```bash
python vote_authority.py
```

Choose:

```text
1
```

This will:

* generate Paillier keys
* create voter database
* initialize election state

---

## Step 2 — Vote

Run:

```bash
python vote.py
```

Example:

```text
Enter your Vote ID: 1
Choose candidate: 0
```

The system:

* encrypts the ballot
* stores ciphertext
* creates a vote receipt

---

## Step 3 — View Bulletin Board

Run:

```bash
python bulletin_board.py
```

Features:

* display encrypted ballots
* verify vote existence
* search by vote ID

---

## Step 4 — Aggregate Votes

Run:

```bash
python homomorphic_server.py
```

The server:

* multiplies encrypted ballots
* produces homomorphic tally

---

## Step 5 — End Election

Run:

```bash
python vote_end.py
```

This will:

* close election
* decrypt final tally
* display winner

---

#🔒 Security Concepts

This project demonstrates:

## ✔️ Ballot Privacy

Votes remain encrypted during tallying.

---

## ✔️ Homomorphic Counting

Server computes vote totals without decrypting ballots.

---

## ✔️ Public Verification

Voters can verify their ballots using the bulletin board.

---

## ✔️ Separation of Authority

The tally server cannot decrypt votes.

---

#  Limitations

This is an educational/demo implementation.

The project does NOT yet include:

* digital signatures
* zero-knowledge proofs
* secure authentication
* network communication
* blockchain integration
* production-grade key management

---

#📚 Technologies Used

* Python
* Paillier Homomorphic Encryption
* UUID
* File-based storage

---

# 🗳️ Example Voting Flow

```text
Vote YES -> Encrypt -> Send Ciphertext
                     ->
              Homomorphic Multiplication
                     ->
              Decrypt Final Sum
```

Example:

```text
Enc(1) * Enc(0) * Enc(1)
```

After decryption:

```text
1 + 0 + 1 = 2
```

---

# 👨‍💻 Author

Dinh Quoc Dat - CT07N0107
Vietnam Academy of Cryptography Techniques
---

# 📌 Future Improvements

* GUI voting interface
* SQLite/MySQL database
* RSA digital signatures
* Zero-Knowledge Proofs
* Secure sockets
* Blockchain integration
* Multi-authority decryption

---
