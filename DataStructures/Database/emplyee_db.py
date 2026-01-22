import sqlite3


class EmployeeDAO:
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
            print("Employee added successfully")
        except sqlite3.IntegrityError:
            print("Employee ID already exists")

    def display_employees(self):
        self.cursor.execute("SELECT * FROM employee")
        rows = self.cursor.fetchall()

        if not rows:
            print("No employees found")
            return

        print("\nID   Name")
        print("-" * 20)
        for row in rows:
            print(row[0], " ", row[1])

    # --------- SEARCH METHOD ----------
    def search_employee(self, empid):
        self.cursor.execute(
            "SELECT * FROM employee WHERE id=?",
            (empid,)
        )
        row = self.cursor.fetchone()

        if row is None:
            print("Employee not found")
        else:
            print("\nEmployee Found")
            print("ID:", row[0])
            print("Name:", row[1])

    # --------- UPDATE METHOD ----------
    def update_employee(self, empid, name):
        self.cursor.execute(
            "UPDATE employee SET name=? WHERE id=?",
            (name, empid)
        )
        self.conn.commit()

        if self.cursor.rowcount == 0:
            print("Employee ID not found")
        else:
            print("Employee updated successfully")

    # --------- DELETE METHOD ----------
    def delete_employee(self, empid):
        self.cursor.execute(
            "DELETE FROM employee WHERE id=?",
            (empid,)
        )
        self.conn.commit()

        if self.cursor.rowcount == 0:
            print("Employee ID not found")
        else:
            print("Employee deleted successfully")

    def close_connection(self):
        self.conn.close()
        print("Database connection closed")


def main():
    dao = EmployeeDAO()

    while True:
        print("\n===== EMPLOYEE MENU =====")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                empid = int(input("Enter employee id: "))
                name = input("Enter employee name: ")
                dao.add_employee(empid, name)

            case 2:
                dao.display_employees()

            case 3:
                empid = int(input("Enter employee id to search: "))
                dao.search_employee(empid)

            case 4:
                empid = int(input("Enter employee id to update: "))
                name = input("Enter new name: ")
                dao.update_employee(empid, name)

            case 5:
                empid = int(input("Enter employee id to delete: "))
                dao.delete_employee(empid)

            case 6:
                dao.close_connection()
                print("Exiting program")
                break

            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
