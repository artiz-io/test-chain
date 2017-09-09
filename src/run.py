import datetime as date
from Blockchain.Block import Block


def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(previous_block):
    index = previous_block.index + 1
    data = "Block " + str(index)
    previous_hash = previous_block.hash
    return Block(index, date.datetime.now(), data, previous_hash)


blockchain = [create_genesis_block()]
head_block = blockchain[0]

num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    block_to_add = next_block(head_block)
    blockchain.append(block_to_add)
    head_block = block_to_add

    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))
