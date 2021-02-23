from __main__ import db

class UserData(db.Model):
    __tablename__ = 'user_data'

    ud_id = db.Column(db.Integer, primary_key=True)
    ud_forename = db.Column(db.String(50))
    ud_surname = db.Column(db.String(50))
    ud_birthyear = db.Column(db.Integer)
    ud_email = db.Column(db.String(50), unique=True)
    ud_password = db.Column(db.String(100))
    ud_gender = db.Column(db.Enum('M', 'F', 'NB', name='gender'))
    ud_twitter = db.Column(db.String(50), unique=True)

    def __init__(self, forename, surname, birthyear, email, password, gender, twitter=''):
        self.ud_forename = forename
        self.ud_surname = surname
        self.ud_birthyear = birthyear
        self.ud_email = email
        self.ud_password = password
        self.ud_gender = gender
        self.ud_twitter = ''
    
    def serialise(self):
        return {
            'id': self.user_id,
            'forename': self.ud_forename,
            'surname': self.ud_surname,
            'birthyear': self.ud_birthyear,
            'email': self.ud_email,
            'gender': self.ud_gender,
            'twitter': self.ud_twitter
        }