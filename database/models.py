from database.db import get_connection

def insert_quote(text, author):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id
        FROM quotes
        WHERE text = %s
        """,
        (text,)
    )

    existing = cur.fetchone()

    if not existing:
        cur.execute(
            """
            INSERT INTO quotes (text, author)
            VALUES (%s, %s)
            """,
            (text, author)
        )

        conn.commit()

    cur.close()
    conn.close()