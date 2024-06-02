from .base import db, BaseModel
from sqlalchemy.orm import relationship

class Prediction(BaseModel):
    __tablename__ = 'prediction'
    
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image = db.Column(db.String(255))
    result = db.Column(db.String(255))
    suggestion = db.Column(db.Text)

    author = relationship("User", back_populates="predictions")
