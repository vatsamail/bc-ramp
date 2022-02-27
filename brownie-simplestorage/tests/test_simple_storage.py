from brownie import SimpleStorage, accounts

# command> brownie test
# command> brownie test -k test_update_storage
# command> brownie test --pdb # for debugger when it fails
# command> brownie test -s # prints print statements

def test_deploy():
    # arrange
    account = accounts[0]

    # act
    simple_storage = SimpleStorage.deploy({'from': account})
    init_value = simple_storage.retrieve()
    expected_init_value = 0

    # assert
    assert init_value == expected_init_value

def test_update_storage():
    # arrange
    account = accounts[0]
    print("This account:", account)
    simple_storage = SimpleStorage.deploy({'from': account})

    # act
    expected_value = 15
    transaction = simple_storage.store(expected_value, {'from': account})
    print("The trasaction is:", transaction)
    now_value = simple_storage.retrieve()

    # assert
    assert now_value == expected_value

