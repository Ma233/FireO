from fireo.fields import TextField
from fireo.models import Model
from fireo.fields.errors import AttributeTypeError
import pytest


def test_simple_format():
    class TextFieldFormat(Model):
        name_title = TextField(format='title')
        name_upper = TextField(format='upper')
        name_lower = TextField(format='lower')
        name_capitalize = TextField(format='capitalize')

    t = TextFieldFormat()
    t.name_title = "they're bill's friends from the UK"
    t.name_upper = 'name upper'
    t.name_lower = 'Name LOWER'
    t.name_capitalize = 'name capitalize'
    t.save()

    tf = TextFieldFormat.collection.get(t.key)

    assert tf.name_title == "They're Bill's Friends From The Uk"
    assert tf.name_upper == 'NAME UPPER'
    assert tf.name_lower == 'name lower'
    assert tf.name_capitalize == 'Name capitalize'


def test_invalid_text_format_type():
    class TextFieldFormat(Model):
        name = TextField(format='invalid type')

    with pytest.raises(AttributeTypeError):
        t = TextFieldFormat()
        t.name = 'name text'
        t.save()