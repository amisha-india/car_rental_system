class Vehicle:
    def __init__(
        self,
        vehicle_id,
        make,
        model,
        Year,
        daily_rate,
        status,
        passenger_capacity,
        engine_capacity,
    ):
        self.__vehicle_id = vehicle_id

        self.__make = make

        self.__model = model

        self.__Year = Year

        self.__daily_rate = daily_rate

        self.__status = status

        self.__passenger_capacity = passenger_capacity

        self.__engine_capacity = engine_capacity

    # For getting the car details
    def get_car_details(self):
        return {
            "vehicle_id": self.__vehicle_id,
            "make": self.__make,
            "model": self.__model,
            "Year": self.__Year,
            "daily_rate": self.__daily_rate,
            "status": self.__status,
            "passenger_capacity": self.__passenger_capacity,
            "engine_capacity": self.__engine_capacity,
        }

    def set_car_details(
        self,
        vehicle_id,
        make,
        model,
        Year,
        daily_rate,
        status,
        passenger_capacity,
        engine_capacity,
    ):
        self.__vehicle_id = vehicle_id

        self.__make = make

        self.__model = model

        self.__Year = Year

        self.__daily_rate = daily_rate

        self.__status = status

        self.__passenger_capacity = passenger_capacity

        self.__engine_capacity = engine_capacity

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_Year(self):
        return self.__Year

    def get_daily_rate(self):
        return self.__daily_rate

    def get_status(self):
        return self.__status

    def get_passenger_capacity(self):
        return self.__passenger_capacity

    def get_engile_capacity(self):
        return self.__engine_capacity
