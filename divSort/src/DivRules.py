from datetime import date

from src import Swimmer

class DivRules:
	def __init__(self):
		self.__divNOldest = [date.today()]*7
	
	def __repr__(self):
		retStr = ""
		cnt = 1
		for line in self.__divNOldest:
			retStr += ('%s-%s\n' % (cnt,str(line)))
			cnt += 1
		return retStr
	
	def __str__(self):
		return self.__repr__()
	
	def __checkDivRange(self, div):
		if div < 1:
			error = RuntimeError()
			error.add_note('Input div can not be less than one.')
			raise error
		if div > 7:
			error = RuntimeError()
			error.add_note('Input div can not be more than than seven.')
			raise error
		
	def __checkDateObject(self, dateObject):
		if not(type(dateObject) is date):
			error = RuntimeError()
			error.add_note('Input Div rule date is not a datetime.date object.')
			raise error			
	
	def setDivNOldest(self, div, dateObject):
		self.__checkDivRange(div)
		self.__checkDateObject(dateObject)
		div = div - 1 
		
		self.__divNOldest[div] = date(dateObject.year, dateObject.month, dateObject.day)
		
	def returnSwimmerDiv(self, swimmer):
		divIndx = 1
		for div in self.__divNOldest:
			if swimmer.getBirthday() >= div:
				return divIndx
			else:
				divIndx += 1
		
		return 8
	