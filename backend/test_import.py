import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from app.core.config.database import Base
    print("✓ Successfully imported Base from database")
    
    from app.core.database.base import BaseModel
    print("✓ Successfully imported BaseModel")
    
    print("All imports working correctly!")
except ImportError as e:
    print(f"✗ Import error: {e}")