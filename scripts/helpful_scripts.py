from brownie import network,accounts,config, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev"]
LOCAL_DEVELOPMENT_NETWORKS = ["development", "ganache-local"]

def get_account():
  if( network.show_active() in LOCAL_DEVELOPMENT_NETWORKS
      or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
    return accounts[0]
  else:
    if(network.show_active() == "rinkeby"):
      return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
  print(f"The active network is {network.show_active()}")
  if len(MockV3Aggregator) <= 0 :
    print("Deploying Mocking....")
    MockV3Aggregator.deploy( 18, Web3.toWei(2000, "ether"), {"from": get_account()})
  print("Deployed Mock!")
