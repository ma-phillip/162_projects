# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 17, 2022
# Description: Creates a class NeighborhoodPets that can add a pet, delete a pet, and search
# for owners of a pet. It can save and load the data to a JSON file. Can also get a set of species.
import json


class DuplicateNameError(Exception):
    """An error to be raised for duplicate name"""
    pass


class NeighborhoodPets:
    def __init__(self):
        """Creates a private data member that is an empty dictionary"""
        self._pet_dict = {}

    def add_pet(self, pet_name, pet_species, owner_name):
        """Takes a pet name, a pet species, and owner name as parameters and
        adds them to the pet dictionary. If the name in the dictionary exists already,
        it raises a DuplicateNameError"""
        if pet_name in self._pet_dict:
            raise DuplicateNameError
        else:
            self._pet_dict[pet_name] = {"Pet Name": pet_name,
                                        "Pet Species": pet_species,
                                        "Pet Owner": owner_name}

    def get_pet_dict(self):
        """Returns the pet dictionary"""
        return self._pet_dict

    def delete_pet(self, pet_name):
        """Takes a pet name and deletes it from the pet dictionary"""
        del self._pet_dict[pet_name]

    def get_owner(self, pet_name):
        """Takes a pet name and returns the owner of the pet"""
        return self._pet_dict[pet_name]["Pet Owner"]

    def save_as_json(self, file_name):
        """Takes a .JSON file name and writes the pet dictionary to that file"""
        with open(file_name, 'w') as outfile:
            json.dump(self._pet_dict, outfile)

    def read_json(self, file_name):
        """Loads a .JSON file containing a pet dictionary and replaces the current
        pet dictionary"""
        with open(file_name, 'r') as infile:
            self._pet_dict = json.load(infile)

    def get_all_species(self):
        """Returns a set of the species of all pets"""
        all_species = {pet["Pet Species"] for pet in self._pet_dict.values()}
        return all_species
