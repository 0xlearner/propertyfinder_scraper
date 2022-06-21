"""Initial

Revision ID: a165f7cadd52
Revises: 
Create Date: 2022-06-20 21:38:39.325602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a165f7cadd52'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('propertyfinder_commercial',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('URL', sa.String(), nullable=True),
    sa.Column('Breadcrumb', sa.String(), nullable=True),
    sa.Column('Price', sa.String(), nullable=True),
    sa.Column('Title', sa.String(), nullable=True),
    sa.Column('Type', sa.String(), nullable=True),
    sa.Column('Bedrooms', sa.String(), nullable=True),
    sa.Column('Bathrooms', sa.String(), nullable=True),
    sa.Column('Area', sa.String(), nullable=True),
    sa.Column('Location', sa.String(), nullable=True),
    sa.Column('Agent_company', sa.String(), nullable=True),
    sa.Column('Agent_name', sa.String(), nullable=True),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('Amenities', sa.String(), nullable=True),
    sa.Column('Reference', sa.String(), nullable=True),
    sa.Column('Listed_date', sa.String(), nullable=True),
    sa.Column('Image_url', sa.String(), nullable=True),
    sa.Column('Phone_number', sa.String(), nullable=True),
    sa.Column('Map_location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('propertyfinder_new_projects',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('URL', sa.String(), nullable=True),
    sa.Column('Breadcrumb', sa.String(), nullable=True),
    sa.Column('Price', sa.String(), nullable=True),
    sa.Column('Title', sa.String(), nullable=True),
    sa.Column('Type', sa.String(), nullable=True),
    sa.Column('Bedrooms', sa.String(), nullable=True),
    sa.Column('Bathrooms', sa.String(), nullable=True),
    sa.Column('Area', sa.String(), nullable=True),
    sa.Column('Location', sa.String(), nullable=True),
    sa.Column('Agent_company', sa.String(), nullable=True),
    sa.Column('Agent_name', sa.String(), nullable=True),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('Amenities', sa.String(), nullable=True),
    sa.Column('Reference', sa.String(), nullable=True),
    sa.Column('Listed_date', sa.String(), nullable=True),
    sa.Column('Delivery_date', sa.String(), nullable=True),
    sa.Column('Image_url', sa.String(), nullable=True),
    sa.Column('Phone_number', sa.String(), nullable=True),
    sa.Column('Map_location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('propertyfinder_rent',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('URL', sa.String(), nullable=True),
    sa.Column('Breadcrumb', sa.String(), nullable=True),
    sa.Column('Price', sa.String(), nullable=True),
    sa.Column('Title', sa.String(), nullable=True),
    sa.Column('Type', sa.String(), nullable=True),
    sa.Column('Bedrooms', sa.String(), nullable=True),
    sa.Column('Bathrooms', sa.String(), nullable=True),
    sa.Column('Area', sa.String(), nullable=True),
    sa.Column('Location', sa.String(), nullable=True),
    sa.Column('Agent_company', sa.String(), nullable=True),
    sa.Column('Agent_name', sa.String(), nullable=True),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('Amenities', sa.String(), nullable=True),
    sa.Column('Reference', sa.String(), nullable=True),
    sa.Column('Listed_date', sa.String(), nullable=True),
    sa.Column('Image_url', sa.String(), nullable=True),
    sa.Column('Phone_number', sa.String(), nullable=True),
    sa.Column('Map_location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('propertyfinder_sale',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('URL', sa.String(), nullable=True),
    sa.Column('Breadcrumb', sa.String(), nullable=True),
    sa.Column('Price', sa.String(), nullable=True),
    sa.Column('Title', sa.String(), nullable=True),
    sa.Column('Type', sa.String(), nullable=True),
    sa.Column('Bedrooms', sa.String(), nullable=True),
    sa.Column('Bathrooms', sa.String(), nullable=True),
    sa.Column('Area', sa.String(), nullable=True),
    sa.Column('Location', sa.String(), nullable=True),
    sa.Column('Agent_company', sa.String(), nullable=True),
    sa.Column('Agent_name', sa.String(), nullable=True),
    sa.Column('Description', sa.String(), nullable=True),
    sa.Column('Amenities', sa.String(), nullable=True),
    sa.Column('Reference', sa.String(), nullable=True),
    sa.Column('Listed_date', sa.String(), nullable=True),
    sa.Column('Image_url', sa.String(), nullable=True),
    sa.Column('Phone_number', sa.String(), nullable=True),
    sa.Column('Map_location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('propertyfinder_sale')
    op.drop_table('propertyfinder_rent')
    op.drop_table('propertyfinder_new_projects')
    op.drop_table('propertyfinder_commercial')
    # ### end Alembic commands ###