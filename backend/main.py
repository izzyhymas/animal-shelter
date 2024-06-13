from models import Animal, Shelter

from fastapi import FastAPI


app = FastAPI()

# Make the pydantic model `Shelter` that will represent this data, then manually
# change this list to be a list[Shelter]. You don't need to write code to convert
# this list, just manually change it by hand.

shelters: list[Shelter] = [
    Shelter(
        name="St. George Animal Shelter",
        address="605 Waterworks Dr, St. George, UT 84770",
        animals=Animal(cats=13, dogs=15)
    ),
    Shelter(
        name="St. George Paws",
        address="1125 W 1130 N, St. George, UT 84770",
        animals=Animal(cats=12, dogs=9)
    ),
    Shelter(
        name="Animal Rescue Team",
        address="1838 W 1020 N Ste. B, St. George, UT 84770",
        animals=Animal(cats=4, dogs=7)
    )
]

@app.get("/shelters")
async def get_shelters() -> list[Shelter]:
    return shelters

@app.post("/shelters")
async def add_shelter(shelter: Shelter) -> None:
    shelters.append(shelter)

@app.put("/shelters/{shelter_name}")
async def update_shelter(shelter_name: str, updated_shelter: Shelter) -> None:
    for i, shelter in enumerate(shelters):
        if shelter.name == shelter_name:
            shelters[i] = updated_shelter
            return

@app.delete("/shelters/{shelter_name}")
async def delete_shelter(shelter_name: str) -> None:
    for i, shelter in enumerate(shelters):
        if shelter.name == shelter_name:
            shelters.pop(i)
            return  