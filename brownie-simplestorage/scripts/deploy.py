from brownie import accounts
from brownie import config
from brownie import network

from brownie import SimpleStorage

import os

# command> brownie run scripts/deploy.py
# command> brownie run scripts/deploy.py --network rinkeby # after adding WEB3_INFURA_PROJECT_ID in .env

def deploy_simple_storage():
    #local_account = accounts[0]
    #print("Default account", local_account)

    local_account = getAccount()
    print("Dynamic account:", local_account)
    
    #rink_account = accounts.load('rinkeby-test')
    #print("My account", rink_account)
    
    #rink_4m_os = accounts.add(os.getenv('PRIVATE_KEY'))
    #print("Os based my rink private key:", rink_4m_os)
    
    #this_account = accounts.add(config['wallets']['from_key'])
    #print("This account:", this_account)

    simple_obj = SimpleStorage.deploy({'from': local_account})
    print("Contract Object:", simple_obj)

    #Call/View function
    store_value = simple_obj.retrieve()
    print("Stored Value:", store_value)

    #Transaction
    transact = simple_obj.store(15, {'from': local_account})
    transact.wait(1)
    store_value = simple_obj.retrieve()
    print("Stored Value Now:", store_value)




def getAccount():
    if (network.show_active() == 'development'):
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])


def main():
    print("Hello world, from Brownie")
    deploy_simple_storage()