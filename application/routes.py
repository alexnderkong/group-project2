from flask import render_template, request
from application import app
from application.models import Users
from application.forms import NameForm
from application.ref_gen import ref_gen
from application.prize_gen import random_prize


@app.route('/')
@app.route('/home', methods=['GET','POST'])
def home():
    form = NameForm()
    if form.validate_on_submit():
        ref2 = ref_gen()
        prize = random_prize()
        print(prize)
    return render_template('index.html', title='home', form=form)
    
    
# letters = random_letters()
# numbers = random_numbers()
# id_list = letters + numbers
# id_string = ''.join(id_list)
# prize = random_prize()
# print(id_string)
# print(prize)
