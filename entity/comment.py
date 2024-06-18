from .base import db, BaseModel
from sqlalchemy.orm import relationship

class Comment(BaseModel):
    __tablename__ = 'comment'
    
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    author = relationship('User')

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'author': self.author.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
