// Get references to the tbody element, input field and button

var $tbody = document.querySelector("tbody");
var $restInput = document.querySelector("#Restaurant");
var $searchBtn = document.querySelector("#search");
var $costInput = document.querySelector("#Cost");
var $typeInput = document.querySelector("#Type");
// var $countryInput = document.querySelector("#country");
// var $shapeInput = document.querySelector("#shape");
var $resetBtn = document.querySelector("#reset");
// event listener for searchButton to invoke handleSearchButtonClick

$searchBtn.addEventListener("click", handleSearchButtonClick);
$resetBtn.addEventListener("click", resetData);

// Set filteredData var to the contents of data dict
var filteredData = data;
var resetData = data;
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filteredData.length; i++) {
    // Get current address object and its fields
    var myData = filteredData[i];
    var fields = Object.keys(myData);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // create a new cell and set the inner text to current adress object value
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = myData[field];
    }

  }

}
function handleSearchButtonClick(event) {
  // prevent page from refreshing
   event.preventDefault();
   var filterName = $restInput.value.trim().toLowerCase();
   if (filterName != "") { 
     filteredData = filteredData.filter(function(data) { 
       var dataName = data.Restaurant.toLowerCase(); 
       return dataName === filterName;
     });
 }; 
   var filterCost = Math.floor($costInput.value.trim()); 
   if (filterCost !="") { 
     filteredData = filteredData.filter(function(data) { 
       var dataCost = Math.floor(data.Average_of_Cost);
       return dataCost === filterCost; 
     }); 
   };  
   var filterType = $typeInput.value.trim().toLowerCase(); 
   if (filterType!="") { 
     filteredData = filteredData.filter(function(data) { 
       var dataType = data.Type.toLowerCase(); 
       return dataType === filterType; 
     }); 
   };
    renderTable(); 
   }      
  
  function resetData() {  
    filteredData = data;
    $restInput.value = "";
    $costInput.value = "";
    $typeInput.value = "";
    renderTable();
  
  }

  function resetForm() {
  
    document.getElementById("myForm").reset();
  
  }
renderTable();