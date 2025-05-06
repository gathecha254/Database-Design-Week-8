import mysql.connector
from mysql.connector import pooling

# Set up a connection pool for better performance and scalability
connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    host="localhost",      # Change if your DB is hosted elsewhere
    user="root",           # Your MySQL username
    password="yourpassword",  # ⚠️ Change to your actual MySQL password
    database="library"     # Make sure this matches your MySQL database name
)

# Function to get a connection from the pool
def get_db():
    return connection_pool.get_connection()
