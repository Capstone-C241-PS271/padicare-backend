from .base import db, BaseModel
from sqlalchemy.orm import relationship

class Post(BaseModel):
    __tablename__ = 'post'
    
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)

    author = relationship('User')

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'author': self.author.name
        }
