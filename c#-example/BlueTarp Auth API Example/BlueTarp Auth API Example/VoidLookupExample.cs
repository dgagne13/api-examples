using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Net;

namespace BlueTarp_Auth_API_Example
{
    class VoidLookupExample : ExampleBase
    {
        public static void Run()
        {
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(BLUETARP_TEST_API + BLUETARP_TEST_MERCHANT + "/transactions/void");
            request.Headers.Add(HttpRequestHeader.Authorization, "Bearer " + BLUETARP_TEST_CLIENT_KEY);
            request.Headers.Add(HttpRequestHeader.ContentEncoding, "UTF-8");

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
