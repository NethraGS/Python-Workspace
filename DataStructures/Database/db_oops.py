import sqlite3
from abc import ABC, abstractmethod


# ==================== ABSTRACT DAO (ABSTRACTION) ====================

class EmployeeDAO(ABC):

    @abstractmethod
    def add_employee(self, empid, name):
        pass

    @abstractmethod
    def display_employees(self):
        pass

    @abstractmethod
    def update_employee(self, empid, name):
        pass

    @abstractmethod
    def delete_employee(self, empid):
        pass

    @abstractmethod
    def close_connection(self):
        pass


# ==================== SQLITE IMPLEMENTATION (INHERITANCE) ====================

class SQLiteEmployeeDAO(EmployeeDAO):

    def __init__(self):
        self.conn = sqlite3.connect("employee.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def add_employee(self, empid, name):
        try:
            self.cursor.execute(
                "INSERT INTO employee (id, name) VALUES (?, ?)",
                (empid, name)
            )
            self.conn.commit()
            print("✅ Employee added successfully")
        except sqlite3.IntegrityError:
            print("❌ Employee ID already exists")

    def display_employees(self):
        self.cursor.execute("SELECT * FROM employee")
        rows = self.cursor.fetchall()

        if not rows:
            print("⚠️ No employees found")
            return

        print("\nID   Name")
        print("-" * 20)
        for row in rows:
            print(f"{row[0]}   {row[1]}")

    def update_employee(self, empid, name):
        self.cursor.execute(
            "UPDATE employee SET name=? WHERE id=?",
            (name, empid)
        )
        self.conn.commit()

        if self.cursor.rowcount == 0:
            print("❌ Employee ID not found")
        else:
            print("✅ Employee updated successfully")

    def delete_employee(self, empid):
        self.cursor.execute(
            "DELETE FROM employee WHERE id=?",
            (empid,)
        )
        self.conn.commit()

        if self.cursor.rowcount == 0:
            print("❌ Employee ID not found")
        else:
            print("✅ Employee deleted successfully")

    def close_connection(self):
        self.conn.close()
        print("🔒 Database connection closed")


# ==================== MENU (POLYMORPHISM) ====================

def main():
    dao: EmployeeDAO = SQLiteEmployeeDAO()

    while True:
        print("\n===== EMPLOYEE MENU =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Please enter a valid number")
            continue

        match choice:
            case 1:
                empid = int(input("Enter employee id: "))
                name = input("Enter employee name: ")
                dao.add_employee(empid, name)

            case 2:
                dao.display_employees()

            case 3:
                empid = int(input("Enter employee id to update: "))
                name = input("Enter new name: ")
                dao.update_employee(empid, name)

            case 4:
                empid = int(input("Enter employee id to delete: "))
                dao.delete_employee(empid)

            case 5:
                dao.close_connection()
                print("👋 Exiting program")
                break

            case _:
                print("❌ Invalid choice")


# ==================== PROGRAM ENTRY ====================

if __name__ == "__main__":
    main()
