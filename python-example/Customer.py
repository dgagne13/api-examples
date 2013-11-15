#Just a bogus customer class to store information in fro the example
#Merchant system probably already has an equivalent
from itertools import islice

class Customer(object):
	name =""
	btfCid = -1
	creditLimit = -1
	creditAvailable = -1
	purchasers = {}

	def __init__(self, name):
		self.name = name

	def display(self):
		print self.name + ":"
		if self.btfCid != -1:	
			print "  cid: " + self.btfCid
		if self.creditLimit != -1:	
			print "  limit: " + self.creditLimit
		if self.creditAvailable != -1:	
			print "  available: " + self.creditAvailable
		print "  Purchasers (up to 10 shown):"
		for pname, token in islice(self.purchasers.iteritems(),10):
			print "    " + pname + " : " + token
