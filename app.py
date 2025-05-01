from sqlmodel import Session,  select
from database import *
from models import *


session = Session(engine)

hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


with session as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()


statement = select(Hero).where(Hero.name == "Spider-Boy")
hero = session.exec(statement).all()
print(hero)
session.close()