import sqlite3


class UserDatabase:

    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()

    def create_table(self):
        self.connect()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
        """)
        self.conn.commit()
        self.close()

    def add_user(self, name, age):
        self.connect()
        self.cursor.execute(
            "INSERT INTO users (name, age) VALUES (?, ?)",
            (name, age)
        )
        self.conn.commit()
        self.close()
        print("User added successfully")

    def view_users(self):
        self.connect()
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        self.close()

        if not users:
            print("No users found")
            return

        print("\nID   Name        Age")
        print("-" * 25)
        for u in users:
            print(f"{u[0]:<4} {u[1]:<10} {u[2]}")

    # --------- SEARCH METHOD ----------
    def search_user(self, user_id):
        self.connect()
        self.cursor.execute(
            "SELECT * FROM users WHERE id=?",
            (user_id,)
        )
        user = self.cursor.fetchone()
        self.close()

        if user is None:
            print("User ID not found")
        else:
            print("\nUser Found:")
            print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")

    def update_user(self, user_id, name, age):
        self.connect()
        self.cursor.execute(
            "UPDATE users SET name=?, age=? WHERE id=?",
            (name, age, user_id)
        )
        self.conn.commit()
        affected = self.cursor.rowcount
        self.close()

        if affected == 0:
            print("User ID not found")
        else:
            print("User updated successfully")

    def delete_user(self, user_id):
        self.connect()
        self.cursor.execute(
            "DELETE FROM users WHERE id=?",
            (user_id,)
        )
        self.conn.commit()
        affected = self.cursor.rowcount
        self.close()

        if affected == 0:
            print("User ID not found")
        else:
            print("User deleted successfully")


def main():
    print("🔹 Program started")

    db = UserDatabase()
    db.create_table()

    while True:
        print("\n===== USER DATABASE MENU =====")
        print("1. Add User")
        print("2. View Users")
        print("3. Search User")
        print("4. Update User")
        print("5. Delete User")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            db.add_user(name, age)

        elif choice == "2":
            db.view_users()

        elif choice == "3":
            uid = int(input("Enter user ID to search: "))
            db.search_user(uid)

        elif choice == "4":
            uid = int(input("Enter user ID: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            db.update_user(uid, name, age)

        elif choice == "5":
            uid = int(input("Enter user ID: "))
            db.delete_user(uid)

        elif choice == "6":
            print("Exiting program")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
