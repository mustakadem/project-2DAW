
$(function () {
   $("#search-reservate").on("click",function (e) {
       e.preventDefault();
       search();
   })
});

function search() {
$.ajax({
    url: 'http://127.0.0.1:8000/home/form/reservate/',
    type: 'GET',
    success: function(data) {
        $("#reservate").html(data)
    },
    failure: function(data) {
        alert('Got an error dude');
    }
});
}