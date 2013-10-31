##BTF auth example for Python 2.7.5

from httplib import HTTPSConnection
from httplib import HTTPException
import customberObj as Customer
from btfConstants import *
 		  
def getAuthResponseXML(transactionXML):
	try:
		#Check with BTF regarding port number
		con = HTTPSConnection(hosturl,8443)
		headers = {"Authorization":"Bearer " + BTF_CLIENT_KEY, "Content-Type":"text/xml", "Content-Encoding": "UTF-8"}
		con.request("POST",BTF_REQ_PREFIX, transactionXML, headers)
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
	
def getCustomerList():
	response = getRequestResponseXML(BTF_CUSTOMER) 	
	customerList = parseCustomersXML(response)			
	return customerList
	
def findTokenByName(companyName, purchaserName):
	response = getRequestResponseXML(BTF_CUSTOMER_BY_NAME + companyName)
	custList = parseCustomersXML(response)
	cust = custList[0]
	token = cust.purchasers[ purchaserName ]
	return token

def setCreditLimit(customer):
	response = getRequestResponseXML(BTF_CUSTOMER_BY_BTF_NUM + customer.btfCid)
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

	
