from sqlalchemy import Column, String, Integer, Text, Boolean
from sqlalchemy.orm import relationship
from app.core.database.base import BaseModel

class Institution(BaseModel):
    __tablename__='institutions'

    name = Column(String(255), nullable=False, unique=True)
    domain = Column(String(255), nullable=True, unique=True)
    address = Column(Text, nullable=True)
    contact_email = Column(String(255), nullable=True)
    is_active = Column(Boolean,default=True)
    max_users = Column(Integer, default=100)
    storage_limit = Column(Integer, default=1073741824) # 1GB in bytes

    # Relationships
    users = relationship("User", back_populates="institution")
    portals = relationship("EducationalPortal", back_populates="institution")

    def __repr__(self):
        return f"<Institution(id={self.id}, name={self.name})>"