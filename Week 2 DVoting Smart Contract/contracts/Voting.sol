// SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;

contract Voting {
    address public chairperson;
    uint public startTime;
    uint public duration;

    constructor(uint durationinsec) {
        chairperson = msg.sender;
        startTime = block.timestamp;
        duration = durationinsec;
    }

    modifier Chairperson() {
        require(msg.sender == chairperson, "Only chairperson can do this.");
        _;
    }

    modifier DuringVoting() {
        require(
            block.timestamp >= startTime && block.timestamp <= startTime + duration,
            "Voting is finished."
        );
        _;
    }

    struct Voter {
        bool isRegistered;
        bool hasVoted;
        uint votedProposalId;
    }

    struct Proposal {
        string name;
        uint voteCount;
    }

    mapping(address => Voter) public voters;
    Proposal[] public proposals;

    event VoterRegistered(address voter);
    event VoteCast(address voter, uint proposalId);

    function registerVoter(address voter) external Chairperson {
        require(!voters[voter].isRegistered, "Already registered.");
        voters[voter].isRegistered = true;
        emit VoterRegistered(voter);
    }

    function addProposal(string memory name) external Chairperson {
        proposals.push(Proposal(name, 0));
    }

    function vote(uint proposalId) external DuringVoting {
        Voter storage sender = voters[msg.sender];
        require(sender.isRegistered, "You are not registered.");
        require(!sender.hasVoted, "You already voted.");
        require(proposalId < proposals.length, "Invalid proposal ID.");

        sender.hasVoted = true;
        sender.votedProposalId = proposalId;
        proposals[proposalId].voteCount++;

        emit VoteCast(msg.sender, proposalId);
    }

    function getWinners() external view returns (string[] memory) {
        uint highestVotes = 0;
        uint winnerCount = 0;

        for (uint i = 0; i < proposals.length; i++) {
            if (proposals[i].voteCount > highestVotes) {
                highestVotes = proposals[i].voteCount;
            }
        }

        for (uint i = 0; i < proposals.length; i++) {
            if (proposals[i].voteCount == highestVotes) {
                winnerCount++;
            }
        }

        string[] memory winnersList = new string[](winnerCount);
        uint index = 0;
        for (uint i = 0; i < proposals.length; i++) {
            if (proposals[i].voteCount == highestVotes) {
                winnersList[index] = proposals[i].name;
                index++;
            }
        }

        return winnersList;
    }
}
