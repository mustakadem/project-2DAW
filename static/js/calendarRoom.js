$(function () {

let id_room = $("#valueRoom").val();

$("#calendar").fullCalendar({
    header: {left: 'month,'},
    height: 600,
    navLinks: true,
    editable: false,
    eventLimit: true,
    timeFormat: 'H:mm',
    events: function (start, end, timezone, callback) {

             $.ajax({
               url: 'http://127.0.0.1:8000/rooms/'+ id_room +'/',
               type: 'GET',
               dataType: 'json',
               success: function (data) {
                   let events = [];
                     $.each(data, function (index, item) {
                        if (index === 'bookings'){
                            for(let booking of item){
                                events.push({
                                   title: booking.title,
                                    start: booking.start,
                                    end: booking.end,
                                });
                            }
                        }
                     });
                     callback(events);
               }
             });
            }
});
});