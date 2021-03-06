# bc-ramp
### Fundamentals of Block Chain development
### Technologies: Ethereum, Dapps, Python, Solidity, DAO, DeFi, Polygon, Chainlink, Metamask

### Features:
* Decentralized - n/w of independent users
* Transparent - no back door deals
* Speed - seconds to minutes
* Immutable, so secured
* Remove brand based agreement to 
* Trust minimized agreement
* Hybrid smart contracts - chainlink
* Decentralized Autonomous organization

## Read more
* Blockchain Oracles  - interface b/w BC and External data
* Hybrid smart contracts - Chainlink ( a powerful blockchain oracle)


## General Pointers
* https://www.youtube.com/watch?v=M576WGiDBdQ&list=PLI85das5B-EArbVej37onhhawk20IIMwb
* Rinkyby know-how: https://www.youtube.com/watch?v=M576WGiDBdQ&t=7655s 
* https://etherscan.io/ -> check your address
* https://faucet.rinkeby.io/ or https://www.rinkeby.io/#faucet -> test n/w for sample transaction
* https://ethgasstation.info/
* https://remix.ethereum.org/
* https://data.chain.link/ getting the latest price
* Api calls: https://docs.chain.link/docs/get-the-latest-price 
* https://blog.polymath.network/a-simple-guide-for-getting-kovan-testnet-poly-27ddeb1149cb
* https://docs.chain.link/docs/link-token-contracts/


## Course pointers
* https://andersbrownworth.com/blockchain/ - Hands on demonstration. Don't miss it.
* Learning Solidity: Refer: https://github.com/smartcontractkit/full-blockchain-solidity-course-py



## Setup
"""
Installations for this code
1. Ganache
2. node. Check node --version
3. npm install --global yarn # a package manager
4. yarn --version
5. yarn --global add ganache-cli or try this: npm install -g ganache-cli --force
6. ganache-cli --version
7. ganache-cli --deterministic # after closing the cli. Use deterministic to get the same private keys and addresses
8. pip install web3
9. pip install eth-brownie
"""


### Jargons
* Consensus: agreement the state of the block chain. Example: Nakomoto concensus
* Proof of work (algo for blockchain riddle). Cause a lot of electricity for mining.
* Gas or transaction fee
* Proof of stake : paid to validator (not miners). Puts a stake and then when it misbehaves it loses the money. Example: Pocodock, pockodot, antera - eth-2.0 upgrades. It is faster and gives sybil attack protection. But the cons, it is slightly less decentralized.
* Randomness: ETH-2.0 for selection of nodes.
* Block reward : cuts in 1/2 once every 4 years for bitcoin. miners currently get block reward + transaction fee. Eventually just transaction fee
* Attacks: 1. sybil attack: one node when it fakes to be multiple machine to create multiple collaterals and 2. 51% attack: to influence the network. ETH-classic had this issue.
* Sharding: is a solution that is blockchain of blockchain and solves scalability problem.
* Layer #1 : Base layer solution example: eth, bitcoin etc. 
* Layer #2: Chainlink, orbitron, optimism and has rollups.
* rollup and sidechain: rollup derives the hash security from base but sidechain will have its own. 
* 