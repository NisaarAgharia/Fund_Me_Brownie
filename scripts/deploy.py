from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    deploy_mocks,
    get_account,
)
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contract
    # if we are on rinkeyby account use address
    # else use mocks
    print(network.show_active())

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()

        price_feed_address = MockV3Aggregator[-1].address
    print(network.show_active())
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=False
        # publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
