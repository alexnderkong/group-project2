from flask import render_template, request
from application import app, db
from application.models import Users
from application.forms import NameForm
import json
import boto3
kong = boto3.client('lambda', region_name='eu-west-1', aws_access_key_id='AWS_ACCESS_KEY_ID', aws_secret_access_key='AWS_SECRET_ACCESS_KEY')
@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def home():
    form = NameForm()
    if form.validate_on_submit():
        temp = kong.invoke(FunctionName='ref_gen',
                        InvocationType='RequestResponse')     
        ref2 = json.loads(temp['Payload'].read().decode('utf-8'))
        
        temp = kong.invoke(FunctionName='prize-gen',
                        InvocationType='RequestResponse')     
        prize1 = json.loads(temp['Payload'].read().decode('utf-8')) 
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
