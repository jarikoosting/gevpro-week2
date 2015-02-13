#!/opt/local/bin/python3.4

import sys

class Country():

    """ Return name of a country """

    def __init__(self, country):
        self.country = country

    def getCountry(self):
        return self.country

    def __str__(self):
        return "Hello from {}".format(self.country)


def main(argv):

    if len(argv) == 2:
        getCountry = Country(argv[1])
        print(getCountry)

    else:
        print("Wrong command given.")

if __name__ == "__main__":
    main(sys.argv)
