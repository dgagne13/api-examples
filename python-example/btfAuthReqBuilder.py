from btfConstants import *
import xml.etree.ElementTree as ET

#for readability
bt = BTF_NAMESPACE

def buildAuthRequest(transactionId, clientId, authToken):
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

    return authRoot
        
def buildSaleXML(transactionId, clientId, authToken, amount, invoice, job):

    authRoot = buildAuthRequest(transactionId, clientId, authToken)
    authReq = authRoot.find(bt + "authorization-request")

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

def buildCreditXML(transactionId, clientId, authToken, amount, invoice, job, oldInvoice):

    authRoot = buildAuthRequest(transactionId, clientId, authToken)
    authReq = authRoot.find(bt + "authorization-request")

    #add sale and sub-elements. Set amount, invoce, job
    credElem = ET.SubElement(authReq, bt + "credit")
    amountElem = ET.SubElement(credElem, bt + "amount")
    amountElem.text = str(amount)
    jobElem = ET.SubElement(credElem, bt + "job-code")
    jobElem.text = job
    invoiceElem = ET.SubElement(credElem, bt + "invoice")
    invoiceElem.text = invoice
    invoiceElem = ET.SubElement(credElem, bt + "original-invoice")
    invoiceElem.text = oldInvoice

    credXML = ET.tostring(authRoot, "utf-8")

    return credXML

def buildHoldXML(transactionId, clientId, authToken, amount, invoice, job):

    authRoot = buildAuthRequest(transactionId, clientId, authToken)
    authReq = authRoot.find(bt + "authorization-request")
    
    #add sale and sub-elements. Set amount, invoce, job
    holdElem = ET.SubElement(authReq, bt + "deposit-hold")
    amountElem = ET.SubElement(holdElem, bt + "amount")
    amountElem.text = str(amount)
    jobElem = ET.SubElement(holdElem, bt + "job-code")
    jobElem.text = job
    invoiceElem = ET.SubElement(holdElem, bt + "invoice")
    invoiceElem.text = invoice

    holdXML = ET.tostring(authRoot, "utf-8")

    return holdXML

def buildCollectXML(transactionId, clientId, authToken, amount, authSeq, invoice, job):

    authRoot = buildAuthRequest(transactionId, clientId, authToken)
    authReq = authRoot.find(bt + "authorization-request")
    
    #add sale and sub-elements. Set amount, invoce, job
    collectElem = ET.SubElement(authReq, bt + "deposit-collect")
    amountElem = ET.SubElement(collectElem, bt + "amount")
    amountElem.text = str(amount)
    authSeqElem = ET.SubElement(collectElem, bt + "auth-seq")
    authSeqElem.text = str(authSeq)
    jobElem = ET.SubElement(collectElem, bt + "job-code")
    jobElem.text = job
    invoiceElem = ET.SubElement(collectElem, bt + "invoice")
    invoiceElem.text = invoice

    collectXML = ET.tostring(authRoot, "utf-8")

    return collectXML

def buildVoidXML(transactionId, clientId, authSeq, authToken):

    authRoot = buildAuthRequest(transactionId, clientId, authToken)
    authReq = authRoot.find(bt + "authorization-request")
    
    #add sale and sub-elements. Set amount, invoce, job
    voidElem = ET.SubElement(authReq, bt + "void")
    authSeqElem = ET.SubElement(voidElem, bt + "auth-seq")
    authSeqElem.text = str(authSeq)
    
    collectXML = ET.tostring(authRoot, "utf-8")

    return collectXML
