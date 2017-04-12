import csv
from enum import Enum
import os
from os import listdir
import os.path

class Person():

    """
    Struct representing name, gender tuple
    """

    str_to_int = {"male": 0, "female": 1, "unknown": 2}
    int_to_str = {v:k for k,v in str_to_int.items()}

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __repr__(self):

        return f'{self.name}:{self.gender}'

class People():

    """
    A struct that builds a list of all unique people and their names
    """

    def __init__(self):

        self.people = set()
        self.names = set()

    def __repr__(self):

        return f'{len(self.people)} unique names'

    def add(self, name, gender):

        """

        Saves a name, gender as a person if it is unique

        """

        if name in self.names:
            return 0

        self.names.add(name)

        new_person = Person(name, gender)
        self.people.add(new_person)

        return 1

    @staticmethod
    def _collect_data():
        """
        Process the intial data files and extracts name and gender
        """

        people = People()

        def read_csvs():

            dirs = ("imdb/2006/actors", "imdb/2015/actors")

            for _dir in dirs:
                for filename in listdir(_dir):

                    with open(_dir + "/" + filename, 'r') as infile:

                        csvreader = csv.reader(infile)
                        next(csvreader)

                        for line in csvreader:

                            name = line[0]
                            gender = line[1]
                            people.add(name, gender)
        read_csvs()
        people._write()


    def _write(self):

        """

        Writes people struct to disk

        """

        with open("people.csv", 'w') as outfile:

            writer = csv.writer(outfile)

            writer.writerow(["name", "gender"])

            for person in self.people:

                name, gender = person.name, person.gender

                writer.writerow([name, gender])

    @staticmethod
    def read():

        """

        Reads all people from disk and returns it as a populated people struct

        """

        if not os.path.isfile("people.csv"):

            if not os.path.isdir("imdb"):

                raise Exception("Hmmm looks like you don't have the original data contact Nasr Maswood for the data directly")
            else:
                People._collect_data()

        p = People()

        with open("people.csv", "r") as infile:

            reader = csv.reader(infile)
            next(reader)

            for name, gender in reader:

                p.add(name, gender)

        return p

if __name__ == "__main__":
    people = People.read()
    print (people)
