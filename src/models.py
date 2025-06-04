from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class FavouritePlanet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    planet_id: Mapped[int] = mapped_column(ForeignKey("planets.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user_id_favourite: Mapped["User"] = relationship(back_populate="user_favourite_planet")
    planet_id_favourite: Mapped["Planets"] = relationship(back_populates="planet_favourites")
  
    def serialize(self):
        return {
            "id": self.id,
        }


class FavouritePeople(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    people_id: Mapped[int] = mapped_column(ForeignKey("people.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    people :Mapped["People"] = relationship(back_populates="people_favourites")
    user: Mapped["User"] = relationship(back_populates="user_favourite_people")

    def serialize(self):
        return {
            "id": self.id,
        }


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)

    people_favourites: Mapped[list["FavouritePeople"]]= relationship(back_populates="user_id_favourite")
    planet_facourites: Mapped[list["FavouritePlanet"]]= relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name
            # do not serialize the password, its a security breach
        }


class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(400), nullable=False)
    description: Mapped[str] = mapped_column(String(120), nullable=False)
    galaxy: Mapped[str] = mapped_column(String(120), nullable=False)
    population: Mapped[str] = mapped_column(String(120), nullable=False)
    gravity: Mapped[int] = mapped_column(nullable=False)
    image: Mapped[str] = mapped_column(String(120), nullable=False)

    favourite_user: Mapped[list["FavouritePlanet"]] = relationship(back_populates="planet_id_favourite")
    people: Mapped[list["People"]]= relationship(back_populates="planet")
  
    def serialize(self):
        return {
            "id": self.id,
            "description": self.description,
            "name": self.name,
            "galaxy": self.galaxy,
            "population": self.population,
            "gravity": self.gravity,
            "image": self.image

        }


class People(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(400), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(String(120), nullable=False)
    height: Mapped[int] = mapped_column(nullable=False)
    weight: Mapped[int] = mapped_column(nullable=False)
    image: Mapped[str] = mapped_column(String(120), nullable=False)
    planet_of_birth: Mapped[int] = mapped_column(ForeignKey("planets.id"))

    planet:Mapped["Planets"] = relationship(back_populates="people")
    favorite_user= Mapped[list["FavouritePeople"]]= relationship(back_populates="people")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "image": self.image,
        }
