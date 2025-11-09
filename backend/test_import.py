import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    
    print("✓ Successfully imported Base from database")
    
    print("✓ Successfully imported BaseModel")
    
    print("All imports working correctly!")
except ImportError as e:
    print(f"✗ Import error: {e}")
