##BTF auth example for Python 2.7.5
from btfAuthReqBuilder import *
from btfConstants import *
from btfConnector import getAuthResponseXML
from btfResponseParse import parseAuthXML

def authorizeSale(transactionId, clientId, authToken, amount, invoice="", 
job=""):
	saleXML = buildSaleXML(transactionId, clientId, authToken, amount, 
        invoice, job)
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

def authorizeCredit(transactionId, clientId, authToken, amount, invoice="", 
job="", oldInvoice=""):
	creditXML = buildCreditXML(transactionId, clientId, authToken, amount, 
        invoice, job, oldInvoice)

	#send xml doc to btf and get response		
	responseXML = getAuthResponseXML(creditXML)
	authResponse = parseAuthXML(responseXML)
	message = authResponse[ "message" ]
	print "Credit Authorization details:" 
	print " Status(Approve/Decline): " + authResponse[ "message" ]
	if(message == "APPROVED"):
		print " Auth Sequence " + authResponse[ "authseq"]
		print "  Approval code: " + authResponse[ "appcode" ]
	return message
	

def authorizeHold(transactionId, clientId, authToken, amount, invoice="", 
job=""):
	holdXML = buildHoldXML(transactionId, clientId, authToken, amount, 
        invoice, job)
	#send xml doc to btf and get response	
	
	responseXML = getAuthResponseXML(holdXML)
	authResponse = parseAuthXML(responseXML)
	message = authResponse[ "message" ]
	print "Hold Authorization details:" 
	print " Status(Approve/Decline): " + authResponse[ "message" ]
	if(message == "APPROVED"):
		print " Auth Sequence " + authResponse[ "authseq"]
		print "  Approval code: " + authResponse[ "appcode" ]
	return message

def authorizeCollect(transactionId, clientId, authToken, amount, authSeq, invoice="", 
                     job=""):
	collectXML = buildCollectXML(transactionId, clientId, authToken, 
                                     amount, authSeq, invoice, job)
	#send xml doc to btf and get response	
	
	responseXML = getAuthResponseXML(collectXML)
	authResponse = parseAuthXML(responseXML)
	message = authResponse[ "message" ]
	print "Collect Authorization details:" 
	print " Status(Approve/Decline): " + authResponse[ "message" ]
	if(message == "APPROVED"):
		print " Auth Sequence " + authResponse[ "authseq"]
		print "  Approval code: " + authResponse[ "appcode" ]
	return message

def authorizeVoid(transactionID, clientId, authSeq, authToken):
        voidXML = buildVoidXML(transactionID, clientId, authSeq, authToken)
	#send xml doc to btf and get response	
	
	responseXML = getAuthResponseXML(voidXML)
	authResponse = parseAuthXML(responseXML)
	message = authResponse[ "message" ]
	print "Collect Authorization details:" 
	print " Status(Approve/Decline): " + authResponse[ "message" ]
	if(message == "APPROVED"):
		print " Auth Sequence " + authResponse[ "authseq"]
		print "  Approval code: " + authResponse[ "appcode" ]
	return message

