import base64
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


template = '''
    <!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>invoice</title>
</head>

<body>
    <div class="invoice-box">
        hello world
    </div>
</body>
</html>
'''

message = Mail(
    from_email='from_email@example.com',
    to_emails='jasirmj@gmail.com',
    subject='test Sending with Twilio SendGrid is Fun',
    html_content=template #html template
)
file_path = 'jasir1.pdf'
with open(file_path, 'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()
attachment = Attachment()
attachment.file_content = FileContent(encoded)
attachment.file_type = FileType('application/pdf')
attachment.file_name = FileName('jasir1.pdf')
attachment.disposition = Disposition('attachment')
attachment.content_id = ContentId('123')
message.attachment = attachment
try:
    # sendgrid_client = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    sendgrid_client = SendGridAPIClient('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')
    print("sendgrid_client ", sendgrid_client)
    response = sendgrid_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)


