import sqlite3
import os

# Vercel環境ではメモリベースのDBを使用する
DATABASE = ':memory:' if os.environ.get('VERCEL') else 'database.db'

def create_books_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS books (title, price, arrival_day)")
    # サンプルデータを挿入
    con.execute("INSERT OR IGNORE INTO books VALUES('Sample Book', '1000', '2025-01-01')")
    con.commit()
    con.close()
