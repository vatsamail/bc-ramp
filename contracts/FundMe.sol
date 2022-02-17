// SPDX-License-Identifier : MIT
pragma solidity >= 0.6.6 < 0.9.0;

contract FundMe {
    mapping(address => uint256) public addressToAmountFunded;
    function fund() public payable{
        addressToAmountFunded[msg.sender] += msg.value;
        // eth to usd conversion: https://docs.chain.link/docs/get-the-latest-price/
        // https://docs.chain.link/docs/link-token-contracts
        // https://faucets.chain.link/kovan
        // Important: https://docs.chain.link/docs/link-token-contracts/

    }
}