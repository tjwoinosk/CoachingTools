import pathlib
import os

from datetime import date

from src import SwimmerHandler as SH
from src import Swimmer as SW


class SwimmerReaderBase:
	def __init__(self, file):
		self.__fileLocation = file
		self.listOfCSVLines = []
		
	def read(self):
		p = pathlib.Path(self.__fileLocation)
		
		f = open(p.absolute(), 'r')
		for line in f:
			 self.listOfCSVLines.append(line)
		f.close()
		
		self.parse()
	
	def parse(self):
		pass
		
		
class SwimmerReader(SwimmerReaderBase):
	
	def __init__(self, file):
		SwimmerReaderBase.__init__(self, file)
		self.__swimmerHandlerObject = SH.SwimmerHandler()
	
	def returnSwimmerObject(self):
		return self.__swimmerHandlerObject

	def __monthDayYearStrToDate(self, intputString):
		dateList = intputString.split('/')
		month = int(dateList[0])
		day = int(dateList[1])
		year = int(dateList[2])
		return date(year,month,day)

	def __yearMonthDayStrToDate(self, intputString):
		dateList = intputString.split('-')
		year = int(dateList[0])
		month = int(dateList[1])
		day = int(dateList[2])
		return date(year,month,day)

	def __parseLineToSwimmer(self, inputLine):
		inputLine = inputLine.strip()
		inputLineList = inputLine.split(',')
		
		if not(len(inputLineList) ==  20):
			return None
		
		if inputLineList == '':
			return None
		
		if 'reg' in inputLineList[0].lower():
			return None
		
		fn = inputLineList[5].split(' ')[0]
		ln = inputLineList[6].split(' ')[0]
		
		isMale = True
		if 'fe' in inputLineList[8].lower():
			isMale = False
			
		birthday = self.__yearMonthDayStrToDate(inputLineList[9])
		
		retSwimmer = SW.Swimmer(fn,ln,birthday,isMale)
		
		return retSwimmer
	
	def parse(self):
		for line in self.listOfCSVLines:
			tempSwimmer = self.__parseLineToSwimmer(line)
			if tempSwimmer is None:
				continue
			self.__swimmerHandlerObject.addSwimmer(tempSwimmer)
	