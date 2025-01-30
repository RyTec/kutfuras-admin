from datetime import datetime
from db import get_db_connection

# Az árajánlatok modellje
class Quote:
    def __init__(self, id, company_name, address, postal_code, city, street, house_number, tax_id, contact_email, contact_phone, date_created=None, status=None):
        self.id = id
        self.company_name = company_name
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.street = street
        self.house_number = house_number
        self.tax_id = tax_id
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.date_created = date_created if date_created else datetime.utcnow()
        self.status = status

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM quotes')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Quote(*row) for row in rows]

    @staticmethod
    def get_by_id(quote_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM quotes WHERE id = %s', (quote_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Quote(*row)
        return None

    @staticmethod
    def insert(company_name, address, postal_code, city, street, house_number, tax_id, contact_email, contact_phone):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(''' 
            INSERT INTO quotes (company_name, address, postal_code, city, street, house_number, tax_id, contact_email, contact_phone) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) 
        ''', (company_name, address, postal_code, city, street, house_number, tax_id, contact_email, contact_phone))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def update(quote_id, company_name, address, postal_code, city, street, house_number, tax_id, contact_email, contact_phone):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(''' 
            UPDATE quotes 
            SET company_name = %s, address = %s, postal_code = %s, city = %s, street = %s, house_number = %s, tax_id = %s, contact_email = %s, contact_phone = %s 
            WHERE id = %s 
        ''', (company_name, address, postal_code, city, street, house_number, tax_id, contact_email, contact_phone, quote_id))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete(quote_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM quotes WHERE id = %s', (quote_id,))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def search(query):
        """
        Keresési funkció, amely cégnév és státusz alapján keres.
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        if not query:
            cursor.execute('SELECT * FROM quotes')
        else:
            # Keresés cégnév és státusz alapján
            cursor.execute('''
                SELECT * FROM quotes 
                WHERE company_name LIKE %s OR status LIKE %s
            ''', (f'%{query}%', f'%{query}%'))
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Quote(*row) for row in rows]

# A megrendelések modellje
class Order:
    def __init__(self, id, order_type, status, quote_id, drilling_point_id):
        self.id = id
        self.order_type = order_type
        self.status = status
        self.quote_id = quote_id
        self.drilling_point_id = drilling_point_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM orders')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Order(*row) for row in rows]

    @staticmethod
    def get_by_id(order_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM orders WHERE id = %s', (order_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return Order(*row)
        return None

    # Új rekord beszúrása
    @staticmethod
    def insert(order_type, status, quote_id, drilling_point_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO orders (order_type, status, quote_id, drilling_point_id)
            VALUES (%s, %s, %s, %s)
        ''', (order_type, status, quote_id, drilling_point_id))
        conn.commit()
        cursor.close()
        conn.close()

    # Rekord frissítése
    @staticmethod
    def update(order_id, order_type, status, quote_id, drilling_point_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE orders
            SET order_type = %s, status = %s, quote_id = %s, drilling_point_id = %s
            WHERE id = %s
        ''', (order_type, status, quote_id, drilling_point_id, order_id))
        conn.commit()
        cursor.close()
        conn.close()

    # Rekord törlése
    @staticmethod
    def delete(order_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM orders WHERE id = %s', (order_id,))
        conn.commit()
        cursor.close()
        conn.close()


# A fúrási pontok modellje
class DrillingPoint:
    def __init__(self, id, city, street, house_number, drilling_status, depth, water_yield, work_days, comment):
        self.id = id
        self.city = city
        self.street = street
        self.house_number = house_number
        self.drilling_status = drilling_status
        self.depth = depth
        self.water_yield = water_yield
        self.work_days = work_days
        self.comment = comment

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM drilling_points')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [DrillingPoint(*row) for row in rows]

    @staticmethod
    def get_by_id(drilling_point_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM drilling_points WHERE id = %s', (drilling_point_id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            return DrillingPoint(*row)
        return None

    # Új rekord beszúrása
    @staticmethod
    def insert(city, street, house_number, drilling_status, depth, water_yield, work_days, comment):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO drilling_points (city, street, house_number, drilling_status, depth, water_yield, work_days, comment)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (city, street, house_number, drilling_status, depth, water_yield, work_days, comment))
        conn.commit()
        cursor.close()
        conn.close()

    # Rekord frissítése
    @staticmethod
    def update(drilling_point_id, city, street, house_number, drilling_status, depth, water_yield, work_days, comment):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE drilling_points
            SET city = %s, street = %s, house_number = %s, drilling_status = %s, depth = %s, water_yield = %s, work_days = %s, comment = %s
            WHERE id = %s
        ''', (city, street, house_number, drilling_status, depth, water_yield, work_days, comment, drilling_point_id))
        conn.commit()
        cursor.close()
        conn.close()

    # Rekord törlése
    @staticmethod
    def delete(drilling_point_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM drilling_points WHERE id = %s', (drilling_point_id,))
        conn.commit()
        cursor.close()
        conn.close()
