import btfCustomerQuery as BtCQ
import btfTransactionQuery as BtTQ
import btfAuthorization as BtAuth

import Customer
import Transaction

print "Testing out the BTF auth with Python:"

partCName = "F_"


print "Searching for partial name of " + partCName
print "BTF Auth system will search for matches in customer"
print "and purchaser names"
print " "

customerList = BtCQ.getCustomersByName(partCName)

print "Displaying first 10 customer names and purchasers:"

for cust in customerList[:10]:
	cust.display()

cust1 = customerList[0]
cName = cust1.name
pName = cust1.purchasers.keys()[0]
token = cust1.purchasers[pName]

print " "
print "Searching for customer by bluetarp-cid = "
print "Displaying first 10 customer names and purchasers:"
customerList = BtCQ.getCustomersByBTFID(cust.btfCid)
for cust in customerList[:10]:
	cust.display()
        print " "

print "Authorizing $100.00 sale for " + pName
print "Using token " + token
BtAuth.authorizeSale('727382f0-3fff-11e3-aa6e-0800200c9a66', "Terminal 1", token, 
    100.00, "Invoice.1")	

print " "
print "Authorizing $10,000,000 sale for " + pName
print "Using token " + token
BtAuth.authorizeSale('727382f0-3fff-11e3-aa6e-0800200c9a66', "Terminal 1", token, 
    10000000.00)

print " "
print "Authorizing $100.00 credit for " + pName
print "Using token " + token
BtAuth.authorizeCredit('727382f0-3fff-11e3-aa6e-0800200c9a66', "Terminal 1", token, 
    100.00, "Invoice.3", "credit-Example", "Invoice.1")	

print " "
print "Authorizing $100.00 hold for " + pName
print "Using token " + token
BtAuth.authorizeHold('727382f0-3fff-11e3-aa6e-0800200c9a66', "Terminal 1", token,
     100.00, "Invoice.4")

print " "
print "Listing collectable deposits (there should be at least 1)"
transList = BtTQ.getDeposits()

"Listing first ten transactions:"
for trans in transList[:10]:
        trans.display()
        print " "

trans1 = transList[0]
holdToken = trans1.cust.purchasers.values()[0]

print "Attempting to collect 90% of the first hold"
print "Using token " + holdToken
BtAuth.authorizeCollect("6b5ae470-4d53-11e3-8f96-0800200c9a66", 
"Terminal 1", holdToken, (0.9 * trans1.amount), trans1.authSeq,
"Invoice.5", "Collect-Example")

print " "
print "Listing voidable deposits (there should be at least 1)"
transList = BtTQ.getVoidables()

"Listing first ten transactions:"
for trans in transList[:10]:
        trans.display()
        print " "

trans1 = transList[0]
voidToken = trans1.cust.purchasers.values()[0]

print "Attempting to void auth " + trans1.authSeq
print "Using token " + voidToken
BtAuth.authorizeVoid("8848dd50-4d5a-11e3-8f96-0800200c9a66", "Terminal 1",
trans1.authSeq, voidToken)
