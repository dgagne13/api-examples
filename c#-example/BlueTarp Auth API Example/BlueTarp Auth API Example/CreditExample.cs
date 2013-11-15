using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;

namespace BlueTarp_Auth_API_Example
{
    public class CreditExample :ExampleBase
    {
        private readonly static string CREDIT_XML = "" +
            "<?xml version='1.0' encoding='utf-8'?>" +
            "<bt:bluetarp-authorization xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://api.bluetarp.com/ns/1.0 https://api.bluetarp.com/v1/Authorization.xsd\" xmlns:bt=\"http://api.bluetarp.com/ns/1.0\">" +
            "  <bt:authorization-request>" +
            "    <bt:merchant-number>" + BLUETARP_TEST_MERCHANT + "</bt:merchant-number>" +
            "    <bt:client-id>Test Client</bt:client-id>" +
            "    <bt:transaction-id>143e1641-66d9-4f9f-a291-f0fd118b7b01</bt:transaction-id>" +
            "    <bt:purchaser-with-token>" +
            "      <bt:token>" + BLUETARP_TEST_PURCHASER_TOKEN + "</bt:token>" +
            "    </bt:purchaser-with-token>" +
            "    <bt:credit>" +
            "      <bt:amount>1.00</bt:amount>" +
            "      <bt:job-code>1k23rh</bt:job-code><!-- optional -->" +
            "      <bt:invoice>J08223</bt:invoice><!-- optional -->" +
            "      <bt:original-invoice>602437</bt:original-invoice><!-- optional -->" +
            "    </bt:credit>" +
            "  </bt:authorization-request>" +
            "</bt:bluetarp-authorization>";

        public static void Run()
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(BLUETARP_TEST_API + BLUETARP_TEST_MERCHANT);
            request.ContentType = "text/xml";
            request.Headers.Add(HttpRequestHeader.Authorization, "Bearer " + BLUETARP_TEST_CLIENT_KEY);
            request.Headers.Add(HttpRequestHeader.ContentEncoding, "UTF-8");
            request.Method = "POST";

            byte[] requestXml = Encoding.UTF8.GetBytes(CREDIT_XML);

            request.GetRequestStream().Write(requestXml, 0, requestXml.Length);

            try
            {
                printResponseToConsole((HttpWebResponse)request.GetResponse());
            }
            catch (WebException e)
            {
                printResponseToConsole((HttpWebResponse)e.Response);
            }
        }
    }
}
