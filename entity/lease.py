#Lease model to manage the deatil
class Lease:
    def __init__(self,leaseID ,vehicleId,customerID,startDate,endDate,type):
        self.__leaseId = leaseID
        self.__vehicleId = vehicleId
        self.__customerID = customerID
        self.__startDate = startDate
        self.__endDate = endDate
        self.__type = type

    def get_lease_id(self):
        return self.__leaseId
    
    def set_lease_id(self, leaseID):
        self.__leaseId = leaseID

    def get_lease(self):
        return {"leaseID":self.__leaseId,"vehicleID": self.__vehicleId,"customerID": self.__customerID,"startDate": self.__startDate,"endDate": self.__endDate,"Type": self.__type}