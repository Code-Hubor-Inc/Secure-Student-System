from sqlalchemy import Column, String, Integer, DateTime, Text, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from app.core.database.base import BaseModel

class SecureFile(BaseModel):
    __tablename__= "secure_files"

    # File information
    original_name = Column(String(500), nullable=False)
    encrypted_name = Column(String(500), nullable=False)
    file_size = Column(Integer, nullable=False) # Size in bytes
    file_type = Column(String(100), nullable=False)

    # Encryption details
    encryption_key_hash = Column(String(255), nullable=False)
    encryption_algorithm = Column(String(50), default="AES-256-GCM")

    # Access control
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    expires_at = Column(DateTime, nullable=False)
    max_downaloads = Column(Integer, default=0)
    is_public = Column(Boolean, default=False)

    # Protection settings
    requires_password = Column(Boolean, default=False)
    password_hash = Column(String(255), nullable=True)
    auto_delete = Column(Boolean,default=False)

    # Relationships
    owner = relationship("User", back_populates="files")
    access_logs = relationship("FileAccessLog", back_populates="file")

    def __repr__(self):
         return f"<SecureFile(id={self.id}, name={self.original_name})>"
    
class FileAccessLog(BaseModel):
    __tablename__= "file_access_log"

    file_id = Column(Integer, ForeignKey('secure_files.id'), nullable=False)
    user_id = Column(Integer,ForeignKey('users.id'), nullable=True)
    access_type = Column(String(50), nullable=False) # 'download', 'view', 'share'
    ip_address = Column(String(45), nullable=True)
    user_agent = Column(Text, nullable=True)
    success = Column(Boolean, default=True)

    # Relationships

    file = relationship("SecureFile", back_populates="access_logs")
    user =relationship("User")

    def __repr__(self):
       return f"<FileAccessLog(file_id={self.file_id}, access_type={self.access_type})>"