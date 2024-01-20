
from twilio.rest import Client

account_sid = 'AC3b282a21223c3f32887dbeca2b2c69a1'
auth_token = '020afc973badd72abd2898bbd64a6680'
client = Client(account_sid, auth_token)

ct=Client(account_sid,auth_token)

ct.messages.create(body='your phone is been hacked your gpay balance is stolen ohh nevermind your account has no balance i feel sad for you i will send you 10 rupees',from_='+12019955209',to='+917200869116')