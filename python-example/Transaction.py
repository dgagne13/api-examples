import Customer

class Transaction(object):
      authSeq = ""
      amount = -1.00
      cust = None
      invoice = ""
      job = ""
      oldInvoice = ""

      def __init__(self, authSeq):
            self.authSeq = authSeq

      def display(self):
            print "Auth Seq: " + str(self.authSeq)
            if self.amount != -1:
                  print "Amount: " + str(self.amount)
            if self.cust is not None:
                  cust = self.cust
                  print "Cust Name: " + cust.name
                  if cust.purchasers.values() is not None:
                        print "Token:  " + cust.purchasers.values()[0]
            if self.invoice != "":
                  print "Invoice : " + str(self.invoice)
            if self.job != "":
                  print "Job Code : " + str(self.job)
            if self.oldInvoice != "":
                  print "Old Invoice: " + str(self.oldInvoice)
