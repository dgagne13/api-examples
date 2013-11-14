##BTF auth example for Python 2.7.5
import btfConnector as btc
from btfConstants import *
import btfResponseParse as btrp

def getVoidables():
        response = btc.getRequestResponseXML(BTF_VOIDABLES)
	transList = btrp.parseTransactionsXML(response)			
	return transList

def getDeposits():
        response = btc.getRequestResponseXML(BTF_DEPOSITS)
	transList = btrp.parseTransactionsXML(response)			
	return transList

