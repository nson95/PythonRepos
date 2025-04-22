from dataclasses import dataclass

@dataclass
class Person:
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str

    def to_string(self):
        return f'Person: id:{self.id}, name: {self.first_name} {self.last_name}, email: {self.email}, phone {self.phone} '