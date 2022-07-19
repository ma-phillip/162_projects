# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 10, 2022
# Description: A library simulator that tracks items in the library as well as its patrons. Keeps track of
# how long items have been checked out for and fines owed by patrons.

class LibraryItem:
    """Creates a class with LibraryItem objects containing a unique library ID, a title, a
    location for the item, who checked out the item, who requested the item,
    and when it was checked out"""

    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._location = "ON_SHELF"
        self._date_checked_out = 0

    def get_location(self):
        """Returns location for a Library Item"""
        return self._location

    def get_library_item_id(self):
        """Returns a unique identifier for a Library Item"""
        return self._library_item_id

    def set_checked_out_by(self, member):
        """Sets a new check out member"""
        self._checked_out_by = member

    def set_date_checked_out(self, date):
        """Sets a new date for check out"""
        self._date_checked_out = date

    def set_location(self, new_location):
        """Sets a new location for Library Item"""
        self._location = new_location

    def get_requested_by(self):
        """Returns who requested an item"""
        return self._requested_by

    def set_requested_by(self, new_request):
        """Sets a new requester"""
        self._requested_by = new_request

    def get_checked_out_by(self):
        """Returns who checked out an item"""
        return self._checked_out_by

    def get_date_checked_out(self):
        """Returns the date item got checked out"""
        return self._date_checked_out


class Book(LibraryItem):
    """Create a book class that inherits from LibraryItem, contains an additional string field for author"""

    def __init__(self, library_item_id, title, author):
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._location = "ON_SHELF"
        self._date_checked_out = 0
        self._check_out_length = 21
        self._author = author

    def get_check_out_length(self):
        """Returns check out length for book"""
        return self._check_out_length

    def get_author(self):
        """Returns author of book"""
        return self._author


class Album(LibraryItem):
    """Create a album class that inherits from LibraryItem, contains an additional string field for artist"""

    def __init__(self, library_item_id, title, artist):
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._location = "ON_SHELF"
        self._date_checked_out = 0
        self._check_out_length = 14
        self._artist = artist

    def get_check_out_length(self):
        """Returns check out length for album"""
        return self._check_out_length

    def get_artist(self):
        """Returns artist of album"""
        return self._artist


class Movie(LibraryItem):
    """Create a movie class that inherits from LibraryItem, contains an additional string field for director"""

    def __init__(self, library_item_id, title, director):
        self._library_item_id = library_item_id
        self._title = title
        self._checked_out_by = None
        self._requested_by = None
        self._location = "ON_SHELF"
        self._date_checked_out = 0
        self._check_out_length = 7
        self._director = director

    def get_check_out_length(self):
        """Returns check out length for movie"""
        return self._check_out_length

    def get_director(self):
        """Returns director of movie"""
        return self._director


class Patron:
    """Create a class Patron containing a unique identifier, a name, a list of checked out items, and
    the amount a patron owes in late fines in dollars"""

    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0.0

    def get_fine_amount(self):
        """Returns the amount a patron owes in fines """
        return self._fine_amount

    def add_library_item(self, added_item):
        """Adds an item to the list of checked out items"""
        self._checked_out_items.append(added_item)

    def remove_library_item(self, removed_item):
        """Removes an item from the list of checked out items"""
        self._checked_out_items.remove(removed_item)

    def amend_fine(self, fine):
        """Increases or decreases the fine amount"""
        self._fine_amount += fine

    def get_patron_id(self):
        """Returns the patron's id number"""
        return self._patron_id

    def get_checked_out_item(self):
        """Returns list of checked out items"""
        return self._checked_out_items


