from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 18
STARTING_PRICE = 2000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The cative network is {network.show_active()}")
    print("deploying Mocks ..")
    if len(MockV3Aggregator) <= 0:
        mockaggregator = MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        )
    print("Mocks Deployed")
