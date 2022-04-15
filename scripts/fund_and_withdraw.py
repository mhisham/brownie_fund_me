from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account


def fund():
  print(len(FundMe))
  fund_me = FundMe[-1]
  account = get_account()
  entrance_fee = fund_me.getEntranceFee()
  print(f"The current entrance fee {entrance_fee}")
  print("Fund")
  fund_me.fund({"from": account, "value": entrance_fee})

def withdraw():
  fund_me = FundMe[-1]
  account = get_account()
  fund_me.withdraw({"from": account})


def main():
  fund()
  withdraw()
