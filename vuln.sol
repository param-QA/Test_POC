pragma solidity ^0.8.0;

contract Vault {
    mapping(address => uint) public balances;

    function withdraw() public {
        uint bal = balances[msg.sender];
        require(bal > 0);
        // Trigger: Sending ETH before updating the state (Checks-Effects-Interactions violation)
        (bool sent, ) = msg.sender.call{value: bal}("");
        require(sent);
        balances[msg.sender] = 0;
    }
}
