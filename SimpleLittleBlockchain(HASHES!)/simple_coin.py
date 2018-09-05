from blockchain import Blockchain
from block import Block

# Initiates blockchain

def generate_blocks(number_of_blocks):
    """
    input: number_of_blocks: int
    output: hash of final block: str

    Given a number of blocks return the output after x amount of block as a string. 
    Input blocks are EMPTY
    """

    ###
    if Blockchain.blocks == []:
        Blockchain()
        for i in range((int(number_of_blocks) - 1)):
            Blockchain.mine(Blockchain, Blockchain.blocks[-1])
            print(Blockchain.blocks[-1])
    else:   
        for i in range(int(number_of_blocks)):
            Blockchain.mine(Blockchain, Blockchain.blocks[-1])
            print(Blockchain.blocks[-1])
    return Blockchain.blocks[-1].hash
    
    """
    Blockchain()
    for i in range((int(number_of_blocks) - 1)):
        Blockchain.mine(Blockchain, Blockchain.blocks[-1])
        print(Blockchain.blocks[-1])
    return Blockchain.blocks[-1].hash
    """
    
    """
    bc = Blockchain()
    bc
    for i in range(int(number_of_blocks) - 1):
        blk = bc.get_current_block()
        bc.mine(parent_block=blk)
        print(bc.blocks[-1])
        
    return bc.blocks[-1].hash
    """

# Continously generate Blocks that stack on each other
while True:
    generate_blocks(input("How many blocks do you want to generate? "))
    print('Do you want to generate more? (yes or no)? ')
    if not input().lower().startswith('y'):
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    