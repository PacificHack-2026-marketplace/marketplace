import sqlite3


class Listing(object):
    def __init__(self,
                 title: str,
                 category: str,
                 price: float,
                 user_name: str,
                 contact_email: str,
                 contact_phone: int|None = None,
                 location: str|None = None,
                 description: str|None = None,
                 summary: str|None = None,
                 sold: bool = False,
                 listing_id: int|None = None):
        self.title = title
        self.category = category
        self.price = price
        self.user_name = user_name
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.location = location
        self.description = description
        self.summary = summary
        self.sold = sold
        self.listing_id = listing_id

def get_db():
    db = sqlite3.connect("database.db")
    return db

def insert_listing(listing: Listing):
    assert listing.listing_id is None   # must not exist
    db = get_db()
    cur = db.cursor()
    result = cur.execute(
        "INSERT INTO listing (title, category, price, user_name, contact_email, contact_phone, location, description, summary, sold) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (listing.title, listing.category, listing.price, listing.user_name, listing.contact_email, listing.contact_phone, listing.location, listing.description, listing.summary, listing.sold)
    )
    cur.close()
    db.commit()
    return result.lastrowid

LISTING_QUERY_COLS = "title, category, price, user_name, contact_email, contact_phone, location, description, summary, sold, listing_id"

def parse_listing(row) -> Listing:
    return Listing(*row)

def get_listing(id: int):
    db = get_db()
    cur = db.cursor()
    result = cur.execute(
        "SELECT " + LISTING_QUERY_COLS + " FROM listing WHERE listing_id = ?",
        (id,)
    )

    row = result.fetchone()
    print(row)

    cur.close()
    db.commit()

    return parse_listing(row)

def _get_top_listings(query, params):
    db = get_db()
    cur = db.cursor()
    result = cur.execute(query, params)

    rows = result.fetchall()

    cur.close()
    db.commit()

    return [parse_listing(r) for r in rows]


def get_top_listings(limit: int = 20, category: str|None = None, search_keywords: list|None = None):
    where_clauses = []
    where_params = []

    if category is not None:
        where_clauses.append("category = ?")
        where_params.append(category)

    where_clause = " AND ".join(where_clauses)
    if len(where_clause) > 0:
        where_clause = "WHERE " + where_clause

    return _get_top_listings(
        "SELECT " + LISTING_QUERY_COLS + " FROM listing " + where_clause + " LIMIT ?",
        (*where_params, limit,)
    )


def init_db():
    db = get_db()
    cur = db.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS listing(
        listing_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        price REAL NOT NULL,
        user_name TEXT NOT NULL,
        contact_email TEXT NOT NULL,
        contact_phone TEXT,
        location TEXT,
        description TEXT,
        summary TEXT,
        category TEXT,
        sold BOOLEAN NOT NULL
    );
    """)
    cur.close()
    db.commit()

