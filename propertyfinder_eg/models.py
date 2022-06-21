from sqlalchemy import Column, Date, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from . import settings

engine = create_engine(settings.DATABSE_URL)
Session = sessionmaker(bind=engine)
session = Session()
DeclarativeBase = declarative_base()


class PropertyFinder_Sale(DeclarativeBase):
    """
    Defines the sale model
    """

    __tablename__ = "propertyfinder_sale"
    _id = Column(Integer, primary_key=True)
    URL = Column("URL", String)
    Breadcrumb = Column("Breadcrumb", String)
    Price = Column("Price", String)
    Title = Column("Title", String)
    Type = Column("Type", String)
    Bedrooms = Column("Bedrooms", String)
    Bathrooms = Column("Bathrooms", String)
    Area = Column("Area", String)
    Location = Column("Location", String)
    Agent_company = Column("Agent_company", String)
    Agent_name = Column("Agent_name", String)
    Description = Column("Description", String)
    Amenities = Column("Amenities", String)
    Reference = Column("Reference", String)
    Listed_date = Column("Listed_date", String)
    Image_url = Column("Image_url", String)
    Phone_number = Column("Phone_number", String)
    Map_location = Column("Map_location", String)


class PropertyFinder_Rent(DeclarativeBase):
    """
    Defines the rent model
    """

    __tablename__ = "propertyfinder_rent"
    _id = Column(Integer, primary_key=True)
    URL = Column("URL", String)
    Breadcrumb = Column("Breadcrumb", String)
    Price = Column("Price", String)
    Title = Column("Title", String)
    Type = Column("Type", String)
    Bedrooms = Column("Bedrooms", String)
    Bathrooms = Column("Bathrooms", String)
    Area = Column("Area", String)
    Location = Column("Location", String)
    Agent_company = Column("Agent_company", String)
    Agent_name = Column("Agent_name", String)
    Description = Column("Description", String)
    Amenities = Column("Amenities", String)
    Reference = Column("Reference", String)
    Listed_date = Column("Listed_date", String)
    Image_url = Column("Image_url", String)
    Phone_number = Column("Phone_number", String)
    Map_location = Column("Map_location", String)


class PropertyFinder_Commercial(DeclarativeBase):
    """
    Defines the commercial model
    """

    __tablename__ = "propertyfinder_commercial"
    _id = Column(Integer, primary_key=True)
    URL = Column("URL", String)
    Breadcrumb = Column("Breadcrumb", String)
    Price = Column("Price", String)
    Title = Column("Title", String)
    Type = Column("Type", String)
    Bedrooms = Column("Bedrooms", String)
    Bathrooms = Column("Bathrooms", String)
    Area = Column("Area", String)
    Location = Column("Location", String)
    Agent_company = Column("Agent_company", String)
    Agent_name = Column("Agent_name", String)
    Description = Column("Description", String)
    Amenities = Column("Amenities", String)
    Reference = Column("Reference", String)
    Listed_date = Column("Listed_date", String)
    Image_url = Column("Image_url", String)
    Phone_number = Column("Phone_number", String)
    Map_location = Column("Map_location", String)


class PropertyFinder_NewProjects(DeclarativeBase):
    """
    Defines the new projects model
    """

    __tablename__ = "propertyfinder_new_projects"
    _id = Column(Integer, primary_key=True)
    URL = Column("URL", String)
    Breadcrumb = Column("Breadcrumb", String)
    Price = Column("Price", String)
    Title = Column("Title", String)
    Type = Column("Type", String)
    Bedrooms = Column("Bedrooms", String)
    Bathrooms = Column("Bathrooms", String)
    Area = Column("Area", String)
    Location = Column("Location", String)
    Agent_company = Column("Agent_company", String)
    Agent_name = Column("Agent_name", String)
    Description = Column("Description", String)
    Amenities = Column("Amenities", String)
    Reference = Column("Reference", String)
    Listed_date = Column("Listed_date", String)
    Delivery_date = Column("Delivery_date", String)
    Image_url = Column("Image_url", String)
    Phone_number = Column("Phone_number", String)
    Map_location = Column("Map_location", String)
