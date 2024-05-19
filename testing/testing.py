import unittest

from exceptions.custom_excp import *
from dao.lCarLeaseRepositoryImpl import *
from entity import *


class Test_cases(unittest.TestCase):
    def setUp(self):
        self.car = Car_management_implementation()
        self.lease_manage = Lease_management_implementation()
        self.customor =Customer_management_implementation()

    def car_create_test(self):
        result = self.car.add_Car(Vehicle(1, make="alto", model="maruti", Year="2024", daily_rate="25", status="1", passenger_capacity="25", engine_capacity="2456"))

        self.assertEqual(result, "Car added successfully")

    def lease_creat_test(self):
        result = self.lease_manage.create_lease(customer_id=200,  start_date = "2024-05-01", end_date="2024-06-01", type="1",vehicle_id=3)
        self.assertEqual(result,"Lease created successfully")
 
    def find_customer_exp_test(self):
        with self.assertRaises(CarNotFoundException):
            self.customor.find_custmoer(24)

    def lease_retrive_test(self):
        result = self.lease_manage.list_lease_history()
        self.assertNotEqual(len(result),0)

    def find_car_exp_test(self):
        with self.assertRaises(CarNotFoundException):
            self.car.find_cars_by_id(110)

    def find_lease_exp_test(self):
        with self.assertRaises(LeaseNotFoundException):
            self.lease_manage.return_car(23)

    

if __name__ == "__main__":
    unittest.main()
