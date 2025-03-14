#Pour récupérer la clé privée stockée dans le keystore de geth
import json
from eth_account import Account

# Chemin vers le fichier keystore JSON
keystore_file = "C:/Users/pr08glt/Desktop/MODULE_3/C-107/UTC--2025-01-30T14-10-38.884353500Z--4b568226882c0bd36c3295c83052d48a1bbc955f"

# Charger le fichier JSON
with open(keystore_file, "r") as f:
    encrypted_key = json.load(f)

# Mot de passe pour décrypter la clé
password = "Ahmet2460."

# Décrypter la clé privée
private_key = Account.decrypt(encrypted_key, password)
print("Clé privée :", private_key.hex())

