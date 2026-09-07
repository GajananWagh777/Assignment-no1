class Upi:

    def payment(self):
        print("Payment by Upi")


class Creditcard:

    def payment(self):
        print("Payment by Creditcard")


class Debitcard:

    def payment(self):
        print("Payment by Debitcard")


class Payment:

    def __init__(self, strategy):
        self.strategy = strategy

    def start(self):
        self.strategy.payment()


choice = int(input("Enter your choice"))

match choice:

    case 1:
        p = Payment(Upi())
        p.start()

    case 2:
        p = Payment
