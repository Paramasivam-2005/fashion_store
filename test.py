import pyodbc

# Choose the best driver from your available list
DB_DRIVER = "MySQL ODBC 9.2 Unicode Driver"  # Or use "MySQL ODBC 9.2 ANSI Driver"

# Connection string for SQLAlchemy
uri = f"mysql+pyodbc://root:root@localhost/fashion?driver={DB_DRIVER}"

# Verify connection
try:
    conn = pyodbc.connect(f"DRIVER={DB_DRIVER};SERVER=localhost;DATABASE=fashion;USER=root;PASSWORD=root;")
    print("Database connection successful!")
except Exception as e:
    print("Database connection failed:", e)
