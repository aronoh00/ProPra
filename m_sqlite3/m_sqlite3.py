import argparse
import sqlite3
import pprint
import json


# A2
def connect_db():
    return sqlite3.connect("m_sqlite3.db")


def create_table():
    con = connect_db()
    # A3
    cur = con.cursor()

    # A4
    cur.execute('''CREATE TABLE IF NOT EXISTS books (
                title TEXT PRIMARY KEY,
                genre TEXT,
                alredy_read INTEGER
                )''')

    # A5
    cur.execute("""
                INSERT OR IGNORE INTO books VALUES
                    ('The Lord of The Rings', 'Fantasy', 1),
                    ('1984', 'Fiction', 1),
                    ('The Art of Computer Programming', 'Monograph', 0)
                """)

    con.commit()
    con.close()


def query_table():
    con = connect_db()
    cur = con.cursor()

    # A7
    cur.execute("SELECT COUNT(title) FROM books")
    print("numberof entries in 'books':", cur.fetchone()[0])

    # A8
    query_fantasy_books = "SELECT title FROM books WHERE genre='Fantasy'"
    fantasy_books = cur.execute(query_fantasy_books).fetchall()
    print(f"fantasy books: {pprint.pformat(fantasy_books)}")

    # A9
    cur.execute("SELECT genre, COUNT(genre) FROM books GROUP BY genre ORDER BY COUNT(genre) DESC")
    print("most common genre(s):", cur.fetchall())

    con.close()


def import_data():
    con = connect_db()
    cur = con.cursor()

    # A10
    with open("reading-list.json") as f:
        books = json.load(f)

    # A11
    cur.executemany("INSERT INTO books VALUES (:title, :genre, 0)", books)

    con.commit()
    con.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['create', 'query', 'import'])
    args = parser.parse_args()

    if args.action == 'create':
        create_table()
    elif args.action == 'query':
        query_table()
    elif args.action == 'import':
        import_data()


if __name__ == '__main__':
    main()
