$(document).ready(function(){
    setInterval(function() {
        $.ajax({
            url: 'update/all_events',
            type: 'GET',
            datatype: 'json',
            success: function(data) {
                // assuming data is a JSON object with 'value' property
                $('.events_a').empty();
                $.each(data, function(index, element){
                    $('.events_a').append('<li class="li_event" value="' + element.id +'">' + '<a href="#">' + element.title + "</a>"+ '</li>')
                })
            }
        });
    }, 30000);  // make request every second
});