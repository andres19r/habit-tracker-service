from datetime import datetime


class Habit:
    def __init__(self, id, user_id, name, description, target_count, is_active = True) -> None:
        self.id = id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.frequency = 0
        self.target_count = target_count
        self.is_active = is_active
        self.created_at = datetime.now()


    def to_dict(self):
        """Converts the Habit object to a dictionary"""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
            "frequency": self.frequency,
            "target_count": self.target_count,
            "is_active": self.is_active,
            "created_at": self.created_at,
        }

    @staticmethod
    def from_dict(data):
        """Creates a Habit object from a dictionary"""
        return Habit(
            id=data["id"],
            user_id=data["user_id"],
            name=data["name"],
            description=data["description"],
            target_count=data["target_count"],
            is_active=data["is_active"],
        )
