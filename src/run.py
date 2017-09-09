from Blockchain.Chain import Chain
from Blockchain.BlockFactory import BlockFactory

blockchain = Chain()
blockchain.init()

num_of_blocks_to_add = 20

for i in range(0, num_of_blocks_to_add):
    block_to_add = BlockFactory.create_block_from_previous_block(blockchain.get_head())
    blockchain.add_block(block_to_add)

    print("Block #{} has been added to the blockchain!".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))
