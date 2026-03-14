import pytest

from unittest.mock import MagicMock
from burger import Burger
from database import Database

class TestBurger:

    def test_set_buns_correct(self):
        burger = Burger()
        bun = MagicMock()
        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient_correct(self):   
        burger = Burger()
        ingredient = MagicMock()
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients

    def test_remove_ingredient_correct(self):
        burger = Burger()
        ingredient = MagicMock() 
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient_correct(self):
        burger = Burger()
        i1 = MagicMock()
        i2 = MagicMock()
        i3 = MagicMock()
        burger.add_ingredient(i1)
        burger.add_ingredient(i2)  
        burger.add_ingredient(i3)  
        burger.move_ingredient(0,2) 

        assert burger.ingredients == [i2, i3, i1]  

    @pytest.mark.parametrize("bun, ingredient, prices",
                              [(0, [], 200),
                               (0, [0], 300),
                               (0, [0,3], 400)])      

    def test_get_price_correct(self, bun, ingredient, prices):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[bun])
        for i in ingredient:
            burger.add_ingredient(database.available_ingredients()[i])
            
        assert burger.get_price() == prices  

    def test_get_receipt_correct(self):    
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        receipt = ( "(==== black bun ====)\n"
                   "= sauce hot sauce =\n"
                   "(==== black bun ====)\n\n"
                   "Price: 300")
        
        assert burger.get_receipt() == receipt




