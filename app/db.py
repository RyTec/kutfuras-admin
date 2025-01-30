from flask import current_app
import MySQLdb

def get_db_connection():
    with current_app.app_context():
        conn = MySQLdb.connect(
            host=current_app.config['MYSQL_HOST'],
            user=current_app.config['MYSQL_USER'],
            password=current_app.config['MYSQL_PASSWORD'],
            db=current_app.config['MYSQL_DB']
        )
    return conn

# Függvények adatbázis műveletekhez
def get_quotes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM quotes')
    quotes = cursor.fetchall()
    cursor.close()
    conn.close()
    return quotes

def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return orders

def get_drilling_points():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM drilling_points')
    drilling_points = cursor.fetchall()
    cursor.close()
    conn.close()
    return drilling_points