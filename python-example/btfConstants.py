#BTF constants for authorization  

BTF_HOST_NAME = "integration.bluetarp.com"
BTF_MERCHANT_NUM = "***ASK BTF FOR TEST MERCH NUM***"
BTF_CLIENT_KEY = "***ASK FOR THIS***"


# send rewquests to this url
BTF_REQ_PREFIX = "/auth/v1/" + BTF_MERCHANT_NUM 

# request resources
BTF_CUSTOMER = "/customers"
BTF_CUSTOMER_BY_NAME = BTF_CUSTOMER + "?q="
BTF_CUSTOMER_BY_PHONE = BTF_CUSTOMER + "?q="
BTF_CUSTOMER_BY_BTF_NUM = BTF_CUSTOMER + "?bluetarp-cid="

#Search by dealer's id is not used in example
BTF_CUSTOMER_BY_DEALER_NUM = BTF_CUSTOMER + "?merchant-cid="

#ElementTree doesn't handle namespaces very well
BTF_NAMESPACE = "{http://api.bluetarp.com/ns/1.0}"
