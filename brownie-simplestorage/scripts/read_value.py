from brownie import SimpleStorage, accounts, network, config

# command>brownie run .\scripts\read_value.py --network rinkeby

def readContract():
    for s in SimpleStorage:
        print("Items of SimpleStorage:", s) # this works only when you have deployed to a network. Even the test net.
    print("Contract:", SimpleStorage)
    #the best idea is always to use with the latest block: SimpleStorage[-1]

def main():
    readContract()