$(function () {
   $('#calendar').fullCalendar({
   header: {
       left:'title',
   },
       navLinks:true,
       editable:false,
       eventLimit:true,
       events: function (start, end, timezone, callback) {

        $.ajax({
          url: 'events/',
          type: 'POST',
          dataType: 'json',
          success: function (x) {
              console.log(x)
          }
        });
       }
   });
});