from flask import Blueprint,render_template,request,flash,redirect,url_for,session
import dash
import dash_core_components as dcc
import dash_html_components as html
maps = Blueprint('maps',__name__,template_folder = 'templates',static_folder = 'static',static_url_path='/static/')


@maps.route('/loginn', methods=['POST','GET'])
def loginn():
	if request.method == 'POST':
		print(session)
	return render_template('login.html',username=['userLogget'])
@maps.route('/form',methods = ['POST','GET'])
def form():
	if request.method == 'POST':
		try:
			if len(request.form['q']) > 2:
				flash('Строка больше двух',category = 'success')
			else:
				flash('Меньше ёп')	
			
			print(request.form['q'])
		except:
			pass
		return render_template('maps/form.html')
@maps.route('/form')
def form2():
	if request.method == 'POST':
		flash('sdfsdf')



	return render_template('maps/form.html',alert)
@maps.route('/conspect')
def conspect():
	return render_template('maps/conspect.html')


@maps.route('/')
def index():
	return render_template('maps/index.html')

    
if __name__ == '__main__':
    app.run_server(debug=True)
