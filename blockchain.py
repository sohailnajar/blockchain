class Blockchsi(object):
    def __init__(self):
        self.chin = []
        self.current_transaction = []
        
        
    def new_block(self):
        # creates a new block and adds it to the chain
        pass
    
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new tansaction to go into next mined block
        
    
        """
        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
            })
        return self.last_block['index'] + 1
    
    @staticmethod
    def hash(block):
        # hash a block
        pass
    
    
    @property
    def last_block(self):
        # return the last block in the chain
        pass
    
    