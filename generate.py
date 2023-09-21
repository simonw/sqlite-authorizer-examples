import json
import sqlite3

ACTIONS = {
    "SQLITE_CREATE_INDEX",
    "SQLITE_CREATE_TABLE",
    "SQLITE_CREATE_TEMP_INDEX",
    "SQLITE_CREATE_TEMP_TABLE",
    "SQLITE_CREATE_TEMP_TRIGGER",
    "SQLITE_CREATE_TEMP_VIEW",
    "SQLITE_CREATE_TRIGGER",
    "SQLITE_CREATE_VIEW",
    "SQLITE_DELETE",
    "SQLITE_DROP_INDEX",
    "SQLITE_DROP_TABLE",
    "SQLITE_DROP_TEMP_INDEX",
    "SQLITE_DROP_TEMP_TABLE",
    "SQLITE_DROP_TEMP_TRIGGER",
    "SQLITE_DROP_TEMP_VIEW",
    "SQLITE_DROP_TRIGGER",
    "SQLITE_DROP_VIEW",
    "SQLITE_INSERT",
    "SQLITE_PRAGMA",
    "SQLITE_READ",
    "SQLITE_SELECT",
    "SQLITE_TRANSACTION",
    "SQLITE_UPDATE",
    "SQLITE_ATTACH",
    "SQLITE_DETACH",
    "SQLITE_ALTER_TABLE",
    "SQLITE_REINDEX",
    "SQLITE_ANALYZE",
    "SQLITE_CREATE_VTABLE",
    "SQLITE_DROP_VTABLE",
    "SQLITE_FUNCTION",
    "SQLITE_SAVEPOINT",
    "SQLITE_RECURSIVE",
}

# Define the CONSTANTS mapping
CONSTANTS = {getattr(sqlite3, c): c for c in dir(sqlite3) if c in ACTIONS}

