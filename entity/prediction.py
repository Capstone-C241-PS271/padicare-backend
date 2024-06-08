from .base import db, BaseModel
from sqlalchemy.orm import relationship

class Prediction(BaseModel):
    __tablename__ = 'prediction'
    
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image = db.Column(db.Text)
    result = db.Column(db.String(255))
    suggestion = db.Column(db.Text)

    def serialize(self):
        return {
            'id': self.id,
            'author_id': self.author_id,
            'image': self.image,
            'result': self.result,
            'suggestion': self.suggestion,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
