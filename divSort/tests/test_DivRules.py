import unittest as pt

from src import DivRules as MUT
from src import Swimmer as SW
from datetime import date

class DivRulesReader_TestFunctions(pt.TestCase):
	def testCorrectlySortsDivs(self):
		t = MUT.DivRules()
		t.setDivNOldest(1,date(2014, 5,1))
		t.setDivNOldest(2,date(2012,11,1))
		t.setDivNOldest(3,date(2011, 5,1))
		t.setDivNOldest(4,date(2009,11,1))
		t.setDivNOldest(5,date(2008, 5,1))
		t.setDivNOldest(6,date(2006, 5,1))
		t.setDivNOldest(7,date(2003, 5,1))

		swimmerD1 = SW.Swimmer('bob','Jim',date(2018,5,1),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD1), 1)
		
		swimmerD1 = SW.Swimmer('bob','Jim',date(2014,5,1),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD1), 1)

		swimmerD2 = SW.Swimmer('bob','Jim',date(2014,4,30),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD2), 2)

		swimmerD2 = SW.Swimmer('bob','Jim',date(2012,11,1),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD2), 2)

		swimmerD3 = SW.Swimmer('bob','Jim',date(2012,10,31),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD3), 3)

		swimmerD3 = SW.Swimmer('bob','Jim',date(2011,5,1),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD3), 3)

		swimmerD4 = SW.Swimmer('bob','Jim',date(2011,4,30),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD4), 4)

		swimmerD4 = SW.Swimmer('bob','Jim',date(2009,11,1),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD4), 4)

		swimmerD5 = SW.Swimmer('bob','Jim',date(2009,10,31),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD5), 5)

		swimmerD5 = SW.Swimmer('bob','Jim',date(2008,5,1),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD5), 5)
		
		swimmerD6 = SW.Swimmer('bob','Jim',date(2008,4,30),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD6), 6)

		swimmerD6 = SW.Swimmer('bob','Jim',date(2006,5,1),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD6), 6)

		swimmerD7 = SW.Swimmer('bob','Jim',date(2006,4,30),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD7), 7)

		swimmerD7 = SW.Swimmer('bob','Jim',date(2003,5,1),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD7), 7)

		swimmerD8 = SW.Swimmer('bob','Jim',date(2003,4,30),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD8), 8)
	
		swimmerD8 = SW.Swimmer('bob','Jim',date(2000,4,30),True)
		self.assertEqual(t.returnSwimmerDiv(swimmerD8), 8)