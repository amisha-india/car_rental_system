class PropertyUtil:
    @staticmethod
    def get_property_string():
        server_name = "Amarjeet\SQLEXPRESS"
        database_name = "Car_rental_system"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

        return conn_str