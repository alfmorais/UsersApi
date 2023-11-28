from uuid import UUID


class Users:
    def __init__(self, id: UUID, name: str, email: str, password: str) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.password = password
