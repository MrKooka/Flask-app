from wtforms import Form,StringField,TextAreaField

class PostForm(Form):
	title = StringField('Title')
	body = TextAreaField('Body')











#они выстраивают соответвие между моделями и html формами