class EmailNotification:
    def sendNotification(self):
        print("Sending notification via Email")


class SMSNotification:
    def sendNotification(self):
        print("Sending notification via SMS")


class WhatsAppNotification:
    def sendNotification(self):
        print("Sending notification via WhatsApp")


notifications = [
    EmailNotification(),
    SMSNotification(),
    WhatsAppNotification()
]

for notification in notifications:
    notification.sendNotification()