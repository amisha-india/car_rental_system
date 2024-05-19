from dao.lCarLeaseRepositoryImpl import *
from entity import *



print("🙌!!.....Welcome.......!!!🙌")
print("!!.....THE CAR RENTAL SYSTEM.....!!")

while True:
    
    print("Please select the options")
    print("1) Customer Operations")
    print("2) Vehicle Operations")
    print("3) Lease Operations")
    print("4) Payment Operations")
    print("5) Exit")

    # car_manage = CarManagementImplementation()
    # customer_manage = CustomerManagementImplementation()
    # lease_manage = LeaseManagementImplementation()
    # payment_manage = PaymentManagementImplementation()

    option = int(input("Option : "))

    if option == 5:
        print("Thank you!!")
        break


    #customer options
    elif option == 1:
        print()
        print("1) Add Customer")
        print("2) Remove Customer")
        print("3) List Customer")
        print("4) Find Customer")
        print("5) Update Customer")
        print("6) Delete Customer")
        print("7) Back")
        sub_option = int(input("Option : "))

        # Add customer
        if sub_option == 1 :
            print("Please provied following details for the customer:")

            first_name = input("First Name : ")
            last_name = input("Last Name : ")
            email = input("Email : ")
            phone_number = input("Phone Number : ")
            customer_id = input("Customer_id :")
            print(" Added successfully ")
            try:
                result = customer_manage.add_customer(customer=Customer(customer_id, first_name, last_name, email, phone_number))
                print(result)
                print("User added successfully !")
            except Exception as e:
                print(f"Error encountered while adding the customers : {e}")

        # Remove Customer
        elif sub_option == 2:
            customer_id = int(input("User ID to remove (Please verify from the list customer option) : "))

            try:
                result = customer_manage.remove_customer(customer_id)
                print(result)
                print("User removed successfully !")
            except Exception as e:
                print(f"Error encountered while adding the customers : {e}")

        # List Customers
        elif sub_option == 3:
            try:
                result = customer_manage.list_customer()
                for customer in result:
                    print(customer.get_customer())
            except Exception as e:
                print(f"Error encountered while listing the customers : {e}")


        # Find Customers
        elif sub_option == 4:
            customer_id = int(input("Customer to find : "))
            try:
                result = customer_manage.find_customer(customer_id)
                for customer in result:
                    print(customer.get_customer())
            except Exception as e:
                print(f"Error encountered while finding customers : {e}")

        #Update Customer
        elif sub_option == 5:
            customer_id = int(input("Customer to update : "))
            try:
                customer_manage.update_customer(customer_id = customer_id)
            except Exception as e:
                print(f"Error encountered while updating customers : {e}")

        elif sub_option == 6:
            customer_id = int(input("Customer to Delete : "))
            try:
                customer_manage.delete_customer(customer_id = customer_id)
            except Exception as e:
                print(f"Error encountered while updating customers : {e}")

        # continue
        elif sub_option == 7:
            continue
        else:
            print("select valid option")

    # Car Options
    elif option == 2:
        print()
        print("Select options")
        print("1) Add Car")
        print("2) Find car by id")
        print("3) List Rented car")
        print("4) List Available car")
        print("5) Remove car")
        print("6) Update car")
        print("7) Back")

        sub_option = int(input("Option : "))

        #Add Car
        if sub_option == 1:
            print("Please provied the following informations")
            vehicle_id = int(input("Vehicle ID :"))
            make = input("Make of the car : ")
            model = input("Model of the car : ")
            Year = input("Year of the car : ")
            daily_rate = float(input("Daily Rate : "))
            status = int(input("Available(1) or unavailable(0)"))
            passenger_capacity = input("Passenger capacity of the car : ")
            engine_capacity = input("Engine Capacity of the car : ")

            try:
                result = car_manage.add_car(Vehicle(vehicle_id, make, model, Year, daily_rate, status, passenger_capacity, engine_capacity))
                print(result)
                print("Successfully added the car!")
            except Exception as e:
                print(f"Error encountered while adding the car : {e}")

        # find car by id
        if sub_option == 2 :
            vehicle_id = int(input("Give car ID : "))

            try:
                cars = car_manage.find_cars_by_id(vehicle_id)
                for car in cars:
                    print(car.get_car_details())

            except Exception as e:
                print(f"Error encountered while getting cars : {e}")

        #List Rented car
        elif sub_option == 3:
            print("List of the rented cars are : ")
            try:
                cars = car_manage.list_rented_cars()
                for car in cars:
                    print(car.get_car_details())

            except Exception as e:
                print(f"Error encountered while getting cars : {e}")

        #List avialabel car
        elif sub_option == 4:
            print("List of the available cars are : ")
            try:
                cars = car_manage.list_available_cars()
                for car in cars:
                    print(car.get_car_details())

            except Exception as e:
                print(f"Error encountered while getting cars : {e}")

        #Remove car
        elif sub_option == 5:
            vehicle_id = int(input("vehicle ID to remove (Verify from list cars) : "))
            try:
                result = car_manage.remove_car(vehicle_id)
                print("Successfully removed car")
            except Exception as e:
                print(f"Error encountered while removing car : {e}")

        elif sub_option == 6 :
            vehicle_id = int(input("Car ID to update (Verify from list cars) : "))
            try:
                result = car_manage.update_car(vehicle_id)
                print("Successfully Updated car")
            except Exception as e:
                print(f"Error encountered while updating car : {e}")

        elif sub_option == 7:
            continue

        else:
            print("Select valid option")
    # Lease Options
    elif option == 3:
        print()
        print("Select Options")
        print("1) Create new Lease")
        print("2) Get Lease ")
        print("3) List Active Lease")
        print("4) List past Lease")
        print("5) Back")

        sub_option = int(input("Option : "))
        #Create new lease
        if sub_option == 1:
            print("Fill following options")
            lease_id = int(input("Lease ID:"))
            vehicle_id = input("Vehicle ID (select from the vehicle list) : ")
            customer_id = input("Customer ID (select from customer list) : ")
            start_date = input("Start Date (yyyy-mm-dd) : ")
            end_date = input("End date (yyyy-mm-dd) : ")
            type = input("dailyBased(0) monthlyBased (1) : ")

            try:
                ret = lease_manage.create_lease(lease_id, vehicle_id, customer_id, start_date, end_date, type)
                print(ret)
                print("Successfully created lease !")
            except Exception as e:
                print(f"Error encountered while adding lease : {e}")

        #Get Lease
        elif sub_option == 2:
            lease_id = int(input("Lease ID : "))

            try:
                leases = lease_manage.return_car(lease_id)
                for lease in leases:
                    print(lease.get_lease())
            except Exception as e:
                print(f"Error encountered while getting lease : {e}")

        # List Active leases
        elif sub_option ==3:
            print("Active leases are")

            try:
                leases = lease_manage.list_active_leases()
                for lease in leases:
                    print(lease.get_lease())
            except Exception as e:
                print(f"Error encountered while getting lease : {e}")

        #List Past leases
        elif sub_option == 4:
            print("Past leases are")

            try:
                leases = lease_manage.list_lease_history()
                for lease in leases:
                    print(lease.get_lease())
            except Exception as e:
                print(f"Error encountered while getting lease : {e}")

        #continue
        elif sub_option ==5:
            continue

        else:
            print("select valid option")

    #Payment operations
    elif option == 4:
        print("Options")
        print("1) New payment")
        print("2) List payment")
        print("3) Back")

        sub_option = int(input("Option : "))

        #New payment
        if sub_option == 1:
            print("Give following information")
            payment_id = int(input("Payment_id:"))
            lease_id = int(input("Lease_id (verify from lease list) : "))
            payment_date = input("Payment Date (yyyy-mm-dd):")
            amount = int(input("Amount : "))

            try:
                result = payment_manage.record_payment(payment_id,lease_id,payment_date,amount)
                print(result)
                print("Successfully added payment!")
            except Exception as e:
                print(f"Error encountered while adding payment : {e}")

        #List Payment
        elif sub_option ==2:
            print("All payments are")
            try:
                result = payment_manage.get_payment()
                for pay in result:
                    print(pay)

            except Exception as e:
                print(f"Error encountered while adding payment : {e}")

        elif sub_option == 5:
            continue

        else:
            print("select valid option")

    else:
        print("select valid option")



if __name__ == "__main__":
    print("Good day😊😊")    


