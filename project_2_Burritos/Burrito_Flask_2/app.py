# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/Overall<br/>"
        f"/Meat<br/>"
        f"/Tortilla<br/>"
    )


@app.route("/Overall")
def index():

    return render_template("index2.html")

@app.route("/Meat")
def meat():

    return render_template("index_meat.html")

@app.route("/Tortilla")
def tortilla():

    return render_template("index_tortilla.html")

# @app.route("/Cost")
# def cost():

#     return render_template("index_cost.html")



if __name__ == "__main__":
    app.run(debug=True)