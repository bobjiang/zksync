import asyncio
import binascii
from pprint import pprint
from web3 import Web3, Account, HTTPProvider
from zksync_sdk import ZkSyncLibrary, ZkSync, ZkSyncSigner
from zksync_sdk import EthereumSignerWeb3, EthereumProvider
from zksync_sdk import HttpJsonRPCTransport, ZkSyncProviderV01, network

# pipenv install -e git+https://github.com/zksync-sdk/zksync-python.git#egg=zksync_sdk

# async def get_contracts():
#     pass

async def get_wallet():
    # Load crypto library
    library = ZkSyncLibrary()

    # Create Zksync Provider
    zk_provider = ZkSyncProviderV01(provider=HttpJsonRPCTransport(network=network.rinkeby))

    # Load contract addresses from server
    contracts = await zk_provider.get_contract_address()

    pprint(contracts)
    contracts.main_contract
    print(contracts.main_contract)

    # Setup web3 account
    account = Account.from_key("")
    pprint(account)
    addr = account.address
    print(addr)

    # Create EthereumSigner
    eth_signer = EthereumSignerWeb3(account=account)

    # Setup web3
    w3 = Web3(HTTPProvider(endpoint_uri="") )

    # Setup zksync contract interactor
    zksync = ZkSync(account=account, web3=w3,
                    zksync_contract_address=contracts.main_contract)

    # Create ethereum provider for interacting with ethereum node
    eth_provider = EthereumProvider(w3, zksync)

    # Initialize zksync signer, all creating options were described earlier
    zk_signer = ZkSyncSigner.from_account(account, library, network.rinkeby.chain_id)

    # # Initialize Wallet
    # wallet = Wallet(ethereum_provider=eth_provider, zk_signer=zk_signer,
    #                 eth_signer=eth_signer, provider=zk_provider)

    # # Checking zkSync account balance
    # committedETHBalance = await wallet.get_balance("ETH", "committed")

    # # Verified state is final
    # verifiedETHBalance = await wallet.get_balance("ETH", "verified")

    # print(verifiedETHBalance)


# account_info
async def get_account_info():
    account_state = await wallet.get_account_state()
    committed_eth_balance = account_state.committed.balances.get("ETH")
    verified_dai_balance = account_state.verified.balances.get("DAI")

if __name__=="__main__":
    # wallet =
    asyncio.run(get_wallet())
