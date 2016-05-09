"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(model_name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.model_name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter( db.or_(Brand.discontinued != None, Brand.founded < 1950) ).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.options(db.joinedload('brand')).filter(Model.year == year).all()

    for model in models:
        print model.model_name, model.brand_name, model.headquarters


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    models = db.session.query(Model.brand_name, Model.model_name).group_by(Model.brand_name).order_by(Model.brand_name).all()

    for brand_name, model_name in models:
        print brand_name, model_name

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """Function that takes a string and returns a list of objects that are brands whose name contains or is equal to that string"""

    return Brand.query.filter( db.or_(Brand.brand_name == mystr, Brand.brand_name.like('%' + mystr + '%')) ).all()


def get_models_between(start_year, end_year):
    """Takes in start year and end year and returns list of objects that are models with years that fall between the start year and end year"""

    return Model.query.filter(Model.year > start_year, Model.year < end_year).all()


# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# Brand.query.filter_by(brand_name='Ford') returns <flask_sqlalchemy.BaseQuery object at 0x10de24d90>. The datatype of this object is <class 'flask_sqlalchemy.BaseQuery'>. 


# 2. In your own words, what is an association table, and what *type* of relationship does an association table manage?

# An association table is a table that is made solely for the purpose of connecting two other tables together. It includes only 1 primary key, and 2 foreign keys. Association tables manage Many to Many relationships.


