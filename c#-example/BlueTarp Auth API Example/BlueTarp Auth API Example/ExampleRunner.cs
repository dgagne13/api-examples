using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace BlueTarp_Auth_API_Example
{
    public class ExampleRunner
    {
        public static void Main(string[] args)
        {
            /* Sale and Credit Examples */
            SaleWithTokenExample.Run();
            //SaleWithPurcahserNumberExample.Run();
            //CreditExample.Run();

            /* Deposit Hold and Deposit Collect Examples */
            /* Run Deposit Hold example first, and copy the AuthSeq returned from the result. Use that AuthSeq when running the Deposit Collect Example */
            //DepositHoldExample.Run();
            //DepositCollectExample.Run("PUT AUTH SEQUENCE HERE");

            /* Void */
            /* Run a Sale example first and copy the AuthSeq returned from the result. Use the AuthSeq when running the Void example */
            //VoidExample.Run("PUT AUTH SEQUENCE HERE");

            /* Customer Lookup Examples */
            //CustomerLookupExample.Run();

            /* Retrieve Customer Credit Data */
            //RetrieveCreditDataExample.Run();

            /* Transaction Lookup */
            //VoidLookupExample.Run();
            //DepositCollectLookupExample.Run();
        }
    }
}
