
    $(function () {
        $('#calendar').fullCalendar({
            header: {left: 'title  month,'},
            navLinks: true,
            editable: false,    
            eventLimit: true,
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

            //     function (start, end, timezone, callback) {
            //
            //  $.ajax({
            //    url: 'home/events/',
            //    type: 'GET',
            //    dataType: 'json',
            //    success: function (data) {
            //          $.each(data, function (index, item) {
            //              start = item.date_entry;
            //              end = item.date_departure;
            //          });
            //    }
            //  });
            // }
        });
    });
