from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, RadioField, StringField, SelectMultipleField, URLField
from wtforms.fields.html5 import EmailField, IntegerField, DecimalRangeField, IntegerRangeField, DecimalField
from wtforms.validators import DataRequired


# Chaque formulaire hérite de Flask-WTF afin de gérer plus facilement la validation des données et la génération des champs HTML


class URLForm(FlaskForm):
    """Formulaire de connexion"""

    url_field = URLField("Adresse e-mail", validators=[DataRequired()])
    password = PasswordField("Mot de passe", validators=[DataRequired()])
   

class LoginForm(FlaskForm):
    """Formulaire de connexion"""

    email = EmailField("Adresse e-mail", validators=[DataRequired()])
    comment = StringField("Mot de passe", validators=[DataRequired()])
    