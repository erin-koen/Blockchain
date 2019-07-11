import hashlib
import requests # pylint: disable=F0401

import sys


# TODO: Implement functionality to search for a proof 
def valid_proof(last_proof, proof):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:6] == "000000"

def proof_of_work(last_proof):
    proof = 0
    while valid_proof(last_proof, proof) is False:
        proof +=1
    return proof

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://0.0.0.0:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        last = requests.get(f'{node}/last_proof')
        last_proof = last.json()['proof']
        print('last proof', last_proof)
        data = {
            'proof': proof_of_work(last_proof)
        }
        print('next proof', data['proof'])
        # TODO: When found, POST it to the server {"proof": new_proof}
        res = requests.post(url = f'{node}/mine', json = data)

        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.

        print(res.json()['message'])
