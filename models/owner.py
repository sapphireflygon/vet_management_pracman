from socket import INADDR_ALLHOSTS_GROUP


class Owner:
    def __init__(self, input_name, input_phone_number, input_email, input_address, id=None):
        self.id = id
        self.name = input_name
        self.phone_number = input_phone_number
        self.email = input_email
        self.address = input_address