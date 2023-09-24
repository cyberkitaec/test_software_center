$(function() {
        $(document).on('click touchstart', '.agree', function(){
            var id_event = $(this)[0]
            console.log("insert user to " + id_event)
            $.ajax({
            url: 'events/user/insert/' + id_event.value,
            type: 'GET',
            datatype: 'json',
            success: function(data) {
                    console.log("user insert to event")
            }
        });
    });
});

$(function() {
        $(document).on('click touchstart', '.refuse', function(){
            var id_event = $(this)[0]
            console.log("remove user from " + id_event)
            $.ajax({
            url: 'events/user/remove/' + id_event.value,
            type: 'GET',
            datatype: 'json',
            success: function(data) {
                    console.log("user remove from event")
            }
        });
    });
});

$(function() {
        $(document).on('click touchstart', '.delete', function(){
            var id_event = $(this)[0]
            console.log("delete" + id_event)
            $.ajax({
            url: 'events/user/delete/' + id_event.value,
            type: 'DELETE',
            datatype: 'json',
            success: function(data) {
                    console.log("event deleted")
            }
        });
    });
});