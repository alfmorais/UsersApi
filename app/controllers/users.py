from uuid import UUID

from app.config.database import database


class UserController:
    @classmethod
    def save(id: UUID, name: str, email: str, password: str) -> None:
        database.db.users.insert_one(
            {
                "id": id,
                "name": name,
                "email": email,
                "password": password,
            }
        )

    @classmethod
    def find_all(cls):
        return database.db.users.find()

    @classmethod
    def find_one(id: UUID):
        return database.db.users.find_one({"id": id})
