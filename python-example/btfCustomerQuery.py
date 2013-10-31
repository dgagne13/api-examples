def getRequestResponseXML(requesturl):
	try:
		#Check with BTF regarding port number
		con = HTTPSConnection(BTF_HOST_NAME,8443) 
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
