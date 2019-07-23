# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound
import sqlite3
from .utils import create_db, populate_models
from pathlib import Path

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound

def init_db():
    dbfile = Path('./products.db')
    if dbfile.is_file():
        pass
    else:
        # create products table
        create_db([Product])
        # initialise products table
        populate_models(data_source)

init_db()
