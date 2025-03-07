import argparse #https://docs.python.org/3/library/argparse.html#action
import pathlib
import os

from src import DivRulesReader as DRR
from src import SwimmerReader as SR
from src import SwimmerSaver as SS

def sortSwimmers(divRulesFile, csvFile, resDir):
	
	readRules = DRR.DivRulesReader(divRulesFile)
	divRulesObject = readRules.returnRulesObject()
	#print(divRulesObject)
	
	swimmerReaderObject = SR.SwimmerReader2025(csvFile)
	swimmerReaderObject.read()
	swimmerHandlerObject = swimmerReaderObject.returnSwimmerObject()
	print('%s Swimmers Found.' % swimmerHandlerObject.numberSwimmers())

	csvFileObject = pathlib.Path(csvFile)
	fileName = csvFileObject.stem + '_edited.csv'
	swimmerSaverObject = SS.SwimmerSaver(resDir, fileName)
	swimmerSaverObject.register(swimmerHandlerObject)
	
	swimmerHandlerObject.calculateDivs(divRulesObject)
	#swimmerHandlerObject.printList()
	
	swimmerSaverObject.save()
	
	return

def main():
	parser = argparse.ArgumentParser(prog = 'Port Coquitlam Marlins Div Sorting Code', 
						description="Reads CSV file of swimmers Name, Gender, Age. Also read Div Rule file. Uses both to sort the swimmers into divs.")

	parser.add_argument('-d','--DivRulesFile', type=pathlib.Path, default=None,
		help='Absolute or relative location of the rules file for sorting divs. By default it will search for AgeLocator.txt.')
	parser.add_argument('-s','--SwimmerCSVFile', type=pathlib.Path, default=None,
		help='Absolute or relative location of the CSV file with the swimmers. By default it will search forRegistrationList.csv.')
	parser.add_argument('-r','--resFileLocation', type=pathlib.Path, default=None,
		help='The directory you want to save the results to. By default it will save the results to PWD.')

	args = parser.parse_args()
	divRulesFile = ''
	csvFile = ''
	resFile = ''
	
	if args.DivRulesFile is None:
		divRulesFile = 'AgeLocator.txt'
		if not(os.path.isfile(divRulesFile)):
			print('Could not find AgeLocator.txt, add it to the dir.')
			quit()
	elif os.path.isfile(args.DivRulesFile):
		divRulesFile = os.path.abspath(args.DivRulesFile)
	else:
		print('Given file %s does not exist. Stopping.' % args.DivRulesFile)
		quit()
	
	if args.SwimmerCSVFile is None:
		csvFile = 'RegistrationList.csv'
		if not(os.path.isfile(csvFile)):
			print('Could not find RegistrationList.csv, add it to the dir.')
			quit()
	elif os.path.isfile(args.SwimmerCSVFile):
		csvFile = os.path.abspath(args.SwimmerCSVFile)
	else:
		print('Given registration file %s does not exist. Stopping.' % args.SwimmerCSVFile)
		quit()
		
	if args.resFileLocation is None:
		resFile = '.'
	elif os.path.isfile(args.resFileLocation):
		resFile = os.path.abspath(args.resFileLocation)
	else:
		print('Given res file %s does not exist. Stopping.' % args.resFileLocation)
		quit()
		
	sortSwimmers(divRulesFile, csvFile, resFile)

	return 0

#Main functionality
res = main()
