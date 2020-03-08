$(document).ready(function() {

    $("#wishes tbody tr").click(function() {
        const self = $(this);
        const wish_id = parseInt(self.attr('data-wish-id'));
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

    $("#image-selector").change(function () {
        const file_node = $("#image-selector");
        const file_path = file_node.val();
        const file_name = file_path.replace("C:\\fakepath\\", "");
        $("#selected-image-label").text(file_name)
    });

});