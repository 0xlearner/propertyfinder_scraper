from propertyfinder_eg.models import (
    PropertyFinder_Sale,
    PropertyFinder_Rent,
    PropertyFinder_Commercial,
    PropertyFinder_NewProjects,
    session,
)


class PropertyFinderSalePipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates items table.
        """
        # engine = db_connect()
        # create_items_table(engine)
        # self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Process the item and store to database.
        """
        # session = self.Session()
        instance = (
            session.query(PropertyFinder_Sale)
            .filter_by(**item)
            .first()
        )
        if instance:
            return instance
        else:
            property_finder_sale_item = PropertyFinder_Sale(**item)
            session.add(property_finder_sale_item)

        try:
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item


class PropertyFinderRentPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates items table.
        """
        # engine = db_connect()
        # create_items_table(engine)
        # self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Process the item and store to database.
        """
        # session = self.Session()
        try:
            instance = (
                session.query(PropertyFinder_Rent)
                .filter_by(**item)
                .first()
            )
            if instance:
                return instance
            else:
                property_finder_rent_item = PropertyFinder_Rent(**item)
                session.add(property_finder_rent_item)
        except:
            pass

        try:
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item


class PropertyFinderCommercialPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates items table.
        """
        # engine = db_connect()
        # create_items_table(engine)
        # self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Process the item and store to database.
        """
        # session = self.Session()
        try:
            instance = (
                session.query(PropertyFinder_Commercial)
                .filter_by(**item)
                .first()
            )
            if instance:
                return instance
            else:
                property_finder_commercial_item = PropertyFinder_Commercial(**item)
                session.add(property_finder_commercial_item)
        except:
            pass

        try:
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item


class PropertyFinderNewProjectsPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates items table.
        """
        # engine = db_connect()
        # create_items_table(engine)
        # self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Process the item and store to database.
        """
        # session = self.Session()
        try:
            instance = (
                session.query(PropertyFinder_NewProjects).filter_by(**item).first()
            )
            if instance:
                return instance
            else:
                property_finder_commercial_item = PropertyFinder_NewProjects(**item)
                session.add(property_finder_commercial_item)
        except:
            pass

        try:
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
