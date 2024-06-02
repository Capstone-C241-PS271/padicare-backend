from .base import db, BaseModel
from sqlalchemy.orm import relationship

class Comment(BaseModel):
    __tablename__ = db.metadata.tables['comment']
    
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    post = relationship("Post", back_populates="comments")
    author = relationship("User", back_populates="comments")

    def serialize(self):
        return {
            'id': self.id,
            'post_id': self.post_id,
            'author_id': self.author_id,
            'content': self.content,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
