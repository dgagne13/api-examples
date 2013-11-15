using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;

namespace BlueTarp_Auth_API_Example
{
    class VoidExample : ExampleBase
    {
        private readonly static string VOID_XML  ="" +
            "<?xml version='1.0' encoding='utf-8'?>" +
            "<bt:bluetarp-authorization xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://api.bluetarp.com/ns/1.0 https://api.bluetarp.com/v1/Authorization.xsd\" xmlns:bt=\"http://api.bluetarp.com/ns/1.0\">" +
            "  <bt:authorization-request>" +
            "    <bt:merchant-number>" + BLUETARP_TEST_MERCHANT + "</bt:merchant-number>" +
            "    <bt:client-id>Test Client</bt:client-id>" +
            "    <bt:transaction-id>6c4ef62a-220b-467f-aa79-48f762f0b8df</bt:transaction-id>" +
            "    <bt:purchaser-with-token>" +
            "      <bt:token>" + BLUETARP_TEST_PURCHASER_TOKEN + "</bt:token>" +
            "    </bt:purchaser-with-token>" +
            "    <bt:void>" +
            "      <bt:auth-seq>{0}</bt:auth-seq>" +
            "    </bt:void>" +
            "  </bt:authorization-request>" +
            "</bt:bluetarp-authorization>";

        public static void Run(string authSequence)
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(BLUETARP_TEST_API + BLUETARP_TEST_MERCHANT);
            request.ContentType = "text/xml";
            request.Headers.Add(HttpRequestHeader.Authorization, "Bearer " + BLUETARP_TEST_CLIENT_KEY);
            request.Headers.Add(HttpRequestHeader.ContentEncoding, "UTF-8");
            request.Method = "POST";

            // be sure to set the auth sequence to void from a previous transaction
            byte[] requestXml = Encoding.UTF8.GetBytes(String.Format(VOID_XML, authSequence));

            request.GetRequestStream().Write(requestXml, 0, requestXml.Length);
            request.GetRequestStream().Close();

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
