import sqlite3

def initialize_database():
    conn = sqlite3.connect("courses.db")
    cursor = conn.cursor()

    # Create 5 tables with no columns (other than an id for now)
    tables = ["DS_3850", "ACCT_3210", "DS_3540", "BMGT_4410", "PHED_1101"]

    for table in tables:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table} (
                id INTEGER PRIMARY KEY AUTOINCREMENT
            )
        """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    print("Database initialized with 5 blank tables.")