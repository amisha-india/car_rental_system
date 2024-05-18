# Customer model for managing the customer record
class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number

    def get_customer(self):
        return {
            "customer_id": self.__customer_id,
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "email": self.__email,
            "phone_number": self.__phone_number,
        }

    def get_customer_id(self):
        return self.__customer_id
