#!/usr/bin/python3
# SHA-245 function source: https://onuratakan.medium.com/what-is-the-merkle-tree-with-python-example-cbb4513b8ad0#:~:text=What%20is%20the%20Merkle%20Tree%20%E2%80%94%20With%20Python,verification%20of%20the%20contents%20of%20large%20data%20structures.

import hashlib
import os

class MerkleTree():

    def __init__(self):
        pass

    def hash(val):
        return hashlib.sha256(val.encode("utf-8")).hexdigest()

    def find_merkle_root_hash(node_hashes):
        list_length = len(node_hashes)

        concatenated_hashes = []

        # handles the case in which there are an even number of leaf nodes
        if list_length % 2 == 0:
            for x in [node_hashes[y:y+2] for y in range(0, list_length, 2)]:
                concatenated_hashes.append(hash(x[0] + x[1]))
        # else, we must handle case in which there are an odd number of leaf nodes, where the parent's hash will just be the hash of the child for the last node
        else:
            for x in [node_hashes[y:y+2] for y in range(0, list_length - 1, 2)]:
                concatenated_hashes.append(hash(x[0] + x[1]))
                concatenated_hashes.append(node_hashes[list_length - 1])
        
        # when there is only 1 hash in the array, we must have reached the root hash, so we return it
        if len(concatenated_hashes) == 1:
            return concatenated_hashes[0]
        # else, use recursion to repeatedly hash the concatenation of the hashes of the left and right child nodes for each level of the Merkle tree
        else:
            return MerkleTree.find_merkle_root_hash(concatenated_hashes)
            
    def hash_address_and_balance(address, balance):
        
        # converts to type string just in case both the address and balance are all ints
        balance = str(balance)
        address = str(address)
        hashed_concatenation = MerkleTree.hash(address + balance)
        return hashed_concatenation
    
    def main():

        addresses = []
        balances = []
        hashes = []

        txtFile = input('Enter text file with accounts:')
        with open(txtFile, 'r') as fp:
            for line in fp:
                x, y = line.split(' ')
                addresses.append(x)
                balances.append(y)

        print(addresses)
        print(balances)
        

          for x,y in zip(addresses, balances):
            hashed_concatenation = MerkleTree.hash_address_and_balance(x, y)
            hashes.append(hashed_concatenation)

        print(hashes)
        root_hash = MerkleTree.find_merkle_root_hash(hashes)
        print ("Merkle tree root hash: %s"%(root_hash))


if __name__ == "__main__":
    MerkleTree.main()
