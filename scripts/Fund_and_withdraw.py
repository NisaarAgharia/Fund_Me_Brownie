from brownie import FundMe
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
)


def fund():
    funde_me = FundMe[-1]
    account = get_account()
    entrance_fee = funde_me.getEntranceFee()
    print(entrance_fee)
    print(f"THe current entry fee is {entrance_fee}")
    print("Funding ...")
    funde_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    print("Withdraw")


def main():
    fund()
    withdraw()