# SQL setup and example queries for each operation
sql_examples = {
    "SQLITE_CREATE_INDEX": {
        "setup": "CREATE TABLE demo_table (name TEXT);\nINSERT INTO demo_table (name) VALUES ('Alice')",
        "example": "CREATE INDEX demo_index ON demo_table (name)",
    },
    "SQLITE_CREATE_TABLE": {
        "setup": "",
        "example": "CREATE TABLE demo_table (name TEXT)",
    },
    # SQLITE_CREATE_TEMP_INDEX doesn't appear to be supported any more, skipping it
    "SQLITE_CREATE_TEMP_TABLE": {
        "setup": "",
        "example": "CREATE TEMP TABLE demo_table (name TEXT)",
    },
    "SQLITE_CREATE_TEMP_TRIGGER": {
        "setup": "CREATE TABLE demo_table (name TEXT)",
        "example": "CREATE TEMP TRIGGER demo_trigger AFTER INSERT ON demo_table\n  BEGIN\n    INSERT INTO demo_table (name) VALUES ('Alice');\n  END",
    },
    "SQLITE_CREATE_TEMP_VIEW": {
        "setup": "",
        "example": "CREATE TEMP VIEW demo_view AS SELECT 1",
    },
    "SQLITE_CREATE_TRIGGER": {
        "setup": "CREATE TABLE demo_table (name TEXT)",
        "example": "CREATE TRIGGER demo_trigger AFTER INSERT ON demo_table\n  BEGIN\n    INSERT INTO demo_table (name) VALUES ('Alice');\n  END",
    },
    "SQLITE_CREATE_VIEW": {"setup": "", "example": "CREATE VIEW demo_view AS SELECT 1"},
    "SQLITE_DELETE": {
        "setup": "CREATE TABLE demo_table (name TEXT);\nINSERT INTO demo_table (name) VALUES ('Alice')",
        "example": "DELETE FROM demo_table WHERE name='Alice'",
    },
    "SQLITE_DROP_INDEX": {
        "setup": "CREATE TABLE demo_table (name TEXT);\nCREATE INDEX demo_index ON demo_table (name)",
        "example": "DROP INDEX demo_index",
    },
    "SQLITE_DROP_TABLE": {
        "setup": "CREATE TABLE demo_table (name TEXT)",
        "example": "DROP TABLE demo_table",
    },
    # Skip SQLITE_DROP_TEMP_INDEX
    "SQLITE_DROP_TEMP_TABLE": {
        "setup": "CREATE TEMP TABLE demo_table (name TEXT)",
        "example": "DROP TABLE demo_table",
    },
    "SQLITE_DROP_TEMP_TRIGGER": {
        "setup": "CREATE TABLE demo_table (name TEXT);\nCREATE TEMP TRIGGER demo_trigger AFTER INSERT ON demo_table\n  BEGIN\n    INSERT INTO demo_table (name) VALUES ('Alice');\n  END",
        "example": "DROP TRIGGER demo_trigger",
    },
    "SQLITE_DROP_TEMP_VIEW": {
        "setup": "CREATE TEMP VIEW demo_view AS SELECT 1",
        "example": "DROP VIEW demo_view",
    },
    "SQLITE_DROP_TRIGGER": {
        "setup": "CREATE TABLE demo_table (name TEXT);\nCREATE TRIGGER demo_trigger AFTER INSERT ON demo_table\n  BEGIN\n    INSERT INTO demo_table (name) VALUES ('Alice');\n  END",
        "example": "DROP TRIGGER demo_trigger",
    },
    "SQLITE_DROP_VIEW": {
        "setup": "CREATE VIEW demo_view AS SELECT 1",
        "example": "DROP VIEW demo_view",
    },
    "SQLITE_INSERT": {
        "setup": "CREATE TABLE demo_table (name TEXT)",
        "example": "INSERT INTO demo_table (name) VALUES ('Alice')",
    },
    "SQLITE_PRAGMA": {
        "setup": "",
        "example": "PRAGMA foreign_keys; PRAGMA foreign_keys = ON",
    },
    "SQLITE_READ": {
        "setup": "CREATE TABLE demo_table (name TEXT);\nINSERT INTO demo_table (name) VALUES ('Alice')",
        "example": "SELECT name FROM demo_table",
    },
    "SQLITE_SELECT": {
        "setup": "CREATE TABLE demo_table (name TEXT);\nINSERT INTO demo_table (name) VALUES ('Alice')",
        "example": "SELECT name FROM demo_table",
    },
    "SQLITE_TRANSACTION": {
        "setup": "CREATE TABLE demo_table (name TEXT)",
        "example": "BEGIN TRANSACTION;\n  INSERT INTO demo_table (name) VALUES ('Alice');\nCOMMIT",
    },
    "SQLITE_UPDATE": {
        "setup": "CREATE TABLE demo_table (name TEXT);\nINSERT INTO demo_table (name) VALUES ('Alice')",
        "example": "UPDATE demo_table SET name='Bob' WHERE name='Alice'",
    },
    "SQLITE_ATTACH": {"setup": "", "example": "ATTACH DATABASE ':memory:' AS second"},
    "SQLITE_DETACH": {
        "setup": "ATTACH DATABASE ':memory:' AS second",
        "example": "DETACH DATABASE second",
    },
    "SQLITE_ALTER_TABLE": {
        "setup": "CREATE TABLE demo_table (name TEXT)",
        "example": "ALTER TABLE demo_table ADD COLUMN age INTEGER",
    },
    "SQLITE_REINDEX": {
        "setup": "CREATE TABLE demo_table (name TEXT);\nCREATE INDEX demo_index ON demo_table (name)",
        "example": "REINDEX demo_index",
    },
    "SQLITE_ANALYZE": {
        "setup": "CREATE TABLE demo_table (name TEXT);\nCREATE INDEX demo_index ON demo_table (name)",
        "example": "ANALYZE",
    },
    "SQLITE_CREATE_VTABLE": {
        "setup": "",
        "example": "CREATE VIRTUAL TABLE demo_table USING fts5(name)",
    },
    "SQLITE_DROP_VTABLE": {
        "setup": "CREATE VIRTUAL TABLE demo_table USING fts5(name)",
        "example": "DROP TABLE demo_table",
    },
    "SQLITE_FUNCTION": {"setup": "", "example": "SELECT upper('Alice')"},
    "SQLITE_SAVEPOINT": {
        "setup": "CREATE TABLE demo_table (name TEXT)",
        "example": "SAVEPOINT demo_savepoint",
    },
    # SQLITE_COPY is "no longer used"
    "SQLITE_RECURSIVE": {
        "setup": "",
        "example": "WITH RECURSIVE counter(n) AS (\n  SELECT 1 UNION ALL\n  SELECT n+1 FROM counter WHERE n<5\n)\nSELECT n FROM counter;",
    },
}


# Authorizer callback with enhanced output
def authorizer_callback(
    type_of_operation, arg1, arg2, dbname, innermost_trigger_or_view
):
    operation_name = CONSTANTS.get(type_of_operation, "UNKNOWN")
    operations.append(
        {
            "operation": operation_name,
            "arg1": arg1,
            "arg2": arg2,
            "dbname": dbname,
            "innermost_trigger_or_view": innermost_trigger_or_view,
        }
    )
    return sqlite3.SQLITE_OK


# Execute SQL operations and record output
operations = []

by_operation = {}

for operation, sql in sql_examples.items():
    print("## " + operation + "\n")
    conn = sqlite3.connect(":memory:")
    operations = []
    if sql["setup"]:
        conn.executescript(sql["setup"])
        print("Setup SQL:\n```sql\n" + sql["setup"] + "\n```\n")
    conn.set_authorizer(authorizer_callback)
    conn.executescript(sql["example"])
    print("SQL:\n```sql\n" + sql["example"] + "\n```\n")
    # At least one operation must have the expected name
    if not any(o["operation"] == operation for o in operations):
        print(f"This example did not trigger any {operation} operations\n\n")
    by_operation[operation] = {
        "setup_sql": sql["setup"],
        "example_sql": sql["example"],
        "operations": operations,
    }
    print("Operations:\n\n```")
    for op in operations:
        args = [
            f'{key}="{value}"'
            for key, value in op.items()
            if value is not None and key != "operation"
        ]
        print(f'{op["operation"]}\t{", ".join(args)}')
    conn.close()
    print("```\n")

with open("operations.json", "w") as fp:
    json.dump(by_operation, fp, indent=2)
    fp.write("\n")
