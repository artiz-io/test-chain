import datetime as date
from .Block import Block


class BlockFactory:

    @staticmethod
    def create_genesis_block():
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    @staticmethod
    def create_block(index, data, previous_hash):
        return Block(index, date.datetime.now(), data, previous_hash)

    @staticmethod
    def create_block_from_previous_block(previous_block):
        index = previous_block.index + 1
        data = "Block " + str(index)
        previous_hash = previous_block.hash
        return BlockFactory.create_block(index, data, previous_hash)
