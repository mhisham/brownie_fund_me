from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import LOCAL_DEVELOPMENT_NETWORKS, deploy_mocks, get_account
from web3 import Web3




def deploy_fund_me():
  account = get_account()
  print(account)
  if(network.show_active() not in LOCAL_DEVELOPMENT_NETWORKS):
    price_feed_aggregator = config["networks"][network.show_active()]["eth_usd_price_feed"]
  else:
    deploy_mocks()
    price_feed_aggregator = MockV3Aggregator[-1].address

  fund_me = FundMe.deploy(price_feed_aggregator,
  {"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
  print(f"Contract deployed on {fund_me.address}")
  return fund_me





def main():
    deploy_fund_me()