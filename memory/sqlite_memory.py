import sqlite3
class SQLiteMemory:
    def __init__(self, db_name="memory/memory.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            query TEXT,
            response TEXT
        )
        """)
        self.conn.commit()
    def save(self, customer, query, response):
        self.cursor.execute("""
        INSERT INTO conversations
        (customer_name,query,response)
        VALUES(?,?,?)
        """,(customer,query,response))
        self.conn.commit()
    def get_last_issue(self, customer):
        self.cursor.execute("""
        SELECT query
        FROM conversations
        WHERE customer_name=?
        ORDER BY id DESC
        LIMIT 1
        """,(customer,))
        row=self.cursor.fetchone()
        if row:
            return row[0]
        return "No previous issue found."
    def close(self):
        self.conn.close()