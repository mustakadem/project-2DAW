$(function () {
   $('#calendar').fullCalendar({
   header: {
       left:'title',
   },
       navLinks:true,
       editable:false,
       eventLimit:true,
       events: 'http://127.0.0.1:8000/home/events/',
       eventClick:function (calEvent, jsEvent, view) {
           alert(calEvent.start);
       }
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