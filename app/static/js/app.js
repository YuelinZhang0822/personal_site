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
        const preview = $("#image-preview");
        $("#selected-image-label").text(file_name);

        const file = file_node.prop('files')[0];
        const fileReader = new FileReader();
        fileReader.onload = function () {
            // convert image file to base64 stringc

            const uploaded_data = fileReader.result;
            preview.attr("src", uploaded_data);
        };
        fileReader.readAsDataURL(file)
    });

    $("#image-selector-addon").click(function () {
       const uploaded_data = $("#image-preview").attr('src');
       const data = JSON.stringify({'image_base64': uploaded_data});
       $.ajax({
           url: 'image/add',
           type: 'POST',
           dataType: 'json',
           data: data,
           contentType: 'application/json',
           success: function () {
               alert("upload image successfully!")
           },
           error: function () {
               alert("failed")
           }
       });

    });

});