# consensus_demo.py

import random
import time

def simulate_pow(validators):
    print("\n--- Proof of Work (PoW) ---")
    for name, data in validators.items():
        print(f"{name} has power: {data['power']}")
    winner = max(validators.items(), key=lambda x: x[1]['power'])
    print(f"Selected Validator (Highest Power): {winner[0]}")
    return winner[0]

def simulate_pos(validators):
    print("\n--- Proof of Stake (PoS) ---")
    for name, data in validators.items():
        print(f"{name} has stake: {data['stake']}")
    winner = max(validators.items(), key=lambda x: x[1]['stake'])
    print(f"Selected Validator (Highest Stake): {winner[0]}")
    return winner[0]

def simulate_dpos(voters):
    print("\n--- Delegated Proof of Stake (DPoS) ---")
    vote_count = {}
    for voter, vote in voters.items():
        print(f"{voter} voted for {vote}")
        vote_count[vote] = vote_count.get(vote, 0) + 1
    winner = max(vote_count.items(), key=lambda x: x[1])
    print(f"Selected Delegate (Most Votes): {winner[0]}")
    return winner[0]

if __name__ == '__main__':
    # Mock validators
    validators = {
        "Validator_A": {"power": random.randint(10, 100), "stake": random.randint(100, 1000)},
        "Validator_B": {"power": random.randint(10, 100), "stake": random.randint(100, 1000)},
        "Validator_C": {"power": random.randint(10, 100), "stake": random.randint(100, 1000)}
    }

    # Mock voters
    possible_delegates = list(validators.keys())
    voters = {
        "Voter_1": random.choice(possible_delegates),
        "Voter_2": random.choice(possible_delegates),
        "Voter_3": random.choice(possible_delegates),
    }

    start_time = time.time()

    pow_winner = simulate_pow(validators)
    pos_winner = simulate_pos(validators)
    dpos_winner = simulate_dpos(voters)

    end_time = time.time()
    print(f"\nSimulation completed in {round(end_time - start_time, 2)} seconds.")
