import hashlib
import secrets
from ecdsa import SECP256k1

curve = SECP256k1.curve
generator = SECP256k1.generator
order = generator.order()

def inverse_mod(k, p):
    return pow(k, -1, p)

def sign_transaction_manual(transaction_in_bytes: bytes, private_key: int):
   

    transaction_hash = hashlib.sha256(transaction_in_bytes).digest()
    z = int.from_bytes(transaction_hash, 'big')
    print("Transaction hash (z):", z)

    while True:
        k = secrets.randbelow(order)
        if k != 0:
            break
    R = k * generator
    r = R.x() % order
    k_inverse = inverse_mod(k, order)
    s = (k_inverse * (z + r * private_key)) % order
    public_key = private_key * generator
    pub_x = public_key.x()
    pub_y = public_key.y()
    public_key_hex = f"{pub_x:064x}{pub_y:064x}" 

    return (r, s), public_key_hex


transaction_hex = "0100000001abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"
transaction_in_bytes = bytes.fromhex(transaction_hex)
private_key = 0x1E99423A4ED27608A15A2611D3B8F8C8D2B6F5E7C9
signature, pubkey = sign_transaction_manual(transaction_in_bytes, private_key)
print("Signature (r, s):", signature)
print("Public Key:", pubkey)
