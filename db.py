import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="priya@2026",   # Nee set panna MySQL password
        database="image_search"
    )

    cursor = db.cursor()
    print("✅ MySQL Connected Successfully!")

except mysql.connector.Error as err:
    print("❌ Database Connection Error:", err)