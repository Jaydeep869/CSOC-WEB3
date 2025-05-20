import hashlib
from ecdsa import SECP256k1, ellipticcurve
from ecdsa import SECP256k1, SigningKey
from ecdsa.util import sigdecode_string


curve = SECP256k1.curve
G = SECP256k1.generator
n = G.order()

def verify_signature(public_key: bytes, sig: tuple, transaction_hash: bytes) -> bool:

    r, s = sig

    if not (1 <= r < n and 1 <= s < n):
        return False
    if s > n // 2:
        return False

    if len(public_key) != 64:
        return False  

    x = int.from_bytes(public_key[:32], 'big')
    y = int.from_bytes(public_key[32:], 'big')
    try:
        P = ellipticcurve.Point(curve, x, y)
    except:
        return False  

    z = int.from_bytes(transaction_hash, 'big')
    s_inv = pow(s, -1, n)
    u1 = (z * s_inv) % n
    u2 = (r * s_inv) % n
    R = u1 * G + u2 * P

    if R == ellipticcurve.INFINITY:
        return False
    return (R.x() % n) == r