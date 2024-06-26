from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL, ValidationError

from .constants import SHORT_REGEX, ORIGINAL_LINK_LENGTH_MAX, SHORT_LENGTH_MANUAL
from .models import URLMap


ORIGINAL_LINK_FIELD_MESSAGE = 'Введите оригинальную ссылку'
DATA_REQUIRED_MESSAGE = 'Обязательное поле'
CORRECT_URL_MESSAGE = 'Некорректный адрес ссылки'
YOUR_SHORT_LINK_CHOICE_MESSAGE = 'Ваш вариант короткой ссылки до 16 символов'
ALLOWED_SYMBOLS_MESSAGE = ('Недопустимые символы. '
                           'Допустимы только буквы "a-Z" и цифры "0-9"')
SHORT_EXISTS_MESSAGE = 'Предложенный вариант короткой ссылки уже существует.'


class URLForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_LINK_FIELD_MESSAGE,
        validators=[DataRequired(message=DATA_REQUIRED_MESSAGE),
                    Length(max=ORIGINAL_LINK_LENGTH_MAX),
                    URL(message=CORRECT_URL_MESSAGE)]
    )
    custom_id = StringField(
        YOUR_SHORT_LINK_CHOICE_MESSAGE,
        validators=[
            Length(max=SHORT_LENGTH_MANUAL),
            Optional(),
            Regexp(regex=SHORT_REGEX,
                   message=ALLOWED_SYMBOLS_MESSAGE)
        ]
    )
    submit = SubmitField('Создать')

    def validate_custom_id(self, field):
        if field.data and URLMap.get(field.data):
            raise ValidationError(SHORT_EXISTS_MESSAGE)
        return field.data
