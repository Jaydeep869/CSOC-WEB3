### Week 2 (Writing a smart contract for a DVoting App)
---
1. this time we have to create a smart contract which will be used for decentralized voting . so we are doing it on ethereum network so we are going to use solidity to create our smart contract and test it on the remix. 
2. so i will be explaining my code in snippets.
3. so first we will be writing solidity version firstly and we can fix its version by not adding ^ to it and writing a contract name voting there . 
4. now defining the cahirperson and storing its address on ethereum blockchain and he will be one who will deploy the contarct 
5. defing the start time and the duration of the contract to which the voting will last from the time of deployment.
6. defining the constructor and as it run once when the contract deployed so making chairperson in it and putting the current block time in the starttime and duration till the contract will allow to vote and duration is given by deployer of contract. 
7. creating modifiers for main things that only chairperson can do and for time limit of the contract.
8. creating two structs one for voter registration and second for proposals.
9. taking proposals and maping the address of the voter for registration so the voter can vote .
10. creating the events for voter registration and vote cast as we are in remix it is not of more use but when we will connect it with frontend or ui then it will log our action to it and tells us when it is done . 
11. creating the registerVoter function which can be call by chairperson only and it will registered an address as voterid.
12. creating a addProposal function  which can be called only by chairperson .
13. creating a function called vote which cna be used only during voting duration as mention above and sets for not vote again for the same address.
14. create a getWinner function which can be called by anyone and returns the winner of the election and return more winners if there is clash .
15. when we change any memory on the blockchain we have to give a tax type thing called gas for making it updated in our case we have got some fake ether which we are using for our changes.
---
### Reference:
* ethereum stack exchange ```https://ethereum.stackexchange.com/```
* remix ai for error analysis
* docs of solidity ```https://docs.soliditylang.org/en/v0.8.30/solidity-by-example.html```