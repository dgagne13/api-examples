##BTF auth example for Python 2.7.5
#XML Parsing of responses from BTF
import xml.etree.ElementTree as ET

from btfConstants import BTF_NAMESPACE as bt
from Customer import Customer
from Transaction import Transaction


#Takes the xml customer query response returned by BTF and 
#returns a list of populated Customers
def parseCustomersXML(custXML):
	root = ET.XML(custXML)
	custList = []

	for customer in root.iter(bt + "customer"):
		cust = parseCustomerElement(customer)
		custList.append(cust)

	return custList	

#Takes the xml auth response returned by BTF and 
#returns a dictionary with response code, message, etc.
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

#Takes the xml transaction query response returned by BTF and 
#returns a list of populated Transactions
def parseTransactionsXML(transXML):
	root = ET.XML(transXML)
	transList = []

	for transElem in root.iter(bt + "transaction"):
                transaction = Transaction(transElem.find(bt + "auth-seq").text)
                amtString = transElem.find(bt + "amount").text
                transaction.amount = float(amtString)
                
                invoice = transElem.find(bt + "invoice")
                if invoice is not None:
                        transaction.invoice = invoice.text
                        
                job = transElem.find(bt + "job-code")
                if job is not None:
                        transaction.job = job.text

                oldInvoice = transElem.find(bt + "original-invoice")
                if oldInvoice is not None:
                        transaction.oldInvoice = oldInvoice.text

                custElem = transElem.find(bt + "customer")
                transaction.cust = parseCustomerElement(custElem)
		
                transList.append(transaction)
	return transList

#Handles a single cusotmer element
def parseCustomerElement(customer):
        cname  = customer.find(bt + "name").text
        cust = Customer(cname)
        cust.btfCid = customer.find(bt + "number").text
                
        credElem = customer.find(bt + "avaialable-credit")
        if credElem is not None:
                cust.creditAvailable = credElem.text
		
        for purchaser in customer.iter(bt + "purchaser"):
                pname = purchaser.find(bt + "name").text
                token = purchaser.find(bt + "token").text
                cust.purchasers[pname] = token
        
        return cust
