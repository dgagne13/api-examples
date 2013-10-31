import btfCustomerQuery as BtCQ
import btfAuthorization as BtAuth

from customerObj import Cusotmer

print "Testing out the BTF auth with Python:"
print "Getting list of all customers:"
customerList = BtCQ.getCustomerList()

print "Displaying first 10 customer names and purchasers:"
for cust in customerList[:10]:
	cust.display()
	
cust1 = customerList[0]
cName = cust1.name

print "Setting credit for customer " + cName
BtCQ.getCreditLimit(cust1)

print "Displaying info for customer " + cName
cust1.display()   

pName = cust1.purchasers.keys()[0]
print "Find token by search:"	 	
print "  Looking for company " + cName + " with purchaser " + pName
token = BtCQ.findTokenByName(cName, pName)

print "Found token: " + token + "  (should match token above)"

print "Authorizing $100.00 sale for " + pName

#Generate uuid for transaction
# import uuid causes this version of python to break
BtAuth.authorizeSale('727382f0-3fff-11e3-aa6e-0800200c9a66', cName, token, 100.00, "Invoice.123456-1")	

print "Authorizing $10,000,000 sale for " + pName

BtAuth.authorizeSale('727382f0-3fff-11e3-aa6e-0800200c9a66', cName, token, 10000000.00)
