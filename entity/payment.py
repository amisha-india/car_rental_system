# payment model for managing payment related things
from datetime import date


class Payment:
    def _init_(self, payment_id, lease_id, payment_date: date, amount: float):
        self.set_payment_id = payment_id
        self.set_lease_id = lease_id
        self.set_payment_date = payment_date
        self.set_amount = amount

    # Getting Payment ID
    def get_payment_id(self):
        return self._payment_id

    def set_payment_id(self, value):
        if value <= 0:
            raise ValueError("Payment ID must be a positive integer.")
        self._payment_id = value

    # Getting Lease ID
    def get_lease_id(self):
        return self._lease_id

    def set_lease_id(self, value):
        if value <= 0:
            raise ValueError("Lease ID must be a positive integer.")
        self._lease_id = value

    # Getting Payment Date
    def get_payment_date(self):
        return self._payment_date

    def set_payment_date(self, value):
        self._payment_date = value

    # Getting Amount
    def get_amount(self):
        return self._amount

    def set_amount(self, value):
        if value < 0:
            raise ValueError("Amount must be a non-negative value.")
        self._amount = value
