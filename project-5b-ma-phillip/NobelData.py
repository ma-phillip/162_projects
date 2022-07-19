# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 17, 2022
# Description: Reads a json file containing Nobel Winner data and allows a user to search that data using year and category.
import json


class NobelData:
    def __init__(self):
        """Opens the nobels.json file and assigns the data to a private data member"""
        with open('nobels.json', 'r') as nobel_data:
            all_nobel_data = json.load(nobel_data)
        self._data = all_nobel_data

    def search_nobel(self, year, category):
        """Takes year and category as parameters, assigns the winners to a list, takes the winner surnames
        and adds it to a list, sorts the list alphabetically, and returns the list"""
        winner_surnames =[]
        for i in range(0, len(self._data['prizes'])):
            if self._data['prizes'][i]['year'] == year and self._data['prizes'][i]['category'] == category:
                winners = self._data['prizes'][i]['laureates']
            continue

        for i in range(0, len(winners)):
            winner_surnames.append(winners[i]['surname'])

        for i in range(1, len(winner_surnames)):
            value = winner_surnames[i]
            pos = i - 1
            while pos >= 0 and winner_surnames[pos].lower() > value.lower():
                winner_surnames[pos + 1] = winner_surnames[pos]
                pos -= 1
            winner_surnames[pos + 1] = value

        return winner_surnames
