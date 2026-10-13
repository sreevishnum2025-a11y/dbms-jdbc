import sqlite3

def setup_database():
    # Connects to SQLite (creates the file payroll.db if it doesn't exist)
    conn = sqlite3.connect('payroll.db')
    cursor = conn.cursor()

    # ==========================================
    # DDL COMMANDS (Creating Tables)
    # ==========================================
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        designation TEXT NOT NULL,
        basic_pay REAL NOT NULL,
        allowances REAL NOT NULL,
        deductions REAL NOT NULL,
        net_pay REAL NOT NULL
    )
    ''')

    # ==========================================
    # DML COMMANDS (Inserting initial data)
    # ==========================================
    try:
        # Insert admin user for login
        cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
        
        # Insert a sample employee record
        cursor.execute("""
        INSERT INTO employees (name, designation, basic_pay, allowances, deductions, net_pay) 
        VALUES ('Alice Smith', 'Senior Developer', 80000, 15000, 5000, 90000)
        """)
    except sqlite3.IntegrityError:
        # Ignores error if the admin user already exists on subsequent runs
        pass 

    conn.commit()
    conn.close()
    print("Database 'payroll.db' created successfully with required DDL and DML commands.")

if __name__ == '__main__':
    setup_database()