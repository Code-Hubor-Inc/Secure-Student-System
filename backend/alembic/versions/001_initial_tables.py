# A simple migration to get things working
"""Initial ables

Revision ID: 001
Revises:
Create Date: 2025-11-01 

"""

from alembic import op 
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identififer, used by alembic
revision = '001'
down_revision = None
branch_labels =None
depends_on = None

def upgrade():
    # Create institution table
    op.create_table('institutions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('domain', sa.String(length=255), nullable=True),
        sa.Column('address', sa.Text(), nullable=True),
        sa.Column('contact_email', sa.String(length=255), nullable=True),
        sa.Column('is_Active',sa.Boolean(), nullable=True),
        sa.Column('max_user', sa.Integer(), nullable=True),
        sa.Column('storage_limit', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('domain'),
        sa.UniqueConstraint('name')      
    )

    # Create user table
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('hashed_password', sa.String(length=255), nullable=False),
        sa.Column('full_name', sa.String(length=255), nullable=False),
        sa.Column('is_Active', sa.Boolean(), nullable=True),
        sa.Column('is_superuser', sa.Boolean(), nullable=True),
        sa.Column('last_login', sa.DateTime(), nullable=True),
        sa.Column('institution_id', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['institution_id'], ['institution_id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')              
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)

def downgrade():
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('institutions')