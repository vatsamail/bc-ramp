// SPDX-License-Identifier: MIT
pragma solidity >= 0.6.6 < 0.9.0;

// this compiled to application binary interface: ABI
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

// openzepplin library
// import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";


contract MyFundMe {

    address public owner;
    
    constructor() public {
        owner = msg.sender;
    }

    uint256 given_usd;

//    using SafeMathChainlink for uint256; // doesn't allow overflow issue

    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;

    function fund() public payable{
        addressToAmountFunded[msg.sender] += msg.value;
        // eth to usd conversion: https://docs.chain.link/docs/get-the-latest-price/
        // https://docs.chain.link/docs/link-token-contracts
        // https://faucets.chain.link/kovan
        // Important: https://docs.chain.link/docs/link-token-contracts/

        // let's set the price to $50
        // uint256 min_usd = 50;
        
        // 18 digit number to be compared with donated amount 
        // uint256 minimumUSD = min_usd * 10 ** 18;
        //is the donated amount less than 50USD?
        // require(getConversionRate(msg.value) >= minimumUSD, "You need to spend more ETH!");

        // cheap fellow
        require(getConversionRate(msg.value) >= 1, "at least give me something");
        //if not, add to mapping and funders array
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
        
    }

    function showGivenUsd() public view returns(uint256) {
        return given_usd;
    }


    function getPriceOfOneEth() public view returns(uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        (,int256 answer,,,) = priceFeed.latestRoundData();
        return uint256(answer * 10 ** 10);
        // 288520973864 = > 2885.20973864 * 10 ** 10;

    }

     // 1000000000
    function getConversionRate(uint256 ethAmount) public view returns (uint256){
        uint256 ethPrice = getPriceOfOneEth();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        // the actual ETH/USD conversation rate, after adjusting the extra 0s.
        return ethAmountInUsd;
    }



    function convertOneEthToUsd() public view returns(uint256) {
        uint256 wei_per_eth = getPriceOfOneEth();
        uint256 one_eth_in_usd = wei_per_eth / (10 ** 18);
        return one_eth_in_usd;
    }

    modifier onlyOwner {
        require (msg.sender == owner, "you must be the owner to withdraw the amount");
        _; // here is where your withdraw or any other function can be called
    }

    function withdraw() payable onlyOwner public {
        // this is the current address
        msg.sender.transfer(address(this).balance);

        // resetting the balances to 0 for all the funders
        for (uint256 i = 0; i < funders.length; i++) {
            address funder = funders[i];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0); // cleaning the funder array
    }
}