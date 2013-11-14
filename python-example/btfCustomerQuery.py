##BTF auth example for Python 2.7.5
from btfConstants import *
import btfConnector as btc
import btfResponseParse as btrp


def getAllCustomers():
        response = btc.getRequestResponseXML(BTF_CUSTOMER)
	customerList = btrp.parseCustomersXML(response)			
	return customerList

def getCustomersByName(companyName):
        response = btc.getRequestResponseXML(BTF_CUSTOMER_BY_NAME + companyName)
	customerList = btrp.parseCustomersXML(response)			
	return customerList
	
def getCustomersByDealerID(dlrID):
        response = btc.getRequestResponseXML(BTF_CUSTOMER_BY_DLR_NUM + dlrID)
	customerList = btrp.parseCustomersXML(response)			
	return customerList

def getCustomersByBTFID(dlrID):
        response = btc.getRequestResponseXML(BTF_CUSTOMER_BY_BTF_NUM + dlrID)
	customerList = btrp.parseCustomersXML(response)			
	return customerList


