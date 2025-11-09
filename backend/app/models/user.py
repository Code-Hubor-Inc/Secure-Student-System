from sqlalchemy import Column, String, Integer, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database.base import BaseModel

class User(BaseModel):
    __tablename__="users"

    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullabl=False)
    full_name = Column(String(255), nullable=False)
    is_active = Column(Boolean,default=True)
    is_superuser = Column(Boolean, default=False)
    last_login = Column(DateTime, nullable=True)
    institution_id = Column(Integer, ForeignKey('institution.id'), nullable=True)

    # Relationship
    institution = relationship("Institution", back_populates="users")
    file = relationship("SecureFile", back_populates="owner")
    sessions = relationship("PortalSession", back_populates="user")
    audit_logs = relationship("AuditLog", back_populates="user")
    
    def __reps__(self):
        return f"<User(id={self.id}, email={self.email})>"