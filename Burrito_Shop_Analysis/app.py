import os
from flask import Flask, jsonify, render_template
import geocoder
import numpy as np
import requests
from apiclient import discovery
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask import send_from_directory

import gmaps
gmaps.configure(api_key='AIzaSyDPnVYm6BlA9uH623iAccI-7VKj88X5LNY')

engine = create_engine("sqlite:///db/burritoShop.sqlite?check_same_thread=False")
#read CSV and save as DF
burrito_file = "Resources/Burrito_Clean_with_full_address.csv"
burrito_df = pd.read_csv(burrito_file)

#create function for geo coding addresses
def geomapper(address):
    g = geocoder.google(address, key='AIzaSyDPnVYm6BlA9uH623iAccI-7VKj88X5LNY')
    lat = g.json['lat']
    long = g.json['lng']
    return (f'{lat},{long}')
#Create function called locateAddresses that adds latitude and longitude columns for geomapping
#Assumes df have column "Full_Address"

def locateAddresses(burritoDF):
    burritoDF["geo"] = 0
    burritoDF["geo"]= burritoDF.Full_Address.apply(lambda x: geomapper(x))
    
    #split geo column to assign values in latitude and longitude 
    burritoDF[['Lat', 'Lng']] = burritoDF.geo.str.split(',', expand = True)
    del burritoDF['geo']
    return 
#apply function to burrito_df to pull Lat, Lng for addresses on CSV
# locateAddresses(burrito_df)

# burrito_df.to_csv('Resources/BurritoCleanLatLng.csv', index=False, header=True)
# print(burrito_df)
#read CSV that we saved with Lat & long data
burrito_loc_file = "Resources/BurritoCleanLatLng.csv"
burrito_loc_df = pd.read_csv(burrito_loc_file)
# print(burrito_loc_df)
# #################################################

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to our table
burrito_shops = Base.classes.burritoShopList
# Create our session (link) from Python to the DB
session = Session(engine)
# print(burrito_shops)
# #write DF to SQLite DB

burrito_loc_df.to_sql(name='burritoShopList', con=engine, schema=None, if_exists='append', index=False)
# Flask Setup
#################################################
#################################################
app = Flask(__name__)

# Flask Routes
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/shops")
def shops():
    shop_data = session.query(burrito_shops).filter(burrito_shops.Restaurant.isnot(None)) #.all()
    # print(shop_data)
    shop_data_df = pd.read_sql(shop_data.statement, session.bind).transpose()
    # burrito_shop_info = {}
    # for result in shop_data_df:
    #     burrito_shop_info["ID"] = result[0]
    #     burrito_shop_info["Restaurant"] = result[1]
    #     burrito_shop_info["Burrito_Name"] = result[2]
    #     burrito_shop_info["Type"] = result[3]
    #     burrito_shop_info["Full_Address"] = result[4]
    #     burrito_shop_info["Number_of_Reviews"] = result[5]
    #     burrito_shop_info["Average_of_Yelp"] = result[6]
    #     burrito_shop_info["Average_of_Google"] = result[7]
    #     burrito_shop_info["Average_of_Cost"] = result[8]
    #     burrito_shop_info["Average_of_Hunger"] = result[9]
    #     burrito_shop_info["Average_of_Tortilla"] = result[10]
    #     burrito_shop_info["Average_of_Temp"] = result[11]
    #     burrito_shop_info["Average_of_Meat"] = result[12]
    #     burrito_shop_info["Average_of_Fillings"] = result[13]
    #     burrito_shop_info["Average_of_Meat_filling"] = result[14]
    #     burrito_shop_info["Average_of_Uniformity"] = result[15]
    #     burrito_shop_info["Average_of_Salsa"] = result[16]
    #     burrito_shop_info["Average_of_Synergy"] = result[17]
    #     burrito_shop_info["Average_of_Wrap"] = result[18]
    #     burrito_shop_info["Average_of_overall"] = result[19]
    #     burrito_shop_info["Lat"] = result[20]
    #     burrito_shop_info["Lng"] = result[21]
    #     burrito_shop_info["URL"] = result[21]
    shop_data_dict = shop_data_df.to_dict()
    # print(shop_data_dict)
    return jsonify(shop_data_dict)

# @app.route("/burritoshop")
# def burritoshop():
#     """Return the burritoshop for a given input."""
#     # sel = [
#     #     burrito_shops.ID,
#     #     burrito_shops.Restaurant,
#     #     burrito_shops.Burrito_Name,
#     #     burrito_shops.Type,
#     #     burrito_shops.Full_Address,
#     #     burrito_shops.Number_of_Reviews,
#     #     burrito_shops.Average_of_Yelp,
#     #     burrito_shops.Average_of_Google,                
#     #     burrito_shops.Average_of_Cost,
#     #     burrito_shops.Average_of_Hunger,
#     #     burrito_shops.Average_of_Tortilla,
#     #     burrito_shops.Average_of_Temp,
#     #     burrito_shops.Average_of_Meat,
#     #     burrito_shops.Average_of_Fillings,
#     #     burrito_shops.Average_of_Meat_filling,
#     #     burrito_shops.Average_of_Uniformity,
#     #     burrito_shops.Average_of_Salsa,
#     #     burrito_shops.Average_of_Synergy,
#     #     burrito_shops.Average_of_Wrap,
#     #     burrito_shops.Average_of_overall,
#     #     burrito_shops.Lat,
#     #     burrito_shops.Lng,
#     #     burrito_shops.URL
#     # ]
                
#     results_q = session.query(burrito_shops).filter(burrito_shops.Restaurant.isnot(None))
#     results = pd.read_sql(results_q.statement, session.bind)
#     # results = session.query(burrito_shops).filter(burrito_shops.Restaurant.isnot(None)).all()
#     # Create a dictionary entry for each row of metadata information
#     burrito_shop_info = {}
#     for result in results:
#         burrito_shop_info["ID"] = result[0]
#         burrito_shop_info["Restaurant"] = result[1]
#         burrito_shop_info["Burrito_Name"] = result[2]
#         burrito_shop_info["Type"] = result[3]
#         burrito_shop_info["Full_Address"] = result[4]
#         burrito_shop_info["Number_of_Reviews"] = result[5]
#         burrito_shop_info["Average_of_Yelp"] = result[6]
#         burrito_shop_info["Average_of_Google"] = result[7]
#         burrito_shop_info["Average_of_Cost"] = result[8]
#         burrito_shop_info["Average_of_Hunger"] = result[9]
#         burrito_shop_info["Average_of_Tortilla"] = result[10]
#         burrito_shop_info["Average_of_Temp"] = result[11]
#         burrito_shop_info["Average_of_Meat"] = result[12]
#         burrito_shop_info["Average_of_Fillings"] = result[13]
#         burrito_shop_info["Average_of_Meat_filling"] = result[14]
#         burrito_shop_info["Average_of_Uniformity"] = result[15]
#         burrito_shop_info["Average_of_Salsa"] = result[16]
#         burrito_shop_info["Average_of_Synergy"] = result[17]
#         burrito_shop_info["Average_of_Wrap"] = result[18]
#         burrito_shop_info["Average_of_overall"] = result[19]
#         burrito_shop_info["Lat"] = result[20]
#         burrito_shop_info["Lng"] = result[21]
#         burrito_shop_info["URL"] = result[21]
#     print(burrito_shop_info)
#     return jsonify(burrito_shop_info)
if __name__ == '__main__':
    app.run(debug=True)