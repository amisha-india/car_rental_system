class Vehicle:
    def __init__(
        self,
        vehicleID,
        make,
        model,
        Year,
        dailyRate,
        status,
        passenger_capacity,
        engine_capacity,
    ):
        self.__vehicleID = vehicleID

        self.__make = make

        self.__model = model

        self.__Year = Year

        self.__dailyRate = dailyRate

        self.__status = status

        self.__passenger_capacity = passenger_capacity

        self.__engine_capacity = engine_capacity

    # For getting the car details
    def get_car_details(self):
        return {
            "vehicleID": self.__vehicleID,
            "make": self.__make,
            "model": self.__model,
            "Year": self.__Year,
            "dailyRate": self.__dailyRate,
            "status": self.__status,
            "passenger_capacity": self.__passenger_capacity,
            "engine_capacity": self.__engine_capacity,
        }

    def set_car_details(
        self,
        vehicleID,
        make,
        model,
        Year,
        dailyRate,
        status,
        passenger_capacity,
        engine_capacity,
    ):
        self.__vehicleID = vehicleID

        self.__make = make

        self.__model = model

        self.__Year = Year

        self.__dailyRate = dailyRate

        self.__status = status

        self.__passenger_capacity = passenger_capacity

        self.__engine_capacity = engine_capacity

    def get_vehicleID(self):
        return self.__vehicleID

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_Year(self):
        return self.__Year

    def get_dailyRate(self):
        return self.__dailyRate

    def get_status(self):
        return self.__status

    def get_passenger_capacity(self):
        return self.__passenger_capacity

    def get_engile_capacity(self):
        return self.__engine_capacity
