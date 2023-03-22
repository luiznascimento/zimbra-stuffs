#!/usr/lib/python

import requests

soapEnvelope = """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"><soap:Header>\
<context xmlns="urn:zimbra"><nosession/></context></soap:Header><soap:Body><AuthRequest xmlns="urn:zimbraAccount">\
<account by="name">%s</account><password>%s</password></AuthRequest></soap:Body>\
</soap:Envelope>""" % ('admin@xxxxx.com.br', 'xxxxxx')
headers = {
  'Content-Type' : 'text/soap+xml'
}
zimbraUrl = 'https://xxxxxxxxx/service/soap'
req = requests.post(url=zimbraUrl, headers=headers, data=soapEnvelope, verify=False)
print req.text
