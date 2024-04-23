from pydantic import BaseModel


class Animal(BaseModel):
    cats: int
    dogs: int

class Shelter(BaseModel):
    name: str
    address: str
    animals: Animal