import mysql.connector


conn = mysql.connector.connect(
host="localhost", user="root", password="root", database="ECommerce")
cursor = conn.cursor()
try:
    conn.start_transaction()
    cursor.execute("INSERT INTO customers (id,lastname,firstname,birthdate) VALUES (5,'Curtois','Ester','2025-05-28')")
    cursor.execute("INSERT INTO orders (id,customer_id,order_date) VALUES (5,5,'2025-05-28')")
    cursor.execute("UPDATE products SET quantity = quantity - 2 WHERE id = 1")
    conn.commit() # ��� Tout a marché
except Exception as e:
    conn.rollback() # �� Une erreur → on annule tout
    print("Erreur détectée :", e)