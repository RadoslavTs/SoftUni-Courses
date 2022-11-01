class Email:

    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


input_list = input()
emails = []
while input_list != "Stop":
    separated_list = input_list.split()
    sender = separated_list[0]
    receiver = separated_list[1]
    content = separated_list[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    input_list = input()

send_emails = list(map(int, input().split(", ")))

for sequence in send_emails:
    emails[sequence].send()

for email in emails:
    print(email.get_info())
