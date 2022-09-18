# SHA-245 function source: https://onuratakan.medium.com/what-is-the-merkle-tree-with-python-example-cbb4513b8ad0#:~:text=What%20is%20the%20Merkle%20Tree%20%E2%80%94%20With%20Python,verification%20of%20the%20contents%20of%20large%20data%20structures.

import hashlib

class MerkleTree():

    def __init__(self):
        pass

    def hash(val: str)-> str:
        return hashlib.sha256(val.encode("utf-8")).hexdigest()

    def find_merkle_root_hash(self, node_hashes):

        nodes = []

        for h in node_hashes:
            nodes.append(h)

        list_length = len(nodes)

        # must handle case where there are an odd number of leaf nodes, where parent will just be the hash of the child for the last leaf node

        concatenated_hashes = []

        for x in [nodes[y:y+2] for y in range(0, list_length, 2)]:
            concatenated_hashes.append(hash(x[0] + x[1]))
        
        if len(concatenated_hashes) == 1:
            return concatenated_hashes[0]
        else:
            return self.find_merkle_root_hash(concatenated_hashes)
            
    def hash_address_and_balance(address: str, balance: int)-> str:
        hashed_address = MerkleTree.hash(address)
        balance_as_string = str(balance)
        hashed_balance = MerkleTree.hash(balance_as_string)
        concatenation = hashed_address + hashed_balance
        hashed_concatenation = MerkleTree.hash(concatenation)
        return hashed_concatenation
    
    def main():

        # need to read in the values from the text file for addresses and balances

        addresses = [str]
        balances = [int]
        hashes = [str]

        for i in range(len(addresses) - 1):
            hashed_concatenation = MerkleTree.hash_address_and_balance(addresses[i], balances[i])
            hashes.append(hashed_concatenation)

        hash = MerkleTree()
        root_hash = hash.find_merkle_root_hash(hashes)
        print ("Merkle tree root hash: %s"%(root_hash))