# @app.route("/api/v1.0/tobs")
# def temp():
#     # Choose the station with the highest number of temperature observations.
#       highest_temp_count = session.query(Measurement.station, func.count(Measurement.tobs)).\
#       group_by(Measurement.station).order_by(func.count(Measurement.tobs).desc()).first()
#       # print(highest_temp_count)
#       # # Query the last 12 months of temperature observation data for this station and plot the results as a histogram
#       # Calculate the date 1 year ago from the last data point in the database
#       last_dates = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
#       dates = datetime.strptime('2017-08-23', '%Y-%m-%d')
#       year_ago = dates - timedelta(days=365)
#       temp_data = session.query(Measurement.date, Measurement.tobs).\
#       filter(Measurement.date > year_ago).filter(Measurement.station == highest_temp_count[0]).all()
#       # print(temp_data)
#       # Save the query results as a Pandas DataFrame
#       temp_data_df = pd.DataFrame(temp_data)
#       temp_data_dict = temp_data_df.to_dict('index')
#       return jsonify(temp_data_dict)
      
# @app.route("/api/v1.0/<start>")
# def start_date(start):
#     """Fetch the start date for trip for which start date matches
#        the path variable supplied by the user, or a 404 if not."""

#     temp_details = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
#             filter(Measurement.date >= start).all()
#     temp_details_df = pd.DataFrame(temp_details, columns=['TMIN', 'TAVG','TMAX'])
#     temp_details_dict = temp_details_df.to_dict()
#     return jsonify(temp_details_dict)

# @app.route("/api/v1.0/<starting>/<ending>")
# def start_end_date(starting,ending):
#     """Fetch the start date for trip for which start date matches
#        the path variable supplied by the user, or a 404 if not."""

#     temp_details2 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
#             filter(Measurement.date >= starting).filter(Measurement.date <= ending).all()
#     temp_details_df2 = pd.DataFrame(temp_details2, columns=['TMIN', 'TAVG','TMAX'])
#     temp_details_dict2 = temp_details_df2.to_dict()
#     return jsonify(temp_details_dict2)

# @app.route("/burritoshop/<input>")
# def burrito_shops(input):
#     """Return the burritoshop for a given input."""
#     sel = [
#         burrito_shops.ID,
#         burrito_shops.Restaurant,
#         burrito_shops.Burrito_Name,
#         burrito_shops.Type,
#         burrito_shops.Full_Address,
#         burrito_shops.Number_of_Reviews,
#         burrito_shops.Average_of_Yelp,
#         burrito_shops.Average_of_Google,                
#         burrito_shops.Average_of_Cost,
#         burrito_shops.Average_of_Hunger,
#         burrito_shops.Average_of_Tortilla,
#         burrito_shops.Average_of_Temp,
#         burrito_shops.Average_of_Meat,
#         burrito_shops.Average_of_Fillings,
#         burrito_shops.Average_of_Meat_filling,
#         burrito_shops.Average_of_Uniformity,
#         burrito_shops.Average_of_Salsa,
#         burrito_shops.Average_of_Synergy,
#         burrito_shops.Average_of_Wrap,
#         burrito_shops.Average_of_overall,
#         burrito_shops.Lat,
#         burrito_shops.Lng,
#         burrito_shops.URL
#           ]
#                 
#     results = db.session.query(*sel).filter(burrito_shops.input == input).all()
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
#         burrito_shop_info["Average_of_Cost"] = result[21]
#     print(burrito_shop_info)
#     return jsonify(burrito_shop_info)
