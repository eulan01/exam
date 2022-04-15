
class Subscriber:
    def __init__(self, first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def __str__(self):
        return f'{self.first_name} {self.last_name}'  

class Terminal:
    def __init__(self):
        self.amount=0
        self.providers= []
    def register(self,provider):
        self.providers.append(provider)
    def pay(self,provider,subscriber,money):
        try:
            provider.register_payment(subscriber,money)
            self.amount+=money  
            print('Удачное завершение!')
        except Exception as _ex:
            print(_ex)


class Provider:
    def __init__(self,name):
        self.name=  name
        self.subscribers = ['Улан']
        self.payments = {}
    def register_payment(self,subscriber, payment):
        if not subscriber in self.subscribers:
            raise ValueError(f'There\'s no {subscriber} in subscribers!')
        self.payments.setdefault(subscriber, payment)