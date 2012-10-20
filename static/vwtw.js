/* get templates */
$(document).ready(function(){
    $.getJSON('/cities', function (cities) {
        for(i in cities)
        {
            var target = $('<div/>').attr("id",cities[i]);
            cityWeather(cities[i], target);
            $('#main').append("<h2>"+cities[i]+"</h2>");
            $('#main').append(target);
        }
    });
    cityWeather();
});

function cityWeather(place, target)
{
    $.ajax({
        url: "http://api.aerisapi.com/observations/"+place+"?client_id=LxII2WnN9RhFt5Pd7ArOA&client_secret=R5xZ8qJ9bMFuDEbWfLcHlKACnD2AJ9dBGntpKnyQ",
        dataType: "jsonp",
        success: function(json) {
            if (json.success == true) {
                var ob = json.response.ob;
                target.html(ich.weatherTemplate(ob));
            }    
            else {
                console.log(json.error.description);
            }
        }
    });
}
