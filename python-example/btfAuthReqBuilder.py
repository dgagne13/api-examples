from btfConstants import *
import xml.etree.ElementTree as ET

def buildAuthRequest(
def buildSaleXML(transactionId, clientId, authToken, amount, invoice, job):
	authRoot = ET.Element(bt + "bluetarp-authorization")
	authReq = ET.SubElement(authRoot, bt + "authorization-request");
	# add merchant element and set number
	merchElem = ET.SubElement(authReq,bt + "merchant-number")
	merchElem.text = BTF_MERCHANT_NUM

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
