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

	def monthDayYearStrToDate(self, intputString):
		dateList = intputString.split('/')
		month = int(dateList[0])
		day = int(dateList[1])
		year = int(dateList[2])
		return date(year,month,day)

	def yearMonthDayStrToDate(self, intputString):
		dateList = intputString.split('/')
		year = int(dateList[0])
		month = int(dateList[1])
		day = int(dateList[2])
		return date(year,month,day)

	def parseLineToSwimmer(self, inputLine):
		inputLine = inputLine.strip()
		inputLineList = inputLine.split(',')
		
		if not(len(inputLineList) > 20):
			return None
		
		if inputLineList[1] == '':
			return None
		
		if 'reg' in inputLineList[1].lower():
			return None
		
		fn = inputLineList[6].split(' ')[0]
		ln = inputLineList[7].split(' ')[0]
		
		isMale = True
		if 'fe' in inputLineList[9].lower():
			isMale = False
			
		birthday = self.yearMonthDayStrToDate(inputLineList[10])
		
		retSwimmer = SW.Swimmer(fn,ln,birthday,isMale)
		return retSwimmer
	
	def parse(self):
		for line in self.listOfCSVLines:
			tempSwimmer = self.parseLineToSwimmer(line)
			if tempSwimmer is None:
				continue
			self.__swimmerHandlerObject.addSwimmer(tempSwimmer)


class SwimmerReader2024(SwimmerReader):
	def parseLineToSwimmer(self, inputLine):
		inputLine = inputLine.strip()
		inputLineList = inputLine.split(',')
		
		if 'Waitlist' == inputLineList[0]:
			return None
		
		fn = inputLineList[0].split(' ')[0]
		ln = inputLineList[1].split(' ')[0]
		
		isMale = True
		if 'fe' in inputLineList[4].lower():
			isMale = False
		
		birthday = self.yearMonthDayStrToDate(inputLineList[2].split('(')[1].split(')')[0])
		
		retSwimmer = SW.Swimmer(fn,ln,birthday,isMale)
		retSwimmer.setSwimmerID(inputLineList[3])
		return retSwimmer

class SwimmerReader2023(SwimmerReader):
	def parseLineToSwimmer(self, inputLine):
		inputLine = inputLine.strip()
		inputLineList = inputLine.split(',')
		
		if not(len(inputLineList) > 20):
			return None
		
		if inputLineList[1] == '':
			return None
		
		if 'reg' in inputLineList[1].lower():
			return None
		
		fn = inputLineList[6].split(' ')[0]
		ln = inputLineList[7].split(' ')[0]
		
		isMale = True
		if 'fe' in inputLineList[9].lower():
			isMale = False
			
		birthday = self.yearMonthDayStrToDate(inputLineList[10])
		
		retSwimmer = SW.Swimmer(fn,ln,birthday,isMale)
		return retSwimmer