class Library:
    """Create a class Library that contains a holdings list (a collection of items that belong to the library),
    a members list (a collection of patrons that are members of the library), and the number of days since the
    library was created"""

    def __init__(self):
        self._holdings = []
        self._members = []
        self._current_date = 0

    def add_library_item(self, item):
        """Adds a library item to the holdings list"""
        self._holdings.append(item)

    def add_patron(self, member):
        """Adds a patron to the members list"""
        self._members.append(member)

    def get_current_date(self):
        """Returns current date of library"""
        return self._current_date

    def lookup_library_item_from_id(self, item_id):
        """Takes an item ID parameter, looks in list of holdings to either return a LibraryItem object
        that corresponds to the item ID or None"""
        for items in self._holdings:
            if items.get_library_item_id() == item_id:
                return items
            continue  # continues looking through list of holdings
        return None

    def lookup_patron_from_id(self, patron_id):
        """Takes a patron ID parameter, looks in list of patrons to either return a Patron object
        that corresponds to the patron ID or none"""
        for members in self._members:
            if members.get_patron_id() == patron_id:
                return members
            continue  # continues looking through list of members
        return None

    def check_out_library_item(self, patron_id, item_id):
        """Takes a patron ID and item ID, looks through members list to see if the corresponding patron is in there,
        and looks through holdings list to see if corresponding item is in there. Then it checks the corresponding item's
        location to make sure it isn't checked out and checks the items hold status to check it isn't being
        held for another patron. If all these conditions are met, the item's checked out date is updated to
        the current date, the item's hold request is updated, the patron's checked out items are updated and
        returns check out successful"""
        for members in self._members:
            if members.get_patron_id() == patron_id:  # check for corresponding member id
                for item in self._holdings:
                    if item.get_library_item_id() == item_id:  # check for corresponding item id
                        if item.get_location() == "ON_HOLD_SHELF":  # if item is being held for somebody
                            if item.get_requested_by() == patron_id:  # if item is being held for the same patron, check out
                                item.set_checked_out_by(members)
                                item.set_date_checked_out(self._current_date)
                                item.set_location("CHECKED_OUT")
                                members.add_library_item(item)
                                if item.get_requested_by() is not None:
                                    item.set_requested_by(None)
                                return 'check out successful'
                            else:  # item is being held for somebody else
                                return "item on hold by other patron"
                        elif item.get_location == "CHECKED_OUT":  # item is already checked out
                            return "item already checked out"
                        else:
                            item.set_checked_out_by(members)
                            item.set_date_checked_out(self._current_date)
                            item.set_location("CHECKED_OUT")
                            members.add_library_item(item)
                            if item.get_requested_by() is not None:
                                item.set_requested_by(None)
                            return 'check out successful'
                    continue  # continue looking through items list
                return 'item not found'
            continue  # continue looking through members list
        return "patron not found"

    def return_library_item(self, item_id):
        """Takes an item id and checks if it is in holdings list. If it is, checks if it is checked out or not.
        If it is checked out, updates the Patron's checked out items, the item's location, and the checked out by and
        returns a success. Otherwise, returns 'item already in library'"""
        for item in self._holdings:
            if item.get_library_item_id() == item_id:
                if item.get_location() == "CHECKED_OUT":  # if item is checked out
                    patron = item.get_checked_out_by()
                    patron.remove_library_item(item)
                    if item.get_requested_by() is None:  # if the item hasn't been requested
                        item.set_location("ON_SHELF")
                        item.set_checked_out_by(None)
                        return "return successful"
                    else:
                        item.set_location("ON_HOLD_SHELF")  # if the item has been requested
                        item.set_checked_out_by(None)
                        return "return successful"
                    continue
                return "item already in library"
            continue
        return "item not found"

    def request_library_item(self, patron_id, item_id):
        """Takes a patron id and item id, makes sure they both exist in both members and holdings list
        and then it checks that the item isn't on hold for somebody else. If these conditions are met,
        it updates the request status of the item with the patron id"""
        for member in self._members:
            if member.get_patron_id() == patron_id:
                for item in self._holdings:
                    if item.get_library_item_id() == item_id:
                        if item.get_requested_by() is None:  # if nobody has requested the item
                            item.set_requested_by(patron_id)
                            if item.get_location() == "ON_SHELF":
                                item.set_location("ON_HOLD_SHELF")
                                return "request successful"
                            else:
                                return "request successful"
                        else:  # somebody has already requested the item
                            return "item already on hold"
                    continue
                return "item not found"
            continue
        return "patron not found"

    def pay_fine(self, patron_id, paid_amount):
        """Takes a patron id and an amount paid in dollars and checks if patron id exists in members.
        If it exists, updates the patron's fine amount by the paid amount"""
        for member in self._members:
            if member.get_patron_id() == patron_id:
                member.amend_fine(-paid_amount)
                return "payment successful"
            continue
        return "patron not found"

    def increment_current_date(self):
        """Increments the current date and checks to see if a patron has overdue items. If they do,
        add 10 cents for each overdue item"""
        self._current_date += 1
        for member in self._members:
            for item in member.get_checked_out_item():
                overdue_length = self._current_date - item.get_date_checked_out()
                if overdue_length > item.get_check_out_length():
                    member.amend_fine(0.10)