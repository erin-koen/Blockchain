import hashlib
from uuid import uuid4
import requests

import sys


def proof_of_work(last_proof):
    """
    Simple Proof of Work Algorithm
    - Find a number p' such that hash(pp') contains 6 leading
    zeroes, where p is the previous p'
    - p is the previous proof, and p' is the new proof
    """

    print("Searching for next proof")
    proof = 0
    while valid_proof(last_proof, proof) is False:
        proof += 1

    print("Proof found: " + str(proof))
    return proof


def valid_proof(last_proof, proof):
    """
    Validates the Proof:  Does hash(last_proof, proof) contain 6
    leading zeroes?
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:6] == "000000"


def get_my_id():
    my_id = str(uuid4()).replace('-', '')
    try:
        # try to create a file called 'my_id', will get bumped to the except block if it already exists. If it doesn't, save the id you created above for future use.
        with open('./credit_for_mining/my_id', x) as f:
            f.write(my_id)

    except:
        # if the file's already been created, you'll get here and reassign my_id to the one that's already been created
        with open('./credit_for_mining/my_id', r) as f:
            my_id = f.read()
    finally:
        # either way, you'll get here and return the id
        return my_id


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = int(sys.argv[1])
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))
        my_id = get_my_id()

        post_data = {"proof": new_proof, "id": my_id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
