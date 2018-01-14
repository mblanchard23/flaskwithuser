''' Create fake data'''

import requests, random
from bs4 import BeautifulSoup
from webapp import db, User, Message
from faker import Faker

def create_fake_user(bcrypt):
    f = Faker()
    new_user = User(email=f.email()
                    , username=f.user_name()
                    , name=f.name()
                    , password=bcrypt.generate_password_hash(f.password()).decode('utf-8'))
    db.session.add(new_user)
    db.session.commit()
    return new_user.name


def get_lorem_ipsum():
    req = requests.get('https://loripsum.net/api/1/short/headers')
    soup = BeautifulSoup(req.text, 'html.parser')
    subject = soup.find('h1').text
    body = soup.find('p').text
    return {'subject': subject, 'body': body}


def create_fake_message(user_id = None):
    if not user_id:
        user_id = random.randint(0,50)
    new_message = Message(user_id=user_id, **get_lorem_ipsum())
    db.session.add(new_message)
    db.session.commit()
    return new_message.subject
