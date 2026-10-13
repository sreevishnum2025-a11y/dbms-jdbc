from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'secure_payroll_key_123' # Required for session management

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect('payroll.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        # DML (SELECT) to verify user
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        
        if user:
            session['logged_in'] = True
            session['username'] = user['username']
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid Credentials. Please try again.'
            
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    # DML (SELECT) to retrieve all employees
    employees = conn.execute('SELECT * FROM employees').fetchall()
    conn.close()
    
    return render_template('dashboard.html', employees=employees, username=session['username'])

@app.route('/add_employee', methods=['POST'])
def add_employee():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
        
    # Accepting input from user
    name = request.form['name']
    designation = request.form['designation']
    basic = float(request.form['basic_pay'])
    allowances = float(request.form['allowances'])
    deductions = float(request.form['deductions'])
    
    # Processing inputs to calculate Net Pay
    net_pay = (basic + allowances) - deductions
    
    conn = get_db_connection()
    # DML (INSERT) to add new processed record to DB
    conn.execute('''
        INSERT INTO employees (name, designation, basic_pay, allowances, deductions, net_pay) 
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, designation, basic, allowances, deductions, net_pay))
    conn.commit()
    conn.close()
    
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)