from wtforms import Form, StringField, TextAreaField, PasswordField, HiddenField, validators

# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

# Post Form Class
class PostForm(Form):
    id = HiddenField("id")
    title = StringField('Title', [validators.Length(min=1, max=50)])
    body = TextAreaField('Body', [validators.Length(min=30)])


class ContactForm(Form):
    id = HiddenField("id")
    name = StringField("Name", [validators.Length(min=4, max=50)])
    company = StringField("Company", [validators.Length(min=4, max=50)])
    email = StringField("Email", [validators.Length(min=4, max=50)])
    notes = TextAreaField("Notes")