// SPDX-License-Identifier : MIT
// The above line is SPDX license identifier


// Code: https://remix.ethereum.org

pragma solidity ^0.6.0;
// ^0.6.0; // means above 0.6 and below 0.7
//>= 0.6.0 < 0.9.0;

// like class
contract SimpleStore {
    // data types
    uint x = 5;
    int y = -5;
    uint256 fav_number = 5;
    bool is_favorite = true;
    string message = "Hello world";
    address my_acc1_addr = 0x0b271D876F4d6148462292DE8a49b178E3cd7C9c;
    bytes32 word32 = "cat"; // max is 32

    
    // datatype isibility
    // external - can't be called by the same contract. Can be called only by exaernal contracts!
    // public - can be called by anybody
    // internal - can be called only by the contract or derived contracts. This is default.
    // private - can be called only by the contract and no derived contracts. 

    uint256 some_number; // initialized to zero // try not to make it public, let it be internal
    bool male; // this is at index 1
    bool alive; // this is index 2


    struct People {
        string name; // index 0
        uint256 age; // index 1
    }

    People[] public people; // dynamic array
    People[10] public members; // fixed array

    People public person = People({name: 'vatsa', age: 20});

    mapping(string => uint256) public name_to_age;

    // methods
    function store(uint256 val) public {
        some_number = val;
        // store(100);
        // if store() is called here and if it is visible as external then it will fail.
    }

    function square(uint _xy) public pure returns (uint256) {
        uint256 blah = _xy * _xy;
        return blah;
    }

    function get() public view returns (uint256) {
        return some_number;
        // view keyword just reads the state of blockchain. No charge
        // pure keyword just does some math. Again no charge. No saving state.
    }

    function update() public {
        some_number = square(some_number);
    }

    // memory and storage differences.
    // memory works only during the execution. 
    // storage will persist after the data executes 
    // this is required for string as because it is an object of an array of charaters
    function addPerson(string memory _name, uint256 _age) public {
        people.push(People({name: _name,  age:_age}));
        people.push(People(_name, _age)); // duplicating entry but now in the form of array and not dictionary
        name_to_age[_name] = _age;
    }


}