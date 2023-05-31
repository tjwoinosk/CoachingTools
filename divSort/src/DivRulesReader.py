import pathlib
import os
from datetime import date

from src import DivRules as rules

class DivRulesReaderBase:
	def __init__(self,fileLocation):
		self.__fileLocation = pathlib.Path(fileLocation)
		self.__checkFile(self.__fileLocation)
		self.fileLines = []
		self.__loadFile()

	def __checkFile(self,fileLocation):
		if not(fileLocation.is_file()):
			error = RuntimeError()
			error.add_note('Input div rule file dose not exist.')
			raise error
		if not(fileLocation.suffix == '.txt'):
			error = RuntimeError()
			error.add_note('Input div rule file error. Expected a .txt file.')
			raise error
	
	def __loadFile(self):
		f = open(self.__fileLocation,'r')
		for line in f:
			self.fileLines.append(line)
		f.close()
	

class DivRulesReader(DivRulesReaderBase):
	
	def __readLine(self,inputLine):
		inputLine = inputLine.replace(" ", "")
		inputLine = inputLine.strip()
		inputLineList = inputLine.split(',')
		
		strDiv = inputLineList[0].split('-')[1]
		
		div = 0
		if strDiv.isnumeric():
			div = int(strDiv)
		else:
			return div, ''

		dateObject = date.fromisoformat(inputLineList[1]+'-01')
		
		return div, dateObject
	
	def returnRulesObject(self):
		returnRules = rules.DivRules()
		for line in self.fileLines:
			div, dateObject = self.__readLine(line)
			if div == 0:
				continue

			returnRules.setDivNOldest(div, dateObject)
		
		return returnRules
		
		