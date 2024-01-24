from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL


class URLForm(FlaskForm):
    original_link = URLField(
        'Введите оригинальную ссылку',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 256),
                    URL(message='Некорректный адрес ссылки')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки по желанию',
        validators=[
            Length(1, 16),
            Optional()
        ]
    )
    submit = SubmitField('Создать')