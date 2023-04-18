from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .constants import (CHECK_RE_ERROR_MESSAGE, CUSTOM_ID_CHECK_RE,
                        DESCRIPTION_SHORT, DESCRIPTION_URL,
                        LENGTH_ERROR_MESSAGE, MISSING_DATA)


class URLForm(FlaskForm):
    original_link = URLField(
        DESCRIPTION_URL,
        validators=(DataRequired(message=MISSING_DATA),
                    Length(1))
    )
    custom_id = StringField(
        DESCRIPTION_SHORT,
        validators=(Optional(), Length(1, 16, message=LENGTH_ERROR_MESSAGE),
                    Regexp(CUSTOM_ID_CHECK_RE, message=CHECK_RE_ERROR_MESSAGE))
    )
    submit = SubmitField('Создать')
