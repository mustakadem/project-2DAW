
    $(function () {
        $('#calendar').fullCalendar({
            header: {left: 'title  month,'},
            navLinks: true,
            editable: false,    
            eventLimit: true,
            selectable: true,
            events: 'http://127.0.0.1:8000/rooms/events/',
            eventClick: function (calEvent, jsEvent, view) {
                $("#titleEvent").text(calEvent.title);
                $("#dayEvent").text(moment(calEvent.start).format('dddd DD MMMM YYYY'));
                $("#startEvent").text(calEvent.start_time);
                $("#endEvent").text(calEvent.end_time);
                $("#buttonDeleteEvent").attr('href', '/rooms/'+calEvent.room+'/booking/'+calEvent.id+'/delete/' );
                $("#eventModal").modal('show');
            },
            timeFormat: 'H:mm',
            dayClick: function(date, jsEvent, view){
                $('#day_event').text(date.format());
                $("#addEventModal").modal('show');
            },
        });
        $('#addEvent').on('click' , function () {
            let title = $("#title").val();
            let room = $("#room").val();
            let user = $('#user').val();
            let start = $('#day_event').text();
            let start_time = $('#start_time').val();
            let end_time = $('#end_time').val();


            $.ajax({
                url: 'home/reservate/',
                headers: { "X-CSRFToken": $.cookie("csrftoken") },
                data: {'title':title,'room':room,'user':user,'start':start,'start_time': start_time,'end_time':end_time},
                type: 'POST',
                dataType: 'json',
                success: function (json) {
                    if (json.error){
                        $('#divMsgError').removeClass('alert-success');
                        $('#divMsgError').addClass('alert alert-danger');
                        $('#msgError').text(json.error);
                    }else {
                        $('#divMsgError').removeClass('alert-danger');
                        $('#divMsgError').addClass('alert alert-success');
                        $('#msgError').text(json.result);

                    }
                },
                error: function (error) {
                    console.log('error'+ error.data);
                }
            })

        })
    });
