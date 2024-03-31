from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user

from src.models.forms.forms import SignUpForm
from src.models.models.models import Users
from src.db.config import app

signup = Blueprint('operation', __name__, template_folder='templates')


@signup.route('/', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        name = form.name.data
        phone = form.phone.data
        email = form.email.data
        password = form.password.data

        is_user = Users.get_current(email)

        try:
            if is_user:
                message = 'Пользователь уже существует, попробуйте снова!'
                return render_template('signup.html', message)
            else:
                new_user = Users.create(
                    first_name=name,
                    phone_number=phone,
                    user_email=email,
                    user_password=password
                )
                login_user(new_user)

                return redirect(url_for('index.html'))
        except Exception as e:
            app.logger.error(str(e))

    return render_template('signup.html', form=form)
