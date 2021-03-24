from models import db, Pet
from app import app


# Create all tables
db.drop_all()
db.create_all()

# Make a bunch of departments
p1 = Pet(name='scarlet', species='cat', photo_url='https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Siam_lilacpoint.jpg/330px-Siam_lilacpoint.jpg', age=10, notes='nice cat', available=False)
p2 = Pet(name='bonny', species='dog', photo_url='https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Labrador_on_Quantock_%282175262184%29.jpg/330px-Labrador_on_Quantock_%282175262184%29.jpg', available=True)
p3 = Pet(name='fred', species='rabbit', photo_url='', age=10, notes='nice cat')


db.session.add_all([p1,p2,p3])
db.session.commit()