from datetime import date

class Swimmer:
	def __init__(self, firstName, lastName, birthday, isMale):
		self.firstName = firstName.capitalize()
		self.lastName = lastName.capitalize()
		self.birthday = birthday
		self.div = 0
		self.isMale = isMale
		self.swimmerID = None
	
	def __repr__(self):
		fn = self.firstName
		ln = self.lastName
		birthday = str(self.birthday)
		gender = 'Female'
		if self.isMale:
			gender = 'Male'
		div = self.div
		return '%s%s%s%s%s' % (fn,ln,birthday,gender,div)
	
	def __str__(self):
		return self.__repr__()
	
	def setDiv(self, div):
		self.div = div
	
	def getBirthday(self):
		return self.birthday
	
	def getSwimmerID(self):
		if self.swimmerID is None:
			return ''
			
		return self.swimmerID

	def setSwimmerID(self, SIDString):
		self.swimmerID = SIDString
	
	def isLesserLastName(self, other):
		if self.lastName < other.lastName:
			return True
		else:
			return False

	def isLesserFirstName(self, other):
		if self.firstName < other.firstName:
			return True
		else:
			return False
	
	def isYongerThan(self, other):
		if self.birthday < other.birthday:
			return True
		else:
			return False
	