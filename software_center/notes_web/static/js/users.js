$(function() {
        $(document).on('click touchstart', '.users', function(){
            var id_event = $(this)[0]
            console.log("user " + id_event)
            $.ajax({
            url: 'users/data/' + id_event.value,
            type: 'GET',
            datatype: 'json',
            success: function(data) {
                $(".user_data").empty();
                $(".user_data").append("<p> Имя и фамилия: " + data.name + " " + data.surname + "<br>");
                $(".user_data").append("<p> Дата регистрации: " + data.date_of_registration + "<br>");
                if (data.date_of_birthday == null){
                    $(".user_data").append("<p> Дата рождения: не указан <br>");
                }else {
                    $(".user_data").append("<p> Дата рождения: " + data.date_of_birthday + "<br>");
                    }
            }
        });
    });
});