from .base import db, BaseModel
from sqlalchemy.orm import relationship

class User(BaseModel):
    __tablename__ = 'user'
    
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name, 
            'email': self.email,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
