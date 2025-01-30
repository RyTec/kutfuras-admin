from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, config
from flask_mysqldb import MySQL
from db import get_quotes, get_orders, get_drilling_points, get_db_connection
from models import Quote, Order, DrillingPoint

app = Flask(__name__, static_folder="static")
app.config.from_object(config)
app.secret_key = 'your_secret_key'  # Biztonságos kulcs a session kezeléshez

# MySQL konfiguráció
app.config['MYSQL_HOST'] = '79.172.249.13'
app.config['MYSQL_USER'] = 'menhelyt_kutfuras_user'  # A te MySQL felhasználóneved
app.config['MYSQL_PASSWORD'] = 'fostalicsKa.011'  # A jelszavad
app.config['MYSQL_DB'] = 'menhelyt_kutfuras_db'  # Az adatbázis neve

mysql = MySQL(app)


app.config.from_object(config)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

# Alap oldal (home)
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/quotes', methods=['GET'])
def quotes():
    search_query = request.args.get('search', '')
    quotes = Quote.search(search_query)
    return render_template('quotes.html', quotes=quotes)

@app.route('/quote/<int:id>', methods=['GET'])
def view_quote(id):
    quote = Quote.get_by_id(id)
    if not quote:
        flash('Árajánlat nem található!', 'danger')
        return redirect(url_for('quotes'))
    return render_template('view_quote.html', quote=quote)


@app.route('/quote/edit/<int:id>', methods=['GET', 'POST'])
def edit_quote(id):
    quote = Quote.get_by_id(id)
    if not quote:
        flash('Árajánlat nem található!', 'danger')
        return redirect(url_for('quotes'))

    if request.method == 'POST':
        company_name = request.form['company_name']
        address = request.form['address']
        postal_code = request.form['postal_code']
        city = request.form['city']
        street = request.form['street']
        house_number = request.form['house_number']
        tax_id = request.form['tax_id']
        contact_email = request.form['contact_email']
        contact_phone = request.form['contact_phone']

        Quote.update(id, company_name, address, postal_code, city, street, house_number, tax_id, contact_email,
                     contact_phone)
        flash('Árajánlat sikeresen frissítve!', 'success')
        return redirect(url_for('view_quote', id=id))

    return render_template('edit_quote.html', quote=quote)

@app.route('/quote/create', methods=['GET', 'POST'])
def create_quote():
    if request.method == 'POST':
        company_name = request.form['company_name']
        address = request.form['address']
        postal_code = request.form['postal_code']
        city = request.form['city']
        street = request.form['street']
        house_number = request.form['house_number']
        tax_id = request.form['tax_id']
        contact_email = request.form['contact_email']
        contact_phone = request.form['contact_phone']

        Quote.insert(company_name, address, postal_code, city, street, house_number, tax_id, contact_email, contact_phone)
        flash('Új árajánlat sikeresen létrehozva!', 'success')
        return redirect(url_for('quotes'))

    return render_template('create_quote.html')

@app.route('/admin/quotes')
def show_quotes():
    search_query = request.args.get('search', '')  # A keresési lekérdezés
    quotes = Quote.search(search_query)  # A modellben lévő keresési metódust hívjuk meg
    return render_template('quotes.html', quotes=quotes)

@app.route('/admin/orders')
def show_orders():
    orders = Order.get_all()  # Hasonlóan az 'orders' modelhez
    return render_template('orders.html', orders=orders)

@app.route('/admin/drilling_points')
def show_drilling_points():
    drilling_points = DrillingPoint.get_all()  # A fúrási pontok megjelenítése
    return render_template('drilling_points.html', drilling_points=drilling_points)

@app.route('/quote/add', methods=['GET', 'POST'])
def add_quote():
    if request.method == 'POST':
        company_name = request.form['company_name']
        address = request.form['address']
        tax_id = request.form['tax_id']
        contact_email = request.form['contact_email']
        contact_phone = request.form['contact_phone']

        # Add quote to DB
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO quotes (company_name, address, tax_id, contact_email, contact_phone)
            VALUES (%s, %s, %s, %s, %s)
        ''', (company_name, address, tax_id, contact_email, contact_phone))
        conn.commit()
        cursor.close()
        conn.close()

        flash('Árajánlat sikeresen hozzáadva!', 'success')
        return redirect(url_for('quotes'))
    return render_template('add_quote.html')

@app.route('/quote/delete/<int:quote_id>', methods=['POST'])
def delete_quote(quote_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM quotes WHERE id = %s', (quote_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash('Árajánlat sikeresen törölve!', 'success')
    return redirect(url_for('quotes'))


@app.route('/orders')
def orders():
    orders = get_orders()
    return render_template('orders.html', orders=orders)

@app.route('/drilling_points')
def drilling_points():
    drilling_points = get_drilling_points()
    return render_template('drilling_points.html', drilling_points=drilling_points)

if __name__ == '__main__':
    app.run(debug=True)