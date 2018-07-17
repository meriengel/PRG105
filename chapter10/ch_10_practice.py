"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
    
    We are going to convert the coin class to a dice class
    The following code is based on the coin class from your book
"""

import random


class Coin:  # note class names are capitalized
    def __init__(self):
        self.side_up = 'Heads'
        
    def toss(self):
        if random.randint(0, 1) == 0:
            self.side_up = 'Heads'
        else:
            self.side_up = 'Tails'
            
    def get_side_up(self):
        return self.side_up
    

def main():
    my_coin = Coin()
    my_coin_two = Coin()
    print('This side is up, ', my_coin.get_side_up())
    print('This side is up, ', my_coin_two.get_side_up())
    
    print('I am tossing the coins...')
    my_coin.toss()
    my_coin_two.toss()
    print('This side is up, ', my_coin.get_side_up())
    print('This side is up, ', my_coin_two.get_side_up())

main()
