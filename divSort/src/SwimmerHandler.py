from src import Swimmer as SW


class SwimmerHandler:
	def __init__(self):
		self.__listOfSwimmers = []
	
	def addSwimmer(self, swimmerIn):
		self.__listOfSwimmers.append(swimmerIn)
	
	def numberSwimmers(self):
		return len(self.__listOfSwimmers)
		
	def printList(self):
		for swim in self.__listOfSwimmers:
			print(swim)
	
	def getListOfDivNBoys(self, div):
		newList=[]
		for swim in self.__listOfSwimmers:
			if swim.isMale and swim.div == div:
				fn = swim.firstName
				ln = swim.lastName
				birthday = swim.birthday
				tmp = SW.Swimmer(fn,ln,birthday,True)
				tmp.setDiv(swim.div)
				newList.append(tmp)
		return newList
	
	def getListOfDivNGirls(self, div):
		newList=[]
		for swim in self.__listOfSwimmers:
			if not(swim.isMale) and swim.div == div:
				fn = swim.firstName
				ln = swim.lastName
				birthday = swim.birthday
				tmp = SW.Swimmer(fn,ln,birthday,False)
				tmp.setDiv(swim.div)
				newList.append(tmp)
		return newList
	
	def calculateDivs(self, divRulesObject):
		for swim in self.__listOfSwimmers:
			swim.div = divRulesObject.returnSwimmerDiv(swim)

	