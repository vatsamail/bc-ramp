from brownie import FundMe, accounts, network, config


def deployFundMe():
    acc = getAccount()
    print("Account:", acc)

    f = FundMe.deploy({'from': acc})
    print("FundMe is deployed:", f)


def getAccount():
    if (network.show_active()== 'development'):
        print("Dealing with the local development network")
        return accounts[0]
    else:
        print("Dealing with non development network:", network.show_active())
        return accounts.add(config['wallets']['from_key'])

def main():
    deployFundMe()

if __name__ == '__main__':
    main()