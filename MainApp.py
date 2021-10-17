
import Person

## importing another module from a parent folder
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
 
from textDataBase import DatabaseManager
##

database = DatabaseManager.CreateTextDatabase(2)

repeatInfinitely = True
while repeatInfinitely == True:
	name = input("\n\nPerson's name -> ")
	securityCode = input("Person's security code -> ")
	gender = input("Person's gender -> ")
	address = input("Person's address -> ")

	personOne = Person.Person(name, securityCode, gender, address)
	personOne.showBasicInformations()
	
	try:
		database.saveObjectContent(personOne)
	except Exception as ex:
		print(ex)