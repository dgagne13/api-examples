using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.IO;
using BlueTarp_Auth_API_Example;

namespace BlueTarp_Auth_API_Example
{

    class SaleWithPurcahserNumberExample : ExampleBase
    {
        private readonly static string SALE_XML = "" +
            "<?xml version='1.0' encoding='utf-8'?>" +
            "<bt:bluetarp-authorization xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://api.bluetarp.com/ns/1.0 https://api.bluetarp.com/v1/Authorization.xsd\" xmlns:bt=\"http://api.bluetarp.com/ns/1.0\">" +
            "  <bt:authorization-request>" +
            "    <bt:merchant-number>" + BLUETARP_TEST_MERCHANT + "</bt:merchant-number>" +
            "    <bt:client-id>Test Client</bt:client-id>" +
            "    <bt:transaction-id>63f9f8e0-a1a0-42dc-9dda-a3e9defddf49</bt:transaction-id>" +
            "    <bt:purchaser>" +
            "      <bt:number>" + BLUETARP_TEST_PURCHASER_NUMBER + "</bt:number>" +
            "    </bt:purchaser>" +
            "    <bt:sale>" +
            "      <bt:amount>1.00</bt:amount>" +
            "    </bt:sale>" +
            "  </bt:authorization-request>" +
            "</bt:bluetarp-authorization>";

        public static void Run()
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(BLUETARP_TEST_API + BLUETARP_TEST_MERCHANT);
            request.ContentType = "text/xml";
            request.Headers.Add(HttpRequestHeader.Authorization, "Bearer " + BLUETARP_TEST_CLIENT_KEY);
            request.Headers.Add(HttpRequestHeader.ContentEncoding, "UTF-8");
            request.Method = "POST";

            byte[] requestXml = Encoding.UTF8.GetBytes(SALE_XML);

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
