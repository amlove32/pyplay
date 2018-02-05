#!/usr/bin/env python3

# This script will download first and last name data files, clean
# and manipulate them in such a way to be usable by, for example,
# a PowerShell script to create many Active Directory and matching
# Exchange objects for quick development environmment builds.

import requests

firstNameUrl = requests.get("http://deron.meranda.us/data/census-derived-all-first.txt")
lastNameUrl = requests.get("http://deron.meranda.us/data/census-dist-2500-last.txt")

# Functions
def buildNameList(sourceFile):
    """ Expects a messy source file
        and returns a cleaned up list of names. """
    print("Getting the source file.")
    namesByLine = sourceFile.text.splitlines()[:2000]
    print("Cleaning up the data.")
    nameList = [name.split()[0].title() for name in namesByLine]
    return nameList

def buildUsername(firstName, lastName):
    """ Creates a username based on first and last name given. """
    username = str(firstName[:1] + lastName).lower()
    return username

def buildUsernameList(firstList, lastList):
    """ Expects a list of first names and a list of last names,
        concats them, then returns list of usernames. """
    names = list(zip(lastList, firstList))
    usernameList = []
    print("Building usernames from the first and last names.")
    for name in names:
        username = buildUsername(name[1], name[0])
        usernameList.append(username)
    return usernameList

# The script runner.
# TODO: Add try/catch/fail for the source file variables. Test with HTTP response codes.
firstNameList = buildNameList(firstNameUrl)
print("Data list 1... ready.")
lastNameList = buildNameList(lastNameUrl)
print("Data list 2... ready.")
usernameList = buildUsernameList(firstNameList, lastNameList)
print("Data list 3... ready.")
names = list(zip(lastNameList, firstNameList, usernameList))
print("Concatenated 3 data sets, throwing them into comma delimited text file.")
with open("allThePeoples.txt","a") as f:
    f.write("lastname,firstname,username")
    for name in names:
        f.write("\n" + ','.join(name))
        print("Adding {0} to file".format(name))
    print("Should be done.  Check the file - allThePeoples.txt")
