from extensions import db  # Import db from extensions.py

# User table
class User(db.Model):
    __tablename__ = 'user'  # Specifies the table name

    # Define the columns for the 'user' table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Primary key
    email = db.Column(db.String(255), unique=True, nullable=False)  # Email field, unique and required
    password = db.Column(db.String(255), nullable=False)  # Password field, required (hashed)
    description = db.Column(db.Text, nullable=True)  # Description field, optional text
    admin = db.Column(db.Boolean, default=False, nullable=False)  # Admin field, boolean, default is False

    # String representation of the User object for debugging
    def __repr__(self):
        return f'<User {self.email}>'


# Chatroom table
class Chatroom(db.Model):
    __tablename__ = 'chatroom'  # Specifies the table name

    # Define the columns for the 'chatroom' table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Primary key
    name = db.Column(db.String(255), nullable=False)  # Name field, required
    description = db.Column(db.Text, nullable=True)  # Description field, optional text

    # String representation of the Chatroom object for debugging
    def __repr__(self):
        return f'<Chatroom {self.name}>'


# UserBudget table
class UserBudget(db.Model):
    __tablename__ = 'user_budget'  # Specifies the table name

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Primary key
    category = db.Column(db.String(255), nullable=False, index=True)  # Indexed for performance
    amount = db.Column(db.Float, nullable=False)  # Amount cannot be null

    # String representation of the UserBudget object for debugging
    def __repr__(self):
        return f'<UserBudget {self.category}: {self.amount}>'


# CategoryThreshold table
class CategoryThreshold(db.Model):
    __tablename__ = 'category_thresholds'  # Specifies the table name

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Primary key
    category = db.Column(db.String(255), nullable=False, index=True)  # Indexed for performance
    threshold = db.Column(db.Float, nullable=False)  # Threshold cannot be null

    # String representation of the CategoryThreshold object for debugging
    def __repr__(self):
        return f'<CategoryThreshold {self.category}: {self.threshold}>'
