from web3 import Web3

# Connexion au nœud
web3 = Web3(Web3.HTTPProvider("http://10.229.43.181:8545/"))


# Vérifier la connexion
if web3.is_connected():
    print("Connexion à Ethereum réussie")
else:
    print("Échec de la connexion à Ethereum")

# Adresse Ethereum dont vous voulez obtenir le solde
address = '0x4b568226882C0BD36c3295c83052D48a1bbC955F'

# Obtenir le solde de l'adresse
balance = web3.eth.get_balance(address)

# Convertir le solde de Wei à Ether
balance_ether = web3.from_wei(balance, 'ether')

print(f"Le solde de l'adresse {address} est de {balance_ether} ETH")