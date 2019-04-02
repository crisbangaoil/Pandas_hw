var streetmap = 
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets-basic",
    accessToken: API_KEY
  });

  var darkmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.dark",
    accessToken: API_KEY
  });

var burritos = data2;

var breakfastmarkers = [];
var seafoodmarkers = [];
var vegetarianmarkers = [];
var carnemarkers = [];
var carnitasmarkers = [];
var californiamarkers = [];
var specialtymarkers = [];
var pollomarkers = [];

// Loop through the cities array and create one marker for each city object
for (var i = 0; i < burritos.length; i++) {

  // Conditionals for burritos points
  var color = "";
  if (burritos[i].type === "Breakfast") {
    color = "yellow";
  }
  else if (burritos[i].type === "Seafood") {
    color = "blue";
  }
  else if (burritos[i].type === "Vegetarian") {
    color = "green";
  }
  else if (burritos[i].type === "Carne Asada / Beef") {
    color = "red";
  }
  else if (burritos[i].type === "Carnitas / Pork") {
    color = "pink";
  }
  else if (burritos[i].type === "California") {
    color = "orange";
  }
  else if (burritos[i].type === "Specialty") {
    color = "purple";
  }
  else {
    color = "lime";
  }


  // Add circles to map
  if (burritos[i].type === "Breakfast") {
    breakfastmarkers.push(
      L.circle(burritos[i].location, {
        fillOpacity: 0.4,
        color: color,
        fillColor: color,
        // Adjust radius
        radius: burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla
    }).bindPopup("<h1>" + burritos[i].restuarant + "<h2>" + burritos[i].burrito_name + "</h1> <hr> <h3>tortilla score: " + burritos[i].tortilla + "</h3>"));
  }
  else if   
  (burritos[i].type === "Seafood") {
    seafoodmarkers.push(
      L.circle(burritos[i].location, {
        fillOpacity: 0.4,
        color: color,
        fillColor: color,
        // Adjust radius
        radius: burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla
      }).bindPopup("<h1>" + burritos[i].restuarant + "<h2>" + burritos[i].burrito_name + "</h1> <hr> <h3>tortilla score: " + burritos[i].tortilla + "</h3>"));
  }
  else if
  (burritos[i].type === "Vegetarian") {
    vegetarianmarkers.push(
      L.circle(burritos[i].location, {
        fillOpacity: 0.4,
        color: color,
        fillColor: color,
        // Adjust radius
        radius: burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla
      }).bindPopup("<h1>" + burritos[i].restuarant + "<h2>" + burritos[i].burrito_name + "</h1> <hr> <h3>tortilla score: " + burritos[i].tortilla + "</h3>"));
  }
  else if
  (burritos[i].type === "Carne Asada / Beef") {
    carnemarkers.push(
      L.circle(burritos[i].location, {
        fillOpacity: 0.4,
        color: color,
        fillColor: color,
        // Adjust radius
        radius: burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla
      }).bindPopup("<h1>" + burritos[i].restuarant + "<h2>" + burritos[i].burrito_name + "</h1> <hr> <h3>tortilla score: " + burritos[i].tortilla + "</h3>"));
  }
  else if
  (burritos[i].type === "Carnitas / Pork") {
    carnitasmarkers.push(
      L.circle(burritos[i].location, {
        fillOpacity: 0.4,
        color: color,
        fillColor: color,
        // Adjust radius
        radius: burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla
      }).bindPopup("<h1>" + burritos[i].restuarant + "<h2>" + burritos[i].burrito_name + "</h1> <hr> <h3>tortilla score: " + burritos[i].tortilla + "</h3>"));
  }
  else if
  (burritos[i].type === "California") {
    californiamarkers.push(
      L.circle(burritos[i].location, {
        fillOpacity: 0.4,
        color: color,
        fillColor: color,
        // Adjust radius
        radius: burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla
      }).bindPopup("<h1>" + burritos[i].restuarant + "<h2>" + burritos[i].burrito_name + "</h1> <hr> <h3>tortilla score: " + burritos[i].tortilla + "</h3>"));
  }
  else if
  (burritos[i].type === "Specialty") {
    specialtymarkers.push(
      L.circle(burritos[i].location, {
        fillOpacity: 0.4,
        color: color,
        fillColor: color,
        // Adjust radius
        radius: burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla
      }).bindPopup("<h1>" + burritos[i].restuarant + "<h2>" + burritos[i].burrito_name + "</h1> <hr> <h3>tortilla score: " + burritos[i].tortilla + "</h3>"));
  }
  else 
  {
    pollomarkers.push(
      L.circle(burritos[i].location, {
        fillOpacity: 0.4,
        color: color,
        fillColor: color,
        // Adjust radius
        radius: burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla * burritos[i].tortilla
      }).bindPopup("<h1>" + burritos[i].restuarant + "<h2>" + burritos[i].burrito_name + "</h1> <hr> <h3>tortilla score: " + burritos[i].tortilla + "</h3>"));
  }
}

// Create two separate layer groups: one for cities and one for states
var carneasadaburrito = L.layerGroup(carnemarkers);
var breakfastburrito = L.layerGroup(breakfastmarkers);
var seafoodburrito = L.layerGroup(seafoodmarkers);
var specialtyburrito = L.layerGroup(specialtymarkers);
var carnitasburrito = L.layerGroup(carnitasmarkers);
var californiaburrito = L.layerGroup(californiamarkers);
var vegetarianburrito = L.layerGroup(vegetarianmarkers);
var polloburrito = L.layerGroup(pollomarkers);



// Create a baseMaps object
var baseMaps = {
  "Street Map": streetmap,
  "Dark Map": darkmap
};

// Create an overlay object
var overlayMaps = {
  Carne: carneasadaburrito,
  Carnitas : carnitasburrito,
  Pollo : polloburrito,
  California : californiaburrito,
  Breakfast : breakfastburrito,
  Seafood : seafoodburrito,
  Vegetarian : vegetarianburrito,
  Specialty : specialtyburrito
};

// Create a map object
var myMap = L.map("map", {
  center: [32.7157, -117.1611],
  zoom: 13,
  layers: [streetmap, carneasadaburrito, carnitasburrito, polloburrito, californiaburrito,
    breakfastburrito, seafoodburrito, vegetarianburrito, specialtyburrito]
});

// Pass our map layers into our layer control
// Add the layer control to the map
L.control.layers(baseMaps, overlayMaps, {
  collapsed: true
}).addTo(myMap);