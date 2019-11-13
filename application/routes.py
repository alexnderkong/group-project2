from flask import render_template, request
from application import app, db
from application.models import Users
from application.forms import NameForm
from application.ref_gen import ref_gen
from application.prize_gen import random_prize


@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    form = NameForm()
    if form.validate_on_submit():
        ref2 = ref_gen()
        prize1 = random_prize()
        print(prize1)
        user=Users(
        	first_name=form.first_name.data,
        	last_name=form.last_name.data,
        	reference=ref2,
        	prize=prize1
           	)
        db.session.add(user)
        db.session.commit()
        return render_template('index.html', title='home', form=form, prize1=prize1, ref2=ref2)
    else:
    	print(form.errors)
    return render_template('index.html', title='home', form=form)
    
    
# letters = random_letters()
# numbers = random_numbers()
# id_list = letters + numbers
# id_string = ''.join(id_list)
# prize = random_prize()
# print(id_string)
# print(prize)
