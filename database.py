import sqlite3

def initialize_database():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # Create 5 tables with no columns (other than an id for now)
    tables = ["DS_3850", "ACCT_3210", "DS_3540", "BMGT_4410", "PHED_1101"]


    for table in tables:
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        choice_a TEXT,
        choice_b TEXT,
        choice_c TEXT,
        choice_d TEXT,
        correct_answer TEXT
    )
    """)
    

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    print("Database initialized with 5 blank tables.")