#Pour transférer des fonds d'un compte à un autre.
from web3 import Web3

# Connexion au nœud Ethereum (Geth)
w3 = Web3(Web3.HTTPProvider('http://10.229.43.181:8545/'))  # Assurez-vous que le nœud est accessible

# Adresse et clé privée
sender_address = "0x4b568226882C0BD36c3295c83052D48a1bbC955F"
private_key = "788efd1ce90209164c07cc625c0ed65c1aff689c22285ef3d00dde28072b5974"  # Remplacez par la clé privée correspondante

# Adresse du destinataire et montant à transférer
recipient_address = "0x4af55Dc30b5e9c61E3bF13b5BB3453ef0D98Aed9"
amount_in_ether =  0.01 # Montant à envoyer en ETH

try:
    # Convertir les adresses en format checksum
    sender_address = w3.to_checksum_address(sender_address)
    recipient_address = w3.to_checksum_address(recipient_address)
    
    # Convertir Ether en Wei
    value = w3.to_wei(amount_in_ether, 'ether')

    # Récupérer le nonce pour l'adresse de l'expéditeur
    nonce = w3.eth.get_transaction_count(sender_address)

    # Construire la transaction
    transaction = {
        'nonce': nonce,
        'to': recipient_address,
        'value': value,
        'gas': 32000,  # Gas limite pour une transaction simple
        'gasPrice': w3.eth.gas_price,  # Récupérer le prix du gas actuel
        'chainId': 32382  # Remplacez par votre chainId personnalisé
    }

    # Signer la transaction avec la clé privée
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

    # Envoyer la transaction signée
    tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)

    # Afficher le hash de la transaction
    print(f"Transaction envoyée avec succès ! Hash : {w3.to_hex(tx_hash)}")

except Exception as e:
    print(f"Une erreur est survenue : {str(e)}")

