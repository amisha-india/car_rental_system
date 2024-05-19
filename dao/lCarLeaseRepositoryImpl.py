from util import *
from dao import *
from exceptions.custom_excp import *
from datetime import date
class Car_management_implementation(Car_management):
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    def add_car(self, vehicle: Vehicle):
        car_info = vehicle.get_car_details()
        stmt = self.conn.cursor()
        stmt.execute(
            f"INSERT INTO vehicle_table(vehicle_id,make, model, Year, daily_rate, status, passenger_capacity, engine_capacity) VALUES (?,?, ?, ?, ?, ?, ?, ?)",
            (car_info['vehicle_id'],car_info['make'], car_info['model'], car_info['Year'] + "-01-01", car_info['daily_rate'], car_info['status'], car_info['passenger_capacity'], car_info['engine_capacity'])
        )
        self.conn.commit()
        return "Car added successfully"

    def find_cars_by_id(self, vehicle_id):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM vehicle_table WHERE vehicle_id = ?", (vehicle_id,))
        rows = stmt.fetchall()
        if not rows:
            raise CarNotFoundException()
        return [Vehicle(*row) for row in rows]

    def list_available_cars(self):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM vehicle_table WHERE status = 1")
        rows = stmt.fetchall()
        if not rows:
            raise CarNotFoundException()
        return [Vehicle(*row) for row in rows]

    def list_rented_cars(self):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM vehicle_table WHERE status = 0")
        rows = stmt.fetchall()
        if not rows:
            raise CarNotFoundException()
        return [Vehicle(*row) for row in rows]

    def remove_car(self, vehicle_id):
        self.find_cars_by_id(vehicle_id)
        stmt = self.conn.cursor()
        stmt.execute(f"DELETE FROM vehicle_table WHERE vehicle_id = ?", (vehicle_id,))
        self.conn.commit()
        return "Car removed successfully"

    def update_car(self, vehicle_id):
        Vehicle = self.find_cars_by_id(vehicle_id)
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
            val_change = "daily_rate"
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
        stmt.execute(f"UPDATE vehicle_table SET {val_change} = ? WHERE vehicle_id = ?", (value, vehicle_id))
        self.conn.commit()
        print("Value updated successfully")

class Customer_management_implementation(Customer_management):
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    # def add_customer(self, customer: Customer):
    #     stmt = self.conn.cursor()
    #     cust_info = customer.get_customer()
    #     cust_info = customer.get_customer_id()
    #     stmt.execute(
    #         f"INSERT INTO customer_table(customer_id, first_name, last_name, email, phone_number) VALUES (?, ?, ?, ?,?)",
    #         (cust_info['customer_id'],cust_info['first_name'], cust_info['last_name'], cust_info['email'], cust_info['phone_number'])
    #     )
    #     self.conn.commit()
    #     return "Customer added successfully"

    def add_customer(self, customer: Customer):
        stmt = self.conn.cursor()
        cust_info = customer.get_customer()
        stmt.execute(
            f"INSERT INTO customer_table(customer_id, first_name, last_name, email, phone_number) VALUES (?, ?, ?, ?,?)",
            (cust_info['customer_id'], cust_info['first_name'],
            cust_info['last_name'], cust_info['email'], cust_info['phone_number'])
            )
        self.conn.commit()
        return "Customer added successfully"





    def remove_customer(self, customer_id):
        self.find_customer(customer_id)
        stmt = self.conn.cursor()
        stmt.execute(f"DELETE FROM customer_table WHERE customer_id = ?", (customer_id,))
        self.conn.commit()
        return "Customer removed successfully"

    def list_customer(self):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM customer_table")
        rows = stmt.fetchall()
        if not rows:
            raise CustomerrNotFoundException()
        return [Customer(*row) for row in rows]

    def update_customer(self, customer_id):
        self.find_customer(customer_id)
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
            val_change = "phone_number"

        value = input(f"New Value for the {val_change} : ")
        stmt = self.conn.cursor()
        stmt.execute(f"UPDATE customer_table SET {val_change} = ? WHERE customer_id = ?", (value, customer_id))
        self.conn.commit()
        print("Value updated successfully")

    def delete_customer(self, customer_id):
        self.find_customer(customer_id)
        stmt = self.conn.cursor()
        stmt.execute(f"DELETE FROM customer_table WHERE customer_id = ?", (customer_id,))
        self.conn.commit()
        print("Customer deleted successfully")

    def find_customer(self, customer_id):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM customer_table WHERE customer_id = ?", (customer_id,))
        rows = stmt.fetchall()
        if not rows:
            raise CustomerrNotFoundException()
        return [Customer(*row) for row in rows]

class Lease_management_implementation(Lease_management):
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    def create_lease(self, lease_id, vehicle_id, customer_id, start_date, end_date, type):
        stmt = self.conn.cursor()
        try:
            stmt.execute(
                f"INSERT INTO lease_table(lease_id, vehicle_id, customer_id, start_date, end_date, type) VALUES (?, ?, ?, ?, ?,?)",
                (lease_id, vehicle_id, customer_id, start_date, end_date, type)
            )
        except Exception as e:
            print(f"Error while creating lease: {e}")
        self.conn.commit()
        return "Lease created successfully"

    def return_car(self, lease_id):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM lease_table WHERE lease_id = ?", (lease_id,))
        rows = stmt.fetchall()
        return [Lease(*row) for row in rows]

    def list_active_leases(self):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM lease_table WHERE end_date > CURRENT_TIMESTAMP ")
        rows = stmt.fetchall()
        return [Lease(*row) for row in rows]

    def list_lease_history(self):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM lease_table WHERE end_date < CURRENT_TIMESTAMP ")
        rows = stmt.fetchall()
        return [Lease(*row) for row in rows]
    

class Payment_management_implementation(Payment_handling):
    def __init__(self):
        self.conn = DBConnUtil.getConnection()

    def record_payment(self,payment_id, lease_id, payment_date, amount):
        stmt = self.conn.cursor()
        stmt.execute(
            f"INSERT INTO payment_table(payment_id,lease_id, payment_date, amount) VALUES (?,?, ?, ?)",
            (payment_id,lease_id, payment_date, amount)
        )
        self.conn.commit()
        return "Payment recorded successfully"

    def get_payment(self):
        stmt = self.conn.cursor()
        stmt.execute(f"SELECT * FROM payment_table")
        rows = stmt.fetchall()
        return [{"payment_id": row[0], "lease_id": row[1], "payment_date": row[2], "amount": row[3]} for row in rows]
    

#Initiliasing
car_manage = Car_management_implementation()
customer_manage = Customer_management_implementation()
lease_manage = Lease_management_implementation()
payment_manage = Payment_management_implementation()