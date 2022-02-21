import this
from solcx import compile_standard, install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv

import sys
import pathlib

this_folder = pathlib.Path(__file__).parent.resolve()
sys.path.append(this_folder)

load_dotenv()

# ---------------------------------------------

sol_file = os.path.join(this_folder, "SimpleStorage.sol")
with open(sol_file, "r") as file:
    simple_storage_file = file.read()

install_solc("0.6.0")
compile_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {
            "SimpleStorage.sol": {
                "content": simple_storage_file,
            }
        },
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"],
                }
            }
        },
    },
    solc_version="0.6.0",
)

with open("ComplieCode.json", "w") as file:
    json.dump(compile_sol, file)

# print("CompileSol:", compile_sol)

# get the bytecode
bytecode = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

abi = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
# print("Abi:", abi)

############
# deploying in simulated env using ganache
############

# ----------------------------------
ui_url = "http://127.0.0.1:7545"  # do it first with UI
ui_address = "0x9C66C49C04aBa136e65C69cA456Ce9128766876d"
ui_chain_id = 1337

cmdline_url = "http://127.0.0.1:8545"
cmdline_adress = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
cmdline_chain_id = 1337

testnet_url = "https://rinkeby.infura.io/v3/a5bf52c4441a45808fabb792dac874e0"  # infura.io  or alchemy etc. Use infuro.io and create an account. Use rinkeby
testnet_address = "0xbC6CA3AB027402316771b9f999894F3c9CdD551f"  # My Rinkeby address from MetaMask account. And update the private in the .env too
testnet_chain_id = 4  # refer chainid.network for rinkeby

# check the transaction here: https://rinkeby.etherscan.io/
# -----------------------------------


# ----- replacer -----------------------
chain_id = testnet_chain_id
my_address = testnet_address
my_url = testnet_url
# -----------------------------------

w3 = Web3(Web3.HTTPProvider(my_url))

private_key = os.getenv(
    "PRIVATE_KEY"
)  # check the .env file that is NOT pushed on to the source code. Also, python private key should be prefixed by 0x

print("PrivateKey from Env Variable:", private_key)

SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# print("Contract:", SimpleStorage)

# Get latest transaction
nonce = w3.eth.getTransactionCount(my_address)
print("Nonce:", nonce)

# deploy_txn = SimpleStorage.constructor(w3.eth.coinbase, 12345).transact()

transaction = SimpleStorage.constructor().buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,  # add the gas price not in the tutorial
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)
# print("Transaction Object:", transaction)

signed_transaction = w3.eth.account.sign_transaction(
    transaction,
    private_key=private_key,
)
# print("signed_transaction:", signed_transaction)

# now, transact here
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)


##########################
# working with contract need address, abi
##########################
simple_storage = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)
# only two was to interact: Call, it is like view. And Transact makes state change

# we will get 0.
print("Initial Retrieve:", simple_storage.functions.retrieve().call())


store_transaction = simple_storage.functions.store(15).buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,  # add the gas price not in the tutorial
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce + 1,
    }
)

signed_store_transaction = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)
send_store_transaction_hash = w3.eth.send_raw_transaction(
    signed_store_transaction.rawTransaction
)
transaction_receipt = w3.eth.wait_for_transaction_receipt(send_store_transaction_hash)
print("Now Retrieve:", simple_storage.functions.retrieve().call())

"""
Installations for this code
1. Ganache
2. node. Check node --version
3. npm install --global yarn # a package manager
4. yarn --version
5. yarn --global add ganache-cli or try this: npm install -g ganache-cli --force
6. ganache-cli --version
7. ganache-cli --deterministic # after closing the cli. Use deterministic to get the same private keys and addresses
"""
