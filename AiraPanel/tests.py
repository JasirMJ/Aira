import json

import requests
from django.test import TestCase

# Create your tests here.
# import json
#
# # some JSON:
# x = '[{ "name":"John", "age":30, "city":"New York"},{ "name":"John", "age":30, "city":"New York"}]'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(len(y))
# for x in y:
#     print(x['name'])


def SendMail(mail,username,password):
    SUBJECT = "Codedady Invoice"
    url = "https://api.sendgrid.com/v3/mail/send"
    data = {
        "personalizations": [
            {
                "to": [
                    {
                        "email": mail,
                    }
                ]
            }
        ],
        "from": {
            "email": "aira.admin@no-replay.com"
        },
        "subject": SUBJECT,
        "content": [
            {
                "type": "text/html",
                "value": '''

    <html>
        <body><br>
            <br>
            <center>
            <div style="background-color:rgb(241, 241, 241);height: 600px;width: 500px;">
                    <div style="float: left;    background-color:rgb(227, 244, 255);    height: 100px;    width: 200px;">address </div>
                    <div class="invoice_details" style="float: right;    background-color:rgb(223, 242, 255);    height: 100px;    width: 200px;">invoice number</div>
                <div style="height: 10px;"></div>    

                <div class="items" style="margin-top:100px;    background-color:red;    height: 200px;    width: 500px;">
                    items list
                    <div style="background-color: wheat;">
                        <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                            si 
                        </div>
                        <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                            item
                        </div>
                        <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                            tax        
                        </div>
                        <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                            price        
                        </div>
                        <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                            qty
                        </div>
                        <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                            total
                        </div>
                        
                        <div>
                            <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                                si 
                            </div>
                            <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                                item
                            </div>
                            <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                                tax        
                            </div>
                            <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                                price        
                            </div>
                            <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                                qty
                            </div>
                            <div style="display: inline-block;    width: 78px;    background-color: thistle;">
                                total
                            </div>
                            
                        </div>
                    </div>

                </div>

        <div style="float: left ;    margin-top:10px;    background-color:green;    height: 50px;    width: 200px;">other details</div>
            </div>
        </center>
        </body>
    </html>
                    '''

            }
        ]
    }
    headers = {
        'Content-type': 'application/json',
        # 'Accept': 'text/plain',
        'Authorization': 'Bearer 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',
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r)


SendMail('jasirmj@gmail.com', "jasir", "password")