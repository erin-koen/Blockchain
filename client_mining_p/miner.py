import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof 
def proof_of_work(last_proof):
    proof = 0
    while 

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        last = requests.get(f'{node}/last_proof')
        last_proof = last.json()['proof']
        @property
        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        pass
