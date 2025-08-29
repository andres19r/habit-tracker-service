from datetime import datetime


class User:
    def __init__(self, id, first_name, last_name, username, email, password) -> None:
        if not isinstance(first_name, str) or not first_name:
            raise ValueError("Firstname must be a non-empty string")
        if not isinstance(last_name, str) or not last_name:
            raise ValueError("Lastname must be a non-empty string")
        if not isinstance(username, str) or not username:
            raise ValueError("Username must be a non-empty string")
        if not isinstance(email, str) or not email:
            raise ValueError("Email must be a non-empty string")
        if not isinstance(password, str) or not password:
            raise ValueError("Password must be a non-empty string")

        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.created_at = datetime.now()
        self.udpated_at = None

    def to_dict(self):
        """Converts the User object to a dictionary"""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
            "updated_at": self.udpated_at,
        }

    @staticmethod
    def from_dict(data):
        """Creates a User object from a dictionary"""
        return User(
            id=data["id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            username=data["username"],
            email=data["email"],
            password=data["password"],
        )
