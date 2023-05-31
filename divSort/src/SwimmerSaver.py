import pathlib
import os

from src import SwimmerHandler as SH
from src import Swimmer

G_seperate = ',,,,\n'

class SwimmerSaverBase:
	def __init__(self, resDir, fileName):
		self.__resDir = resDir
		self.__fileName = fileName
		self.listOfCSVLines = []
		
	def save(self):
		pTemp = os.path.join(self.__resDir, self.__fileName)
		p = pathlib.Path(pTemp)
		
		self.formatData()
		
		f = open(p.absolute(), 'w')
		for line in self.listOfCSVLines:
			if line is None:
				continue
			f.write(line)
		f.close()
	
	def formatData(self):
		pass
		
		
class SwimmerSaver(SwimmerSaverBase):
	
	def __init__(self, resDir, fileName):
		SwimmerSaverBase.__init__(self, resDir, fileName)
		self.__swimmerHandlerObject = SH.SwimmerHandler()
	
	def register(self, swimmerHandlerObject):
		self.__swimmerHandlerObject = swimmerHandlerObject
	
	def __createCSVLineFromSwimmer(self, swimmerObject):
		if swimmerObject.isMale:
			gender = 'Male'
		else:
			gender = 'Female'
		
		fn = swimmerObject.firstName
		ln = swimmerObject.lastName
		dob = str(swimmerObject.birthday)
		div = swimmerObject.div
		
		line = '%s,%s,%s,%s,%s\n' % (fn, ln, gender, dob, div)
		return line
	
	def __sortSwimmersByLastName(self, swimmerList):
		swimmerList.sort(key = lambda x: x.lastName)

	def __sortSwimmersByFristName(self, swimmerList):
		swimmerList.sort(key = lambda x: x.firstName)

	def __sortSwimmersByAge(self, swimmerList):
		swimmerList.sort(key = lambda x: x.birthday)
	
	def formatData(self):
		self.listOfCSVLines.append('Athlete First Name,Athlete Last Name,Athlete Gender,Athlete DOB,Athlete Div\n')
		self.listOfCSVLines.append(G_seperate)
		
		for div in [1,2,3,4,5,6,7,8]:
			listOfGirls = self.__swimmerHandlerObject.getListOfDivNGirls(div)
			
			self.__sortSwimmersByLastName(listOfGirls)
			for sw in listOfGirls:
				self.listOfCSVLines.append(self.__createCSVLineFromSwimmer(sw))
			
			self.listOfCSVLines.append(G_seperate)
			
			listOfBoys = self.__swimmerHandlerObject.getListOfDivNBoys(div)
			self.__sortSwimmersByLastName(listOfBoys)
			for sw in listOfBoys:
				self.listOfCSVLines.append(self.__createCSVLineFromSwimmer(sw))
			
			if div < 8:
				self.listOfCSVLines.append(G_seperate)