from abc import ABC, abstractmethod


class IContent(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):
    def format(self):
        return '\n'.join(['<myML>', self.value, '</myML>'])


class IReceiver(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def format(self):
        pass


class ISender(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def format(self):
        pass


class IMReceiver(IReceiver):
    def format(self):
        return ''.join(["I'm ", self.value])


class IMSender(ISender):
    def format(self):
        return ''.join(["I'm ", self.value])


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, send):
        pass

    @abstractmethod
    def set_receiver(self, receive):
        pass

    @abstractmethod
    def set_content(self, cont):
        pass


class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, send):
        self.__sender = send.format()

    def set_receiver(self, receive):
        self.__receiver = receive.format()

    def set_content(self, cont):
        self.__content = cont.format()

    def __repr__(self):

        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


email = Email('IM')
sender = IMSender('qmal')
receiver = IMReceiver('james')
content = MyContent('Hello, there!')

email.set_sender(sender)
email.set_receiver(receiver)
email.set_content(content)

print(email)
