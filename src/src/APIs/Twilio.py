from twilio.rest import Client
from User import user


def sendSMS(message):
    client = Client(user.twilio[0], user.twilio[1])
    message = client.messages.create(
                                  from_=user.twilio[3],
                                  body= message,
                                  to=user.twilio[2]
                              )
    print(message.sid)