from flask import Flask, render_template, redirect, request
from models import Pet, db, connect_db
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm, EditPetForm


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoptions'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] = "secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def show_pets():

    pets = Pet.query.all()

    return render_template('petList.html', pets=pets)


@app.route('/add', methods=['POST', 'GET'])
def add_pet():

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        new_Pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)

        db.session.add(new_Pet)
        db.session.commit()
        

        return redirect('/')
    
    else:
        return render_template('addPetForm.html', form=form)

@app.route('/<int:pet_id>', methods=['POST','GET'])
def display_edit_form(pet_id):

    pet = Pet.query.get(pet_id)

    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        pet.photo_url=photo_url
        pet.notes=notes
        pet.available=available

        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:

        return render_template('/petProfile.html',pet=pet,form=form)





