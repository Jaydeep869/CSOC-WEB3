# 🧠 Web3 Learning Journey – COPS SDG SoC 2025

Welcome to my Web3 learning log as part of the **COPS SDG Summer of Code 2025**. This repository documents weekly progress, code explanations, and learning resources.

---



<details>
  <summary><strong>Click to Expand Week 1 Details</strong></summary>
  
## 📅 Week 1 – Bitcoin Cryptography

### 🔐 1. Transaction Hasher

- Uses Python's `hashlib` for SHA-256 hashing.
- Takes a hexadecimal transaction string (must be even length) and converts it into raw bytes.
- Performs **double SHA-256 hashing**, then reverses the result to comply with Bitcoin's big-endian format.
- Converts the reversed byte array into hexadecimal to generate the **Transaction ID (TXID)**.

---

### ✍️ 2. Signature Simulator

- Uses `hashlib`, `secrets`, and `ecdsa` libraries.
- Defines a modular inverse function needed for ECDSA.
- Steps to sign:
  1. Hash the transaction and convert to an integer (`z`).
  2. Generate random nonce `k` in range \([1, n - 1]\).
  3. Compute point `R = k * G`, take `r = R.x % n`.
  4. Compute `s = (k⁻¹ * (z + r * priv_key)) % n`.
  5. Derive public key: `pub_key = priv_key * G`, then encode as hexadecimal.

- ✅ Output: Signature `(r, s)` and public key in hexadecimal format.

📚 Reference: [CryptoBook – ECDSA Signing](https://cryptobook.nakov.com/digital-signatures/ecdsa-sign-verify-messages#ecdsa-sign)

---
### ✅ 3. Signature Verifier

- Verifies the authenticity of the signature using `(r, s)`, public key, and transaction.
- Steps:
  1. Parse public key to obtain x, y coordinates and construct point `P`.
  2. Check that `r` and `s` are valid (range and malleability).
  3. Compute hash of transaction and convert to integer `z`.
  4. Calculate:
     - `u1 = z * s⁻¹ mod n`
     - `u2 = r * s⁻¹ mod n`
     - `R = u1 * G + u2 * P`
  5. Signature is valid if `R.x % n == r`.

📚 Reference: [CryptoBook – ECDSA Verification](https://cryptobook.nakov.com/digital-signatures/ecdsa-sign-verify-messages#ecdsa-sign)

---

</details>


<details>
  <summary><strong>Click to Expand Week 2 Details</strong></summary>
  
  ##  🗳️ Week 2 – DVoting Smart Contract

> **Objective:** Build a decentralized voting system using Solidity on the Ethereum blockchain.

📌 **Highlights**
- Developed and tested on **Remix IDE**
- Smart contract includes:
  - **Chairperson logic** with access control
  - **Time-restricted voting** using block timestamps
  - Structs for **voters** and **proposals**
  - **Event logging** for registration and voting
  - **Gas awareness** for blockchain state changes

🧪 **Functions Implemented**
- `registerVoter()`, `addProposal()`, `vote()`, and `getWinner()`
- Access modifiers for **chairperson-only actions** and **voting duration**

🎥 **Demo Videos Available**  
- Includes video walk-throughs of code and functionality

📂 **Full Details & Code:**  
  [Week 2 DVoting Smart Contract README](./Week%202%20DVoting%20Smart%20Contract/README.md)

📚 **References**
- [Ethereum StackExchange](https://ethereum.stackexchange.com)
- [Solidity by Example Docs](https://docs.soliditylang.org/en/v0.8.30/solidity-by-example.html)

</details>
