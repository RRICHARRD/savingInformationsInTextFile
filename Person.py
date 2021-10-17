
class Person:
	def __init__(self, name, securityCode, gender, address):
		self.informations = {
			'Name': name,
			'SecurityCode': securityCode,
			'Gender': gender,
			'Address': address
		}
		

	def showBasicInformations(self):
		for key in self.informations:
			print(key, ':', self.informations[key])