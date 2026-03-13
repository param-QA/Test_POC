// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VulnerableWallet {

    mapping(address => uint) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    // Reentrancy vulnerability
    function withdraw(uint _amount) public {
        require(balances[msg.sender] >= _amount);

        (bool success,) = msg.sender.call{value:_amount}("");
        require(success);

        balances[msg.sender] -= _amount;
    }
}