$(function() {
            $(document).on('click touchstart', '.li_event', function() {
                    $('.li_event').click(function(e) {
                            var li_value = $(this)[0]
                            user_id = localStorage.getItem("user_id");
                            var FLAG = false;
                            $.ajax({
                                    method: "GET",
                                    url: "update/event/" + li_value.value,
                                    dataType: "json",
                                    success: function(data) {
                                        console.log(data.title)
                                        $(".name_event").html("<h2>" + data.title + "</h2>")
                                        $(".desc_event").html("<h3>" + data.desc + "</h2>")
                                        $(".date_of_event").html("<h3>" + data.date_of_create + "</h2>")
                                        $(".participants").html('<ul class="party"> <h2> Участники: </h2> </ul>')
                                        console.log(data.creator)
                                        if (data.creator == user_id) {
                                            $(".buttons").append("<button class='delete' value='" + data.id + "'>" + "Удалить событие </button>")
                                        }
                                        $.each(data.participants, function(index, element) {
                                            console.log(element.id)
                                            if (element.id == user_id) {
                                                FLAG = true;
                                            }
                                            $(".party").append('<li class="users" value="' + element.id + '">' + '<a href="#">' + element.name + " " + element.surname + "</a>" + '</li>')
                                        })
                                        if (FLAG) {
                                            $(".buttons").append("<button class='refuse' value='" + data.id + "'>" + "Отказаться от участия </button>")
                                        } else {
                                            $(".buttons").append("<button class='agree' value='" + data.id + "'>" + "Принять участие</button>")
                                        }
                                    },
                                    error: function(er) {
                                        console.log(er);
                                    },
                                    complete: function(){
                                        setInterval(function(){
                                            $.ajax({
                                                method: "GET",
                                                url: "update/event/" + li_value.value,
                                                dataType: "json",
                                                success: function(data){
                                                $(".participants").html('<ul class="party"> <h2> Участники: </h2> </ul>')
                                                $(".users").empty();
                                                    $.each(data.participants, function(index, element){
                                                        $(".party").append('<li class="users" value="' + element.id + '">' + '<a href="#">' + element.name + " " + element.surname + "</a>" + '</li>')
                                                    })
                                                }
                                            })
                                        }, 3000)
                                    }

                                    });
                            });
                    })
            });