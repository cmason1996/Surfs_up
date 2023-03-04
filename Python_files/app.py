#import dependencies
from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#create the engine that allows access to the SQLite file and query the database
engine = create_engine("sqlite:///hawaii.sqlite")

#creates a base for the tables to be reflected to
Base = automap_base()

#creates the reflection of each table so we can query them directly
Base.prepare(engine, reflect=True)

#create avariable for the classes so we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from the database file to the Python file
session = Session(engine)

#set up the and define Flask
app = Flask(__name__)

#define the routes for the webpage
@app.route("/")

#add the route information for the pages with return statements and f-strings to reference other routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end
    ''') 

# creating the precipitation route
@app.route("/api/v1.0/precipitation")

# creating the precipitation function
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# create the stations route
@app.route("/api/v1.0/stations")

#create the stations function
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# create the temperature observations (tobs) route
@app.route("/api/v1.0/tobs")

#create the stations function
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#create the routes for the starting and ending date for the statistical analysis
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#create the statistical analysis function
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)