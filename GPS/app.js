// set map options

var mylatlng = {lat:23.2599 , lng:77.4126 };
var mapOptions = {
    center : mylatlng,
    zoom : 6,
    mapTypeId : google.maps.mapTypeId.ROADMAP
};

//create Map

var map = new google.maps.Map(document.getElementById("googleMap"));

// create a direct srvice object to use the route method

var directionService = new google.maps.directionService();

//create direction render object which we will use to display the route

var directionsDisplay = new google.maps.DirectionsRenderer();

//bind the directionsRenderer to the map

directionsDisplay.setMap(map);

//function to calculate distance and the location an all

function calcRoute(){
    //create request
    var request = {
        origin:document.getElementById("From").value,
        destination:document.getElementById("To").value,
        travelMode: google.maps.TravelMode.WALKING,
        unitSystem: google.maps.UnitSystem.IMPERIAL
    }
    
    //Pass the request to the route method
    directionsService.route(request,(result,status) => {
        if(status == google.maps.DirectionStatus.OK){
            //get distance and time
            const output = document.querySelector('#output');
            output.innerHTML = "<div class = 'alert-info'> From: "+ document.getElementById("from").value + " .<br />To: " + document.getElementById("To").value + ".<br /> Walking distance <i class='fa-solid fa-person-walking-with-cane'></i>:" +  result.routes[0].legs[0].distance.text + ".<br />Duration : " + result.routes[0].legs[0].duration.text + ".  </div>";
       
         
            //display route
            directionsDisplay.setDirection(result);

       
       
        }
        else{
            //delete route from map
            directionsDisplay.setDirections({routes: []});

            //centered map of bhopal
            map.setCenter(mylatlng);

            //show error incase showing route is not possible
            outerHeight.innerHTML = "<div class = 'alert-danger'> Could not Retrieve the walking distance "; 
        }


    });

}

// create autocomplete objects for all input

var options = {
    types: ['(cities)']
}

var input1 = document.getElementById("From");
var autocomplete1 = new google.maps.places.Autocomplete(input1, options)

var input2 = document.getElementById("To");
var autocomplete1 = new google.maps.places.Autocomplete(input2, options)
