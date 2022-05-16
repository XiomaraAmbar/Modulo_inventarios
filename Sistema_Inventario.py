from flask import Flask, render_template, request, redirect,url_for,flash
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'Sistema_Inventario'
mysql = MySQL(app)

@app.route('/')
def Index():
	return render_template('navegation.html')

@app.route('/view_products')
def view_products():
	cur=mysql.connection.cursor()
	cur.execute('Select * From productos')
	data = cur.fetchall()
	return render_template('report_products.html', products = data)

@app.route('/view_products_categories/<string:cod_cat>')
def view_products_categories(cod_cat):
	cur=mysql.connection.cursor()
	cur.execute("""Select cod_prod,name_prod,stock_prod,
		fech_exp,categorias.name_cat from productos 
		inner join categorias on productos.cod_cat=categorias.cod_cat 
		where categorias.cod_cat = {0}; """.format(cod_cat))
	data = cur.fetchall()
	return render_template('report_products_categories.html', categories = data)

@app.route('/view_categories')
def view_categories():
	cur=mysql.connection.cursor()
	cur.execute('Select * From categorias')
	data = cur.fetchall()
	return render_template('navegation_categories.html', vcategories = data)

if __name__=='__main__':
	app.run(port=81, debug=True)