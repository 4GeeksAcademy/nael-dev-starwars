from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship

db = SQLAlchemy()


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
   


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    


class Planets(db.Model):
    id:Mapped[int]= mapped_column(primary_key=True)
    name: Mapped[str]= mapped_column(String(400), nullable=False)
    description: Mapped[str]= mapped_column(String(120), nullable= False)
    galaxy: Mapped[str]= mapped_column(String(120), nullable= False)
    population: Mapped[str]= mapped_column(String(120), nullable= False)
    gravity: Mapped[int]= mapped_column( nullable= False)
    image: Mapped[str]= mapped_column(String(120), nullable= False)


    people: Mapped[list["People"]] = relationship(back_populates="planet")
    def serialize(self):
        return {
            "id": self.id,
            "description": self.description,
            "name": self.name,
            "galaxy":self.galaxy,
            "population":self.population,
            "gravity":self.gravity,
            "image":self.image
            # do not serialize the password, its a security breach
        }
    

class People(db.Model):
    id:Mapped[int]= mapped_column(primary_key=True)
    name: Mapped[str]= mapped_column(String(400), nullable=False)
    age: Mapped[int]= mapped_column( nullable= False)
    gender: Mapped[str]= mapped_column(String(120), nullable= False)
    height: Mapped[int]= mapped_column( nullable= False)
    weight: Mapped[int]= mapped_column( nullable= False)
    image: Mapped[str]= mapped_column(String(120), nullable= False)
    planet_of_birth:Mapped[int] = mapped_column(ForeignKey("planets.id"))

    planet: Mapped["Planets"] = relationship(back_populates="people")



    def serialize(self):
        return{
        "id":self.id,
        "name":self.name,
        "age":self.age,
        "gender":self.gender,
        "height":self.height,
        "weight":self.weight,
        "image":self.image,
        }

class FavouritePlanet(db.Model);
    id: Mapped[int]= mapped_column(primary_key= True)
    planet_id:Mapped[int] = mapped_column(ForeignKey("planet.id"))
    user_id:Mapped[int] = mapped_column(ForeignKey("user.id"))
    
    def serialize(self):
        return{
            "id":self.id,
        }
    
class FavouritePeople(db.Model):
    id: Mapped[int]= mapped_column(primary_key= True)
    people_id:Mapped[int] = mapped_column(ForeignKey("people.id"))
    user_id:Mapped[int] = mapped_column(ForeignKey("user.id"))

    def serialize(self):
        return{
            "id":self.id,
        }