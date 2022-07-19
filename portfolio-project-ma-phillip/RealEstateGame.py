# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: May 31, 2022
# Description: Contains a RealEstateGame class which allows two or more players to play a simplified version
# of Monopoly
class RealEstateGame:
    """A class that contains 4 dictionaries and a list to keep track of the game"""

    def __init__(self):
        self._player_position = {}  # empty dictionary to keep track of player positions
        self._player_account = {}  # empty dictionary to keep track of player account
        self._spaces_and_owned = {}  # empty dictionary to keep track of all spaces and who they are owned by
        self._spaces_and_rent = {}  # empty dictionary to keep track of all spaces and their rent value
        self._list_of_players = []  # empty list to keep track of all players

    def get_spaces_and_owned(self):
        """Get method that returns all spaces and their owner status"""
        return self._spaces_and_owned

    def get_list_of_players(self):
        """Get method for the list of players"""
        return self._list_of_players

    def add_to_list_of_players(self, player):
        """Adds a player to the list of players"""
        self._list_of_players.append(player)

    def set_spaces_and_owned(self, space, owned):
        """Set method taking a space and owner parameter. Updates the owner status of that space"""
        self._spaces_and_owned[space] = owned

    def set_spaces_and_rent(self, space, rent):
        """Set method taking a space and rent parameter. Updates the rent value for a space"""
        self._spaces_and_rent[space] = rent

    def set_player_position(self, player, position):
        """Set method taking a player and position parameter. Updates the position for a player"""
        self._player_position[player] = position

    def set_player_account(self, player, amount):
        """Set method taking a player and amount parameter. Updates the amount a player has"""
        self._player_account[player] = amount

    def get_is_owned_by(self, space):
        """Get method that returns all spaces and the owner status"""
        return self._spaces_and_owned[space]

    def rec_create_spaces(self, rent_values, initial_value):
        """Takes a list of 24 numbers as rent values. Creates 24 spaces in the two space dictionaries and
        adds rent and sets their owner status to None"""
        if initial_value == 25:
            return
        else:
            self.set_spaces_and_rent(initial_value, rent_values[initial_value - 1])
            self.set_spaces_and_owned(initial_value, None)
            self.rec_create_spaces(rent_values, initial_value + 1)

    def create_spaces(self, go_amount, rent_values):
        """Helper value so the user only has to input the go amount and rent values. Creates space 0 (go) in the
        two space dictionaries. Adds go value and initializes the owner status to None"""
        initial_value = 1
        self.set_spaces_and_rent(0, go_amount)
        self.set_spaces_and_owned(0, None)
        self.rec_create_spaces(rent_values, initial_value)

    def remove_owned_by(self, player, pos):
        """Recursively sets all spaces owned by a player to None (when they have no money left)"""
        if pos == 25:
            return
        if self.get_is_owned_by(pos) == player:
            self.set_spaces_and_owned(pos, None)
            self.remove_owned_by(player, pos + 1)
        else:
            self.remove_owned_by(player, pos + 1)

    def create_player(self, name, initial_balance):
        """Takes a name and balance as parameter. Sets the players position to 0 and sets their account value
        to the balance. Adds their name to the list of players"""
        self.set_player_account(name, initial_balance)
        self.set_player_position(name, 0)
        self.add_to_list_of_players(name)

    def get_player_account_balance(self, name):
        """Get method that returns a player's balance"""
        return self._player_account[name]

    def get_player_current_position(self, name):
        """Get method that returns a player's position"""
        return self._player_position[name]

    def get_purchase_price(self, space):
        """Get method that returns a space's purchase price (5x the rent price)"""
        return self._spaces_and_rent[space] * 5

    def get_rent_amount(self, space):
        """Get method that returns a space's rent amount"""
        return self._spaces_and_rent[space]

    def get_go_amount(self):
        """Get method that returns go amount"""
        return self._spaces_and_rent[0]

    def buy_space(self, name):
        """Takes a name and checks that their current position is not currently owned and that they are not on go.
        Also checks that they have enough money to purchase the space. If they do, their account is deducted the
        purchase price and the position is set to be owned by them. Returns True if successfully purchased.
        False if otherwise. """
        position = self.get_player_current_position(name)
        purchase_price = self.get_purchase_price(position)
        account_balance = self.get_player_account_balance(name)
        new_balance = account_balance - purchase_price
        if self.get_is_owned_by(position) is None and account_balance > purchase_price and position != 0:
            self.set_player_account(name, new_balance)
            self.set_spaces_and_owned(position, name)
            return True
        else:
            return False

    def move_player(self, name, spaces_moved):
        """Takes a player and the number of spaces moved as a parameter. If they have no money, returns without doing anything.
        If the player passes or lands on go, the go amount is added to their balance. If the new position is a space owned,
        by another player, rent is paid to the owner and the amount is deducted from the player's account. If the rent
        amount is more than the player's current balance, their balance is set to 0, their money is added to the owner's
        balance and their owned properties are surrendered and set to None.
        """
        current_position = self.get_player_current_position(name)
        if self.get_player_account_balance(name) == 0:
            return
        if current_position + spaces_moved < 25:  # if they are not going to pass go
            new_position = spaces_moved + current_position
            self.set_player_position(name, new_position)
            if self.get_is_owned_by(new_position) is not None and self.get_is_owned_by(new_position) != name:
                if self.get_player_account_balance(name) > self.get_rent_amount(new_position):  # if account is
                    # greater than rent owned
                    new_balance = self.get_player_account_balance(name) - self.get_rent_amount(new_position)
                    self.set_player_account(name, new_balance)
                    owner = self.get_is_owned_by(new_position)
                    owner_new_balance = self.get_player_account_balance(owner) + self.get_rent_amount(new_position)
                    self.set_player_account(owner, owner_new_balance)
                if self.get_player_account_balance(name) - self.get_rent_amount(new_position) <= 0:  # if player
                    # doesn't have enough to pay rent
                    balance = self.get_player_account_balance(name)
                    self.set_player_account(name, 0)
                    self.remove_owned_by(name, 1)
                    owner = self.get_is_owned_by(new_position)
                    owner_new_balance = self.get_player_account_balance(owner) + balance
                    self.set_player_account(owner, owner_new_balance)
        if current_position + spaces_moved == 25:  # if the player is landing on go
            self.set_player_position(name, 0)
            new_account_amount = self.get_player_account_balance(name) + self.get_go_amount()  # add go amount
            self.set_player_account(name, new_account_amount)
        if current_position + spaces_moved > 25:  # if the player is passing go
            new_position = current_position + spaces_moved - 25
            self.set_player_position(name, new_position)
            new_account_amount = self.get_player_account_balance(name) + self.get_go_amount()
            self.set_player_account(name, new_account_amount)
            if self.get_is_owned_by(new_position) is not None and self.get_is_owned_by(new_position) != name:
                if self.get_player_account_balance(name) > self.get_rent_amount(new_position):  # if account is
                    # greater than rent owned
                    new_balance = self.get_player_account_balance(name) - self.get_rent_amount(new_position)
                    self.set_player_account(name, new_balance)
                    owner = self.get_is_owned_by(new_position)
                    owner_new_balance = self.get_player_account_balance(owner) + self.get_rent_amount(new_position)
                    self.set_player_account(owner, owner_new_balance)
                if self.get_player_account_balance(name) - self.get_rent_amount(new_position) <= 0:
                    balance = self.get_player_account_balance(name)
                    self.set_player_account(name, 0)
                    self.remove_owned_by(name, 1)
                    owner = self.get_is_owned_by(new_position)
                    owner_new_balance = self.get_player_account_balance(owner) + balance
                    self.set_player_account(owner, owner_new_balance)

    def check_game_over(self):
        """Checks all players accounts and returns the winner if only one player has more than 0 dollars.
        Otherwise returns an empty string"""
        players = self.get_list_of_players()
        winner = ""
        counter = 0
        for player in players:
            if self.get_player_account_balance(player) > 0:
                counter += 1
                winner = player
        if counter == 1:
            return winner
        else:
            return ""
