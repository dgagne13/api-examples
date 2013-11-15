using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;
using System.IO;

namespace BlueTarp_Auth_API_Example
{
    public class ExampleBase
    {
        protected readonly static string BLUETARP_TEST_API = "https://integration.bluetarp.com/auth/v1/";
        /** Contact BlueTarp to obtain test values for these variables */
        protected readonly static string BLUETARP_TEST_CLIENT_KEY = "";
        protected readonly static string BLUETARP_TEST_MERCHANT = "";
        protected readonly static string BLUETARP_TEST_PURCHASER_TOKEN = "";
        protected readonly static string BLUETARP_TEST_PURCHASER_NUMBER = "";
        protected readonly static string BLUETARP_TEST_CID = "";

        protected static void printResponseToConsole(HttpWebResponse response)
        {
            Stream dataStream = response.GetResponseStream();
            StreamReader reader = new StreamReader(dataStream);
            String responseXml = reader.ReadToEnd();

            Console.Out.WriteLine("BlueTarp Auth status code: " + response.StatusCode);
            Console.Out.WriteLine("BlueTarp Auth Response:");
            Console.Out.WriteLine(responseXml);
            dataStream.Close();
            reader.Close();
            response.Close();
        }
    }
}
