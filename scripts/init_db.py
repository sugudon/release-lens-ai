from pathlib import Path

from sqlalchemy import text

from backend.app.db.connection import engine


def initialize_database():
    schema_path = Path(
        "backend/app/db/schema.sql"
    )

    schema = schema_path.read_text()

    statements = [
        statement.strip()
        for statement in schema.split(";")
        if statement.strip()
    ]

    with engine.begin() as connection:
        for statement in statements:
            connection.execute(text(statement))


if __name__ == "__main__":
    initialize_database()

    print(
        "ReleaseLens database initialized successfully."
    )