import hashlib  

def create_tx_hash(tx_hex: str) -> str:
    if len(tx_hex) % 2 != 0:
        print("Error: Hex string must have an even number of characters.")
        return None
    try:
        tx_bytes = bytes.fromhex(tx_hex)
    except ValueError:
        print("Error: Input is not a valid hex string.")
        return None
    
    first_hash = hashlib.sha256(tx_bytes).digest()
    second_hash = hashlib.sha256(first_hash).digest()
    reversed_hash = second_hash[::-1]
    # print("First hash (SHA-256):", first_hash)
    # print(reversed_hash)
    txid = reversed_hash.hex()
    return txid

hex_data = "0100000001abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"
txid = create_tx_hash(hex_data)
print("TXID:", txid)
    