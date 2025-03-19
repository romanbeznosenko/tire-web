from django.shortcuts import render
import mysql.connector

# Create your views here.

db_config = {
    "host": "localhost",
    "user": "br",
    "password": "1234",
    "database": "tires_db",
    "port": 3306
}

def get_all_brands():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        cursor.execute("SELECT name, brand_html_id FROM Brand")  # Adjusted for your Brand table
        brands = cursor.fetchall()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        brands = []  # Fallback in case of DB issues
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

    return brands

def main(request):
    brands = get_all_brands()

    filters = {
        'brands': brands,
        'vehicle_types': ['Car', 'Truck', 'Motorcycle'],
        'seasons': ['Summer', 'Winter', 'All Season'],
    }
    return render(request, 'main.html', {'filters': filters})