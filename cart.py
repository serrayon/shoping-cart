from items import shelf 
import pandas as pd

class Cart:
    def __init__(self, account, balance):
        self.account = None
        self.balance = None
        
    def add_to_cart(self):
        df = pd.DataFrame(shelf)
        print(df)
        selected_item_id = input('''select the id of the item you \n
                                want to buy\n:''')
        selected_item_quantity = input('''How many do you want\n:''')
        print(selected_item_id, selected_item_quantity)
