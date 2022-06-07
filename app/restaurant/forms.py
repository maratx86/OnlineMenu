from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l

from wtforms import SubmitField, StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class REditorForm(FlaskForm):
    title = StringField(_l('Title'), validators=[DataRequired()], render_kw={"placeholder": _l('Title')})
    description = TextAreaField(_l('Description'), render_kw={"placeholder": _l('Description')})
    submit = SubmitField(_l('Edit'))

    def fill(self, r):
        if r.title:
            self.title.data = r.title
        if r.description:
            self.description.data = r.description

    def out(self, r):
        r.title = self.title.data
        r.description = self.description.data


class MEditorForm(FlaskForm):
    title = StringField(_l('Title'), validators=[DataRequired()], render_kw={"placeholder": _l('Title')})
    description = TextAreaField(_l('Description'), render_kw={"placeholder": _l('Description')})
    submit = SubmitField(_l('Edit'))

    def fill(self, m):
        if m.title:
            self.title.data = m.title
        if m.description:
            self.description.data = m.description

    def out(self, m):
        m.title = self.title.data
        m.description = self.description.data


class PositionEditorForm(FlaskForm):
    title = StringField(_l('Title'), validators=[DataRequired()], render_kw={"placeholder": _l('Title')})
    description = TextAreaField(_l('Description'), render_kw={"placeholder": _l('Description')})
    submit = SubmitField(_l('Edit'))

    def fill(self, p):
        if p.title:
            self.title.data = p.title
        if p.description:
            self.description.data = p.description

    def out(self, p):
        p.title = self.title.data
        p.description = self.description.data


class MenuPositionEditorForm(FlaskForm):
    title = StringField(_l('Title'), render_kw={"placeholder": _l('Title'), 'disabled': 'disabled'})
    cost = IntegerField(_l('Cost'), render_kw={"placeholder": _l('Cost')})
    submit = SubmitField(_l('Edit'))

    def fill(self, p):
        if p.position.title:
            self.title.data = p.position.title
        if p.cost:
            self.cost.data = p.cost

    def out(self, p):
        p.cost = self.cost.data
