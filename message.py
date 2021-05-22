from twilio.rest import Client

account_sid="AC8900e6afc2933ddd57cf41c72e272dba"


auth_token="dd73d77310cd5afb1f73fa2bb7c2bb5d"

client = Client(account_sid, auth_token)
message = client.messages.create( # sending msg; client.messages.create is a fcn call 
    to="+886983558907",
    from_="+15598887033",
    body="hi!我是俐璇~收到簡訊後,趕快打電話來祝賀我成功了")

print(message.sid)