from util import DBConnUtil,PropertyUtil
from dao.ICarLeaseRepository import *
from exceptions.custom_excp import *
from entity import Vehicle

class CarManagementImplementation(CarManagement):
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    def addCar(self, vehicle: Vehicle):
        carInfo = vehicle.get_car_details()
        stmt = self.conn.cursor()
        stmt.execute(
            f"INSERT INTO vehicle_table(make, model, Year, dailyRate, status, passenger_capacity, engine_capacity) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (carInfo['make'], carInfo['model'], carInfo['Year'] + "-01-01", carInfo['dailyRate'], carInfo['status'], carInfo['passenger_capacity'], carInfo['engine_capacity'])
        )
        self.conn.commit()
        return "Car added successfully"

    def findCarsById(self, vehicleID):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM vehicle_table WHERE vehicleID = ?", (vehicleID,))
        rows = stmt.fetchall()
        if not rows:
            raise CarNotFoundException()
        return [Vehicle(*row) for row in rows]

    def listAvailableCars(self):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM vehicle_table WHERE status = 1")
        rows = stmt.fetchall()
        if not rows:
            raise CarNotFoundException()
        return [Vehicle(*row) for row in rows]

    def listRentedCars(self):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM vehicle_table WHERE status = 0")
        rows = stmt.fetchall()
        if not rows:
            raise CarNotFoundException()
        return [Vehicle(*row) for row in rows]

    def removeCar(self, vehicleID):
        self.findCarsById(vehicleID)
        stmt = self.conn.cursor()
        stmt.execute(f"DELETE FROM vehicle_table WHERE vehicleID = ?", (vehicleID,))
        self.conn.commit()
        return "Car removed successfully"

    def update_car(self, vehicleID):
        Vehicle = self.findCarsById(vehicleID)
        for Vehicle in Vehicle:
            print(Vehicle.get_car_details())
        print("Select value to update ")
        print("1) Make")
        print("2) Model")
        print("3) Year")
        print("4) Daily Rate")
        print("5) Status")
        print("6) Passenger Capacity")
        print("7) Engine Capacity")
        val_change = "not selected "
        option = int(input("Option : "))
        if option == 1:
            val_change = "make"
        elif option == 2:
            val_change = "model"
        elif option == 3:
            val_change = "Year"
        elif option == 4:
            val_change = "dailyRate"
        elif option == 5:
            val_change = "status"
        elif option == 6:
            val_change = "passenger_capacity"
        elif option == 7:
            val_change = "engine_capacity"

        value = input(f"New Value for the {val_change} : ")
        if option == 3:
            value = value + "-01-01"
        stmt = self.conn.cursor()
        stmt.execute(f"UPDATE vehicle_table SET {val_change} = ? WHERE vehicleID = ?", (value, vehicleID))
        self.conn.commit()
        print("Value updated successfully")

class CustomerManagementImplementation(CustomerManagement):
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    def addCustomer(self, customer: Customer):
        stmt = self.conn.cursor()
        cust_info = customer.get_customer()
        cust_info = customer.get_customerID
        stmt.execute(
            f"INSERT INTO customer_table(customerID, first_name, last_name, email, phoneNumber) VALUES (?, ?, ?, ?,?)",
            (cust_info['customerID'],cust_info['first_name'], cust_info['last_name'], cust_info['email'], cust_info['phoneNumber'])
        )
        self.conn.commit()
        return "Customer added successfully"

    def removeCustomer(self, customerID):
        self.findCustomer(customerID)
        stmt = self.conn.cursor()
        stmt.execute(f"DELETE FROM customer_table WHERE customerID = ?", (customerID,))
        self.conn.commit()
        return "Customer removed successfully"

    def listCustomer(self):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM customer_table")
        rows = stmt.fetchall()
        if not rows:
            raise CustomerrNotFoundException()
        return [Customer(*row) for row in rows]

    def update_customer(self, customer_id):
        self.findCustomer(customer_id)
        print("Select value to update ")
        print("1) First name")
        print("2) Last name")
        print("3) Email")
        print("4) Phone Number")
        val_change = "not selected "
        option = int(input("Option : "))
        if option == 1:
            val_change = "first_name"
        elif option == 2:
            val_change = "last_name"
        elif option == 3:
            val_change = "email"
        elif option == 4:
            val_change = "phoneNumber"

        value = input(f"New Value for the {val_change} : ")
        stmt = self.conn.cursor()
        stmt.execute(f"UPDATE customer_table SET {val_change} = ? WHERE customerID = ?", (value, customer_id))
        self.conn.commit()
        print("Value updated successfully")

    def delete_customer(self, customerID):
        self.findCustomer(customerID)
        stmt = self.conn.cursor()
        stmt.execute(f"DELETE FROM customer_table WHERE customerID = ?", (customerID,))
        self.conn.commit()
        print("Customer deleted successfully")

    def findCustomer(self, customerID):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM customer_table WHERE customerID = ?", (customerID,))
        rows = stmt.fetchall()
        if not rows:
            raise CustomerrNotFoundException()
        return [Customer(*row) for row in rows]

class LeaseManagementImplementation(LeaseManagement):
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    def createLease(self, customerID, carID, startDate, endDate, type):
        stmt = self.conn.cursor()
        try:
            stmt.execute(
                f"INSERT INTO lease_table(vehicleId, customerID, startDate, endDate, type) VALUES (?, ?, ?, ?, ?)",
                (carID, customerID, startDate, endDate, type)
            )
        except Exception as e:
            print(f"Error while creating lease: {e}")
        self.conn.commit()
        return "Lease created successfully"

    def returnCar(self, leaseID):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM lease_table WHERE leaseID = ?", (leaseID,))
        rows = stmt.fetchall()
        return [Lease(*row) for row in rows]

    def listActiveLeases(self):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM lease_table WHERE endDate > CURRENT_DATE")
        rows = stmt.fetchall()
        return [Lease(*row) for row in rows]

    def listLeaseHistory(self):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM lease_table WHERE endDate < CURRENT_DATE")
        rows = stmt.fetchall()
        return [Lease(*row) for row in rows]

class PaymentManagementImplementation(PaymentHandling):
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    def recordPayment(self, leaseID, amount, paymentDate):
        stmt = self.conn.cursor()
        stmt.execute(
            f"INSERT INTO payment_table(leaseID, paymentDate, amount) VALUES (?, ?, ?)",
            (leaseID, paymentDate, amount)
        )
        self.conn.commit()
        return "Payment recorded successfully"

    def getPayment(self):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM payment_table")
        rows = stmt.fetchall()
        return [{"paymentID": row[0], "leaseID": row[1], "paymentDate": row[2], "amount": row[3]} for row in rows]
    

#Initiliasing
car_manage = CarManagementImplementation()
customer_manage = CustomerManagementImplementation()
lease_manage = LeaseManagementImplementation()
payment_manage = PaymentManagementImplementation()