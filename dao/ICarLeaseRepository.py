from abc import ABC, abstractmethod
from entity import Vehicle, Customer, Lease


class Car_management(ABC):
    @abstractmethod
    def add_car(self, vehicle: Vehicle):
        pass

    @abstractmethod
    def remove_car(self,vehicle_id):
        pass

    @abstractmethod
    def list_available_cars(self):
        pass

    @abstractmethod
    def list_rented_cars(self):
        pass

    @abstractmethod
    def find_cars_by_id(self,vehicle_id):
        pass

    @abstractmethod
    def update_car(self,vehicle_id):
        pass

class Customer_management(ABC):

    @abstractmethod
    def add_customer(self, customer:Customer):
        pass

    @abstractmethod
    def remove_customer(self,customer_id):
        pass

    @abstractmethod
    def list_customer(self):
        pass

    @abstractmethod
    def find_customer(self,customer_id):
        pass
    
    @abstractmethod
    def update_customer(self,customer_id):
        pass

    @abstractmethod
    def delete_customer(self,customer_id):
        pass

class Lease_management(ABC):

    @abstractmethod
    def create_lease(self,customer_id,car_id,start_date,end_date,type,lease_id):
        pass

    @abstractmethod
    def return_car(self,lease_id):
        pass

    @abstractmethod
    def list_active_leases(self):
        pass

    @abstractmethod
    def list_lease_history(self):
        pass
    
class Payment_handling():

    @abstractmethod
    def record_payment(self, payment_id,lease:Lease,amount,payment_date):
        pass

    @abstractmethod
    def get_payment(self):
        pass