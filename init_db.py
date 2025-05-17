from run import app
from app import db
print("j")
with app.app_context():
    db.create_all()
    print("✅ Tables created successfully.")
