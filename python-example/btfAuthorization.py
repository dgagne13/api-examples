##BTF auth example for Python 2.7.5

from httplib import HTTPSConnection
from httplib import HTTPException
import xml.etree.ElementTree as ET
from itertools import islice

hosturl = "***ASK BTF FOR TEST AUTH HOST URL***"
authurl = "/auth/v1"
merchantNum = "***ASK BTF FOR TEST AUTH HOST URL***"

#ElementTree doesn't handle namespaces very well
bt ='{http://api.bluetarp.com/ns/1.0}'

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
 		
def getClientKey():
	#keep the client key in a secure location
	return "***ASK BTF FOR A TEST CLIENT KEY***"

def getRequestResponseXML(requesturl):
	try:
		#Check with BTF regarding port number
		con = HTTPSConnection(hosturl,8443) 
		headers = {"Authorization":"Bearer " + getClientKey()}
		cleanedurl = authurl + "/" + merchantNum + requesturl.replace(" ", "%20")
		con.request("GET", cleanedurl, None, headers)
		res = con.getresponse()
		if res.status == 200:
			xml = res.read()
			con.close()
			return xml
		else:
			raise HTTPException(res.reason)
	except HTTPException as e:
		print "There was a problem connecting: "
		con.close()
		raise
  
def getAuthResponseXML(transactionXML):
	try:
		#Check with BTF regarding port number
		con = HTTPSConnection(hosturl,8443)
		headers = {"Authorization":"Bearer " + getClientKey(), "Content-Type":"text/xml", "Content-Encoding": "UTF-8"}
		con.request("POST",authurl + "/" + merchantNum , transactionXML, headers)
		res = con.getresponse()
		if res.status == 200:
			xml = res.read()
			con.close()
			return xml
		else:
			raise HTTPException(res.reason)
	except HTTPException as e:
		print "There was a problem connecting: "
		con.close()
		raise	
	
def parseCustomersXML(custXML):
	root = ET.XML(custXML)
	custList = []

	for customer in root.iter(bt + "customer"):
		
		cust = Customer(customer.find(bt + "name").text)
		cust.btfCid = customer.find(bt + "number").text
		
		for purchaser in customer.iter(bt + "purchaser"):
			pname = purchaser.find(bt + "name").text
			token = purchaser.find(bt + "token").text
			cust.purchasers[pname] = token
		custList.append(cust)
	return custList	

def parseAuthXML(authXML):
	root = ET.XML(authXML)
	authDict = {}
	for authRes in root.iter(bt + "authorization-response"):
		authDict["code"] = authRes.find(bt + "code").text
		authDict["message"] = authRes.find(bt + "message").text
		if(authRes.find(bt + "auth-seq") != None):
			authDict["authseq"] = authRes.find(bt + "auth-seq").text
			authDict["appcode"] = authRes.find(bt + "approval-code").text
	return authDict	

def parseCustomerCreditXML(creditXML):
	root = ET.XML(creditXML)
	credDict = {}
	for customer in root.iter(bt + "customer"):
		credDict["name"] = customer.find(bt + "name").text
		credDict["limit"] = customer.find(bt + "credit-limit").text
		credDict["available"] = customer.find(bt + "available-credit").text
	return credDict

def buildSaleXML(transactionId, clientId, authToken, amount, invoice, job):
	authRoot = ET.Element(bt + "bluetarp-authorization")
	authReq = ET.SubElement(authRoot, bt + "authorization-request");
	# add merchant element and set number
	merchElem = ET.SubElement(authReq,bt + "merchant-number")
	merchElem.text = merchantNum

	# add client elem and set name
	clientElem = ET.SubElement(authReq,bt + "client-id")
	clientElem.text = clientId

	#add transaction elem and set name
	transElem = ET.SubElement(authReq,bt + "transaction-id")
	transElem.text = transactionId

	#add purchaser and token elems and set token
	purchElem =ET.SubElement(authReq, bt + "purchaser-with-token")
	tokenElem = ET.SubElement(purchElem, bt + "token")
	tokenElem.text = authToken

	#add sale and sub-elements. Set amount, invoce, job
	saleElem = ET.SubElement(authReq, bt + "sale")
	amountElem = ET.SubElement(saleElem, bt + "amount")
	amountElem.text = str(amount)
	jobElem = ET.SubElement(saleElem, bt + "job-code")
	jobElem.text = job
	invoiceElem = ET.SubElement(saleElem, bt + "invoice")
	invoiceElem.text = invoice

	saleXML = ET.tostring(authRoot, "utf-8")

	return saleXML

def getCustomerList():
	response = getRequestResponseXML("/customers") 	
	customerList = parseCustomersXML(response)			
	return customerList
	
def findTokenByName(companyName, purchaserName):
	response = getRequestResponseXML("/customers?q=" + companyName)
	custList = parseCustomersXML(response)
	cust = custList[0]
	token = cust.purchasers[ purchaserName ]
	return token

def setCreditLimit(customer):
	response = getRequestResponseXML("/customers?bluetarp-cid=" + customer.btfCid)
	creditInfo = parseCustomerCreditXML(response)
	customer.creditLimit = creditInfo[ "limit" ]	
	customer.creditAvailable = creditInfo[ "available"]
	
def authorizeSale(transactionId, clientId, authToken, amount, invoice="", job=""):
	saleXML = buildSaleXML(transactionId, clientId, authToken, amount, invoice, job)
	#send xml doc to btf and get response	
	
	responseXML = getAuthResponseXML(saleXML)
	authResponse = parseAuthXML(responseXML)
	message = authResponse[ "message" ]
	print "Sale Authorization details:" 
	print " Status(Approve/Decline): " + authResponse[ "message" ]
	if(message == "APPROVED"):
		print " Auth Sequence " + authResponse[ "authseq"]
		print "  Approval code: " + authResponse[ "appcode" ]
	return message

print "Testing out the BTF auth with Python:"
print "Getting list of customers:"
customerList = getCustomerList()
print "Displaying first 10 customer names and purchasers:"
for cust in customerList[:10]:
	cust.display()
	
cust1 = customerList[0]
cName = cust1.name

print "Setting credit for customer " + cName
setCreditLimit(cust1)

print "Displaying info for customer " + cName
cust1.display()   

pName = cust1.purchasers.keys()[0]
print "Find token by search:"	 	
print "  Looking for company " + cName + " with purchaser " + pName
token = findTokenByName(cName, pName)

print "Found token: " + token + "  (should match token above)"

print "Authorizing $100.00 sale for " + pName

#Generate uuid for transaction
# import uuid causes this version of python to break
authorizeSale('727382f0-3fff-11e3-aa6e-0800200c9a66', cName, token, 100.00, "Invoice.123456-1")	

print "Authorizing $10,000,000 sale for " + pName

authorizeSale('727382f0-3fff-11e3-aa6e-0800200c9a66', cName, token, 10000000.00)	