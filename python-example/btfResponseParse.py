##BTF auth example for Python 2.7.5
#XML Parsing of responses from BTF

import xml.etree.ElementTree as ET
import customberObj as Customer
from btfConstants import BTF_NAMESPACE as bt

#Takes the xml customer query response returned by BTF and 
#returns a list of populated Customers
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



