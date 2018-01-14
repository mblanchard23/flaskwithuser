from app_base import db
class User(db.Model):
    # def __init__(self):
    #     self.isactive = True

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(240), unique=False, nullable=False)
    password = db.Column(db.String(60), unique=False, nullable=False)
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    messages = db.relationship('Message', backref='user', lazy=True)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

    def create_message(self, subject, body):
        new_message = Message(subject=subject, body=body, user_id=self.id)
        db.session.add(new_message)
        db.session.commit()

    def __repr__(self):
        return '<User %r>' % self.username


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(1024), nullable=True)
    body = db.Column(db.String(4096), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')
                        , nullable=False)

    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())


    def __repr__(self):
        return '<Message %r>' % self.subject

