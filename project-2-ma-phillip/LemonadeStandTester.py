# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 4, 2022
# Description: Imports LemonadeStand.py to unit test the classes contained in it

import unittest
import LemonadeStand as lemon

class TestLemonadeStand(unittest.TestCase):

    def test1(self):
        """Test init method and get name method for MenuItem"""
        item1 = lemon.MenuItem('banana', .5, 1.5)
        self.assertEqual(item1.get_name(), 'banana')

    def test2(self):
        """Test init method and get name method for LemonadeStand"""
        stand = lemon.LemonadeStand('Woo Lemons')
        self.assertEqual(stand.get_name(),'Woo Lemons')

    def test3(self):
        """Tests total_profit_for_menu_item given 3 floats"""
        stand = lemon.LemonadeStand('Woo Lemons')
        item1 = lemon.MenuItem('chocolate', .524, 1.567)
        stand.add_menu_item(item1)
        day0 = {
            'chocolate': 5
        }
        stand.enter_sales_for_today(day0)
        profit = stand.total_profit_for_menu_item('chocolate')
        self.assertAlmostEqual(profit, 5*(1.567-0.524))

    def test4(self):
        """Tests get_sales_dict_for_day"""
        stand = lemon.LemonadeStand('Woo Lemons')
        item1 = lemon.MenuItem('lemonade', .5, 1.5)
        stand.add_menu_item(item1)
        day0 = {
            'lemonade': 5
        }
        stand.enter_sales_for_today(day0)
        self.assertIs(stand.get_sales_dict_for_day(0), day0)

    def test5(self):
        """Tests total profit for stand"""
        stand = lemon.LemonadeStand('Woo Lemons')
        item1 = lemon.MenuItem('lemonade', .5, 1.5)
        stand.add_menu_item(item1)
        day0 = {
            'lemonade': 5
        }
        day1 = {
            'lemonade': 10
        }
        stand.enter_sales_for_today(day0)
        stand.enter_sales_for_today(day1)
        profit = (10+5)*(1.5-0.5)
        self.assertEqual(stand.total_profit_for_stand(), profit)