class IllegalArgumentError(ValueError):
    pass


class Package():
    package_id: int
    delivery_address: str
    delivery_deadline: str
    delivery_city: str
    delivery_zip: int
    weight: int
    status: str

    def __init__(self, package_id: int, delivery_address: str, delivery_deadline: str, delivery_city: str, delivery_zip: int, weight: int, status: str):
        statuses = ['delayed on flight', 'in route', 'delivered']

        if (status not in statuses):
            raise IllegalArgumentError(
                f"'{status}' is not a valid value for the package status")

        self.package_id = package_id
        self.delivery_address = delivery_address
        self.delivery_deadline = delivery_deadline
        self.delivery_city = delivery_city
        self.delivery_zip = delivery_zip
        self.weight = weight
        self.status = status
