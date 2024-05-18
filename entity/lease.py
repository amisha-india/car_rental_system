#Lease model to manage the deatil
class Lease:
    def __init__(self,lease_id ,vehicle_id,customer_id,start_date,end_date,type):
        self.__lease_id = lease_id
        self.__vehicle_id = vehicle_id
        self.__customer_id = customer_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__type = type

    def get_lease_id(self):
        return self.__lease_id
    
    def set_lease_id(self, lease_id):
        self.__lease_id = lease_id

    def get_lease(self):
        return {"lease_id":self.__lease_id,"vehicle_id": self.__vehicle_id,"customer_id": self.__customer_id,"start_date": self.__start_date,"end_date": self.__end_date,"Type": self.__type}