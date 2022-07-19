# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 4, 2022
# Description: Records the menu items and daily sales of a lemonade stand. Calculates overall profit
# as well as individual item profits

class MenuItem:
    '''Create a class with Menu Item objects containing
     three private data members: name, wholesale cost and selling price'''
    def __init__(self, name, wholesale_cost, selling_price):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        '''Returns name of Menu Item'''
        return self._name

    def get_wholesale_cost(self):
        '''Returns wholesale cost of Menu Item'''
        return self._wholesale_cost

    def get_selling_price(self):
        '''Returns selling price of Menu Item'''
        return self._selling_price


class SalesForDay:
    '''Create a SalesForDay class representing sales for a particular day
    takes two parameters: the day (an integer) and a dictionary where keys are
    names of items sold and values are numbers sold that day'''
    def __init__(self, day, sales_dict):
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        '''Returns the day'''
        return self._day

    def get_sales_dict(self):
        '''Returns the sales dictionary described above'''
        return self._sales_dict


class InvalidSalesItemError(Exception):
    '''An exception for LemonadeStand class (raised when name of an item sold
    doesn't matchname of any MenuItem in the menu)'''
    pass


class LemonadeStand:
    '''Create a LemonadeStand class that has 4 data members:
    a str for the stand name,
    an integer representing the current day,
    a dictionary of MenuItem objects (keys are names of the items and values are the MenuItem objects)
    and a list of SalesForDay objects
    '''

    def __init__(self, name):
        self._name = name
        self.current_day = 0
        self.menu = {}
        self.sales_record = []

    def get_name(self):
        '''Returns the name of LemonadeStand'''
        return self._name

    def add_menu_item(self, item):
        '''Takes a MenuItem object and adds it to the menu dictionary'''
        menu_item = MenuItem.get_name(item)
        self.menu[menu_item] = item

    def enter_sales_for_today(self, items_sold):
        '''Takes a dictionary (keys are names of sold items and values are how many were sold)
        if the name of an item sold doesn't match the name of any MenuItem, it raises
        InvalidSalesItemErrror
        Otherwise, it creates a new SalesForDay object with the current day and the passed in dictionary
        and adds that object to the list of SalesForDay objects
        Increments the current day by 1'''
        for item in items_sold:
            if item not in self.menu:
                raise InvalidSalesItemError

        self.sales_record.append(SalesForDay(self.current_day, items_sold))
        self.current_day = self.current_day + 1

    def get_sales_dict_for_day(self, day):
        '''takes a day (as an integer) and returns the dictionary of sales for that day'''
        for date in self.sales_record:
            if date.get_day() == day:
                return date.get_sales_dict()

    def total_sales_for_menu_item(self, item_name):
        """Takes the name of a menu item and returns the total number of
        that item sold over the entire history of the stand"""
        total_sold = 0
        for sold_item in self.sales_record:
            total_sold += sold_item.get_sales_dict()[item_name]
        return total_sold

    def total_profit_for_menu_item(self, item_name):
        """Takes the name of a menu item and returns the total profit on that
        item over the history of the stand (takes entire revenue and subtracts out wholesale cost)"""
        revenue = self.total_sales_for_menu_item(item_name) * self.menu[item_name].get_selling_price()
        wholesale_total = self.total_sales_for_menu_item(item_name) * self.menu[item_name].get_wholesale_cost()
        total_item_profit = revenue - wholesale_total
        return total_item_profit

    def total_profit_for_stand(self):
        '''Takes no parameters and returns the total profit on all items sold
        over the history of the stand'''
        total = 0
        for all_sold in self.menu:
            total += self.total_profit_for_menu_item(all_sold)
        return total

def main():
    '''A main function that runs if file is run as a script. The main fuction:
    Creates a LemonadeStand object
    Creates 2 MenuItem objects and adds them to the LemonadeStand's menu
    Creates a dictionary of sales for the day that includes one item that isn't on the menu
    Tries calling enter_sales_for_today(), passing that dictionary as the argument
    An InvalidSalesItem function is raied that is caught by try/except and prints out an explanatory message'''
    stand = LemonadeStand('I Like Lemons')
    item1 = MenuItem('lemonade', .5, 1.5)
    stand.add_menu_item(item1)
    item2 = MenuItem('cookie', .2, 1)
    stand.add_menu_item(item2)
    day0 = {
        'lemonade': 5,
        'cookie': 2,
        'soda': 1,
     }
    try:
        stand.enter_sales_for_today(day0)
    except InvalidSalesItemError:
        print("An item entered does not exist")


if __name__ == "__main__":
    main()
