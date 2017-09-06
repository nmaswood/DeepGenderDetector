import csv
from enum import Enum
import os
import numpy as np
from os import listdir
import os.path
import pandas as pd

class Person():

    """
    Struct representing name, gender count
    """
    str_to_int = {"male": 0, "female": 1, "unknown": 2}
    int_to_str = {v:k for k,v in str_to_int.items()}

    def __init__(self, name):
        self.name = name
        self.male = 0
        self.female = 0
        self.unk = 0
        self.nan = 0

    def __repr__(self):

        return f'{self.name}|M:{self.male},F:{self.female}'

    def __hash__(self):
        return hash(self.name)

    def update(self, gender):

        if gender == "male":
            self.male += 1
        elif gender == "female":
            self.female += 1
        elif gender == "unknown":
            self.unk  +=1
        else:
            self.nan += 1

    def to_tuple(self):

        return (self.name,self.male, self.female, self.unk, self.nan)

    @staticmethod
    def select_first_name(full_name):
        lowered = full_name.lower()
        splat = lowered.split()
        return splat[0].strip().strip("'")


class People():

    """
    A struct that builds a list of all unique people and their names
    """

    def __init__(self):

        self.people = {}

    def __repr__(self):

        return f'{len(self.people)} unique names'

    def add(self, name, gender):

        """

        Creates or updates a person struct

        """

        first_name = Person.select_first_name(name)

        if first_name not in self.people:
            person = Person(first_name)
            self.people[first_name] = person
        else:
            person = self.people.get(first_name)

        person.update(gender)

        return person

    def to_csv(self):
        if not self.people:
            print ("Your people dict is empty bro")
            return

        as_list = sorted([v.to_tuple() for k, v in self.people.items() ],key = lambda x:x[0])

        with open("_people.csv", "w") as outfile:
            writer = csv.writer(outfile)

            writer.writerow(['name', 'male', 'female'])

            for name, male, female, _, _ in as_list:

                writer.writerow([name, male, female])

    @staticmethod
    def read():

        """

        Reads all people from disk and returns it as a populated people struct

        """

        if os.path.isfile("_people.csv"):
            return pd.read_csv("_people.csv")

        if not os.path.isfile("people.csv"):
            raise Exception("Hmmm looks like you don't have the original data contact Nasr Maswood for the data directly")

        people_data = pd.read_csv('people.csv')
        people_data = people_data.dropna(how = 'any')

        names = people_data['name'].tolist()
        genders = people_data['gender'].tolist()

        zipped = list(zip(names,genders))

        people = People()

        for name, gender in zipped:
            people.add(name, gender)

        people.to_csv()

if __name__ == "__main__":
    people = People.read()
