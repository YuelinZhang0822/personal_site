$(document).ready(function() {

    $("#wishes tbody tr").click(function() {
        var self = $(this);
        var wish_id = parseInt(self.attr('data-wish-id'));
        window.location = "/wish?id=3"
        // $.ajax({
        //     url: '/wish',
        //     type: 'GET',
        //     dataType: 'json',
        //     data: {
        //         "id": wish_id
        //     },
        //     success: function () {
        //         window.location = "/wish?id=3"
        //     },
        //     error: function () {
        //         alert("Redirect failed!")
        //     }
        // });
    });

    // $( "tr" ).on({
    //     "click": function() { alert( "clicked!" ); },
    //     "mouseover": function() { console.log( "hovered!" ); }
    // });

});