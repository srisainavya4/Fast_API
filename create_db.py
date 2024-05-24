import models

try:
    models.create_tables()
    print("Tables created successfully.")
except Exception as e:
    print("An error occurred while creating tables:", e)
