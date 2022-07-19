# Author: Phillip Ma
# GitHub username: ma-phillip
# Date: April 17, 2022
# Description: Opens sat.json, takes a list of DBNs as a variable and writes the corresponding
# data to a csv file
import json


class SatData:
    def __init__(self):
        """Opens sat.json and assigns the data in it to a private member"""
        with open('sat.json', 'r') as all_sat_data:
            sat_data = json.load(all_sat_data)['data']
        self._data = sat_data

    def save_as_csv(self, list_of_dbns):
        """Sorts the given list of DBNs to be descending. Checks for corresponding DBNs in
        sat.json and writes that data to a csv file"""
        list_of_dbns.sort(reverse=True)

        with open('output.csv', 'w') as outfile:
            outfile.write("DBN,School Name,Number of Test Takers,"
                          "Critical Reading Mean,Mathematics Mean,Writing Mean" + "\n")
            for i in self._data:
                if i[8] in list_of_dbns:
                    outfile.write(i[8] + ',')
                    if "," in i[9]:  # checks for commas and gives double quotes if there are any
                        outfile.write('"' + i[9] + '"' + ',')
                    else:
                        outfile.write(i[9] + ',')
                    outfile.write(i[10] + ',' + i[11] + ',' + i[12] + ',' + i[13] + '\n')
