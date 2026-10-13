# Employee Pay Management System

A desktop-based **Employee Pay Management System** featuring a Python Tkinter graphical user interface (GUI) and seamless integration with an **Oracle Database** backend via `oracledb` / `cx_Oracle`.

The application automates employee compensation processing, calculates gross/net pay, handles statutory deductions (PF, Tax), computes overtime pay, and evaluates bonus eligibility.

---

## 🚀 Features

* **Secure Authentication:** User login system integrated with database validation.
* **Automated Payroll Processing:** Real-time calculation of Gross Salary, PF (12%), Income Tax (10%), Overtime Pay, and Net Salary.
* **Bonus Eligibility Engine:** Automated evaluation of bonus eligibility based on net pay threshold ($\ge \text{₹}50,000$).
* **Database Integration:** Full CRUD capability using Oracle Database with sequence-driven primary keys.
* **Modern Desktop GUI:** Built with Python `tkinter` and styled using `ttk` for a responsive user dashboard.
* **Fail-Safe Presentation Mode:** Built-in offline fallback that ensures continuous demonstration even if the database service is disconnected.

---

## 🛠️ Tech Stack

* **Frontend:** Python `tkinter`, `ttk`
* **Backend Database:** Oracle Database XE / Enterprise (SQL*Plus)
* **Database Driver:** `oracledb` / `cx_Oracle`
* **Environment:** Python 3.x

---

## 📁 Project Structure

```text
├── app.py          # Main application GUI & business logic
├── setup_db.py     # Database schema initialization & seeding script
└── README.md       # Project documentation
