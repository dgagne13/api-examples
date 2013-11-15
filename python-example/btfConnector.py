from httplib import HTTPSConnection
from httplib import HTTPException

from btfConstants import *

def getRequestResponseXML(requesturl):
	try:
		#Check with BTF regarding port number
		con = HTTPSConnection(BTF_HOST_NAME) 
		headers = {"Authorization":"Bearer " + BTF_CLIENT_KEY}
		cleanedurl = BTF_REQ_PREFIX + requesturl.replace(" ", "%20")
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
		con = HTTPSConnection(BTF_HOST_NAME)
		headers = {"Authorization":"Bearer " + BTF_CLIENT_KEY, 
                "Content-Type":"text/xml", "Content-Encoding": "UTF-8"}
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
