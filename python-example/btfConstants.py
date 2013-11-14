#BTF constants for authorization  

BTF_HOST_NAME = "integration.bluetarp.com"
BTF_MERCHANT_NUM = "7"
BTF_CLIENT_KEY = "wLn1zexQS3dzIGx3bG2U2M"


# send rewquests to this url
BTF_REQ_PREFIX = "/auth/v1/" + BTF_MERCHANT_NUM 

# customer lookup resources
BTF_CUSTOMER = "/customers"
BTF_CUSTOMER_BY_NAME = BTF_CUSTOMER + "?q="
BTF_CUSTOMER_BY_PHONE = BTF_CUSTOMER + "?q="
BTF_CUSTOMER_BY_BTF_NUM = BTF_CUSTOMER + "?bluetarp-cid="
BTF_CUSTOMER_BY_DLR_NUM = BTF_CUSTOMER + "?merchant-cid="

#transaction lookup resources
BTF_TRANSACTIONS = "/transactions"
BTF_VOIDABLES = BTF_TRANSACTIONS + "/void"
BTF_DEPOSITS = BTF_TRANSACTIONS + "/deposit"

#ElementTree doesn't handle namespaces very well
BTF_NAMESPACE = "{http://api.bluetarp.com/ns/1.0}"
