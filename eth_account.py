from eth_account import Account
acct = Account.create('KEYSMASH FJAFJKLDSKF7JKFDJ 1530')
acct.address
acct.privateKey

# These methods are also available: signHash(), signTransaction(), encrypt()
# They correspond to the same-named methods in Account.*
# but without the private key argument
'''
transaction = {
...     'to': '0xF0109fC8DF283027b6285cc889F5aA624EaC1F55',
...     'value': 1000000000,
...     'gas': 2000000,
...     'gasPrice': 234567897654321,
...     'nonce': 0,
...     'chainId': 1
... }
key = '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'
signed = w3.eth.account.signTransaction(transaction, key)
signed.rawTransaction
HexBytes('0xf86a8086d55698372431831e848094f0109fc8df283027b6285cc889f5aa624eac1f55843b9aca008025a009ebb6ca057a0535d6186462bc0b465b561c94a295bdb0621fc19208ab149a9ca0440ffd775ce91a833ab410777204d5341a6f9fa91216a6f3ee2c051fea6a0428')
signed.hash
HexBytes('0xd8f64a42b57be0d565f385378db2f6bf324ce14a594afc05de90436e9ce01f60')
signed.r
4487286261793418179817841024889747115779324305375823110249149479905075174044
signed.s
30785525769477805655994251009256770582792548537338581640010273753578382951464
signed.v'''