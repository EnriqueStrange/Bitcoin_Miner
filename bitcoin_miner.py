# -*- coding: utf-8 -*-
"""
Created on Sat May 6 11:18:23 2023

@author: Strange
"""

import hashlib

# Set the maximum number of nonce values to try before giving up
NONCE_LIMIT = 100000000000
# Set the number of leading zeroes that the hash must have to be considered a valid solution
zeroes = 4

# Define a function to mine a block given its block number, transaction data, and previous hash


def mine(block_number, transaction, previous_hash):
    # Iterate over a range of nonce values from 0 to NONCE_LIMIT
    for nonce in range(NONCE_LIMIT):
        # Concatenate the block data and nonce to form a base text
        base_text = str(block_number) + transaction + \
            previous_hash + str(nonce)
        # Calculate the SHA-256 hash of the base text
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        # Check if the hash has the required number of leading zeroes
        if hash_try.startswith('0' * zeroes):
            # If it does, print the nonce value and return the hash as the solution
            print(f"Found Hash with Nonce: {nonce}")
            return hash_try
    # If no valid solution is found, return -1
    return -1


# Example usage
block_number = 24
transaction = "76123fcc2142"
previous_hash = "876de8756b967c87"

mine(block_number, transaction, previous_hash)
