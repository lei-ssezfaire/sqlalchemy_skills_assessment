"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):

    __tablename__ = "models"

    model_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    brand_name = db.Column(db.String(50))
    model_name = db.Column(db.String(50), nullable=False)

    brand = db.relationship('Brand', secondary='model_brands', backref='models')

    def __repr__(self):
        """Show info about model."""

        return "<Model id=%s year=%s name=%s>" % (self.model_id, self.year, self.model_name)


class Brand(db.Model):

    __tablename__ = "brands"

    brand_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_name = db.Column(db.String(50), nullable=False)
    founded = db.Column(db.Integer)
    headquarters = db.Column(db.String(50))
    discontinued = db.Column(db.Integer)

    def __repr__ (self):
        """Show info about brand"""

        return "<Brand id=%s brand_name=%s>" % (self.brand_id, self.brand_name)


class ModelBrand(db.Model):

    __tablename__ = "model_brands"

    model_brand_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model_id = db.Column(db.Integer, db.ForeignKey('models.model_id'), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.brand_id'), nullable=False)



# End Part 1
##############################################################################
# Query functions


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.options(db.joinedload('brand')).filter(Model.year == year).all()

    for model in models:
        print model.model_name, model.brand_name, model.headquarters
        

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''


    models = db.session.query(Model.brand_name, Model.model_name).order_by(Model.brand_name).all()

    for brand_name, model_name in models:
        print brand_name, model_name


def search_brands_by_name(mystr):
    """Function that takes a string and returns a list of objects that are brands whose name contains or is equal to that string"""

    return Brand.query.filter( db.or_(Brand.brand_name == mystr, Brand.brand_name.like('%' + mystr + '%')) ).all()


def get_models_between(start_year, end_year):
    """Takes in start year and end year and returns list of objects that are models with years that fall between the start year and end year"""

    return Model.query.filter(Model.year > start_year, Model.year < end_year).all()


##############################################################################
# Helper functions


def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///cars'
    app.config['SQLALCHEMY_ECHO'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
