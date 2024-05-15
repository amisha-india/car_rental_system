# Customer model for managing the customer record
class Customer:
    def __init__(self, customerID, first_name, last_name, email, phoneNumber):
        self.__customerID = customerID
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phoneNumber = phoneNumber

    def get_customer(self):
        return {
            "customerID": self.__customerID,
            "first_name": self.__first_name,
            "last_name": self.__last_name,
            "email": self.__email,
            "phoneNumber": self.__phoneNumber,
        }

    def get_customerID(self):
        return self.__customerID
