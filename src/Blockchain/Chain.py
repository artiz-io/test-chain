from .BlockFactory import BlockFactory


class Chain:

    def __init__(self):
        self.blocks = {}
        self.head = None

    def init(self):
        self.head = BlockFactory.create_genesis_block()

    def add_block(self, block):
        self.blocks[block.index] = block
        self.head = block

    def get_head(self):
        return self.head
