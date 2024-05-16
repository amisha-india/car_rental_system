from abc import ABC, abstractmethod
from entity import Vehicle, Customer, Lease


class CarManagement(ABC):
    @abstractmethod
    def addCar(self, vehicle: Vehicle):
        pass

    @abstractmethod
    def removeCar(self,vehicleID):
        pass

    @abstractmethod
    def listAvailableCars(self):
        pass

    @abstractmethod
    def listRentedCars(self):
        pass

    @abstractmethod
    def findCarsById(self,vehicleID):
        pass

class CustomerManagement(ABC):

    @abstractmethod
    def addCustomer(self, customer:Customer):
        pass

    @abstractmethod
    def removeCustomer(self,customerID):
        pass

    @abstractmethod
    def listCustomer(self):
        pass

    @abstractmethod
    def findCustomer(self,customerID):
        pass

class LeaseManagement(ABC):

    @abstractmethod
    def createLease(self,customerID,carID,startDate,endDate,type):
        pass

    @abstractmethod
    def returnCar(self,leaseID):
        pass

    @abstractmethod
    def listActiveLeases(self):
        pass

    @abstractmethod
    def listLeaseHistory(self):
        pass

class PaymentHandling():

    @abstractmethod
    def recordPayment(self, lease:Lease,amount,paymentDate):
        pass