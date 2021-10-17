
import random
from pathlib import Path

class CreateTextDatabase:
	def __init__(self, maximumQuantityToSave):
		self.__database()
		self.listOfCreatedIds = []
		self.__maximumQuantityToSave = maximumQuantityToSave

	def __createNonRepeatableNumber(self): #only in memory
		randomNumber = random.randint(1, self.__maximumQuantityToSave)
		if randomNumber not in self.listOfCreatedIds:
			self.listOfCreatedIds.append(randomNumber)
			return randomNumber
		else: 
			return self.__createNonRepeatableNumber()

	def __createDatabaseFile(self):
		try:
			open('textDataBase/customers-database.txt', 'x')
			print("'customers-database.txt' was created sucessfully!")
		except:
			print('Something went wrong, because file was not created!')

	def __database(self):
		if not Path('textDataBase/customers-database.txt').is_file():
			self.__createDatabaseFile()
		else:
			print("Data base 'customers-database.txt' was not created because currently exists!")

	def __writeTopLayout(self):
		try:
			file = open('textDataBase/customers-database.txt', 'a')
			file.write('+--------------------------------------------------+') 
			file.write('\n')
			file.close()			
		except:
			print("Something went wrong when try to write in the 'customers-database.txt'")

	def __writeBottomLayout(self):
		try:
			file = open('textDataBase/customers-database.txt', 'a')	
			file.write('+--------------------------------------------------+')
			file.write('\n\n\n')
			file.close()
		except:
			print("Something went wrong when try to write in the 'customers-database.txt'")

	def __writeMiddleContents(self, words):
		try:
			file = open('textDataBase/customers-database.txt', 'a')
			file.write(words)
			file.close()
		except:
			print("Something went wrong when try to write in the 'customers-database.txt'")

	def __jumpOneLine(self):
		try:
			file = open('textDataBase/customers-database.txt', 'a')
			file.write('\n')
			file.close()
		except:
			print("Something went wrong when try to write in the 'customers-database.txt'")

	def saveObjectContent(self, personObject):
		try:
			uniqueId = str(self.__createNonRepeatableNumber())
		except:
			print("Sorry, you can't save anothers persons. Database is full!")
			print('Press Ctrl+c to stop program running')
		else:
			self.__writeTopLayout()
			self.__writeMiddleContents('id:')
			self.__writeMiddleContents(uniqueId)
			self.__jumpOneLine()

			for key in personObject.informations:
				self.__writeMiddleContents(key)
				self.__writeMiddleContents(':') 
				self.__writeMiddleContents(personObject.informations[key])
				self.__jumpOneLine()
			self.__writeBottomLayout()

	