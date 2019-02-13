#Initializing our blockchain list
blockchain = []
open_transactions=[]
owner = 'Lukasz'
def get_last_blockchain_value():
    """Returns the last value of the blockchain"""
    if len(blockchain)<1:
        return None
    else:
        return blockchain[-1]

def add_transaction(sender, recipient, amount=1.0):
    """Adds value to existing blockchain
    Arguments:
        :sender: person that send coins.
        :recipient: person that receive coins.
        :amount: sent amount of coins (default 1.0)."""
    transaction={'sender':sender,
                 'recipient':recipient,
                 'amount':amount}
    open_transactions.append(transaction)

def mine_block():
    pass

def get_transaction():
    """Gets amount of the operation"""
    tx_recipient= input("Who is going to receive coins? ")
    tx_amount= float(input("Your transaction amount please: "))
    return (tx_recipient,tx_amount) #tuple

def get_user_choice():
    user_input=input("Your choice: ")
    return user_input

def print_blockchain():
    for block in blockchain:
        print("Outputting block")
        print(block)
    else:
        print('-' * 20)

def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        if blockchain[block_index][0] == blockchain[block_index-1]:
            is_valid=True
        else:
            is_valid=False
            break
    return is_valid

waiting_for_input=True

while waiting_for_input:
    print("Please choose: ")
    print("1: Add transaction to the blockchain.")
    print("2: Check the blockchain blocks.")
    print("h: Manipulate the blockchain")
    print("q: Quit")
    user_choice=get_user_choice()
    if user_choice=="1":
        tx_amount=get_transaction()
        add_transaction(last_transaction=get_last_blockchain_value(),
                        transaction_value=tx_amount)
    elif user_choice=="2":
        print_blockchain()
    elif user_choice=="h":
        if(len(blockchain) >= 1):
            blockchain[0]=[2]
    elif user_choice=="q":
        waiting_for_input = False
    else:
        print("Wrong input")
    if not verify_chain():
        print("The chain is invalid!")
        break
else:
    print("User left!")
print("done!")