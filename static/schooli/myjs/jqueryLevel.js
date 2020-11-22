
   
  $("#evaluation").change(function () {
    var url = $("#searchForm").attr("data-levels-url");  // get the url of the `load_cities` view
    var EvaluationId = $(this).val();  // get the selected evaluation ID from the HTML input

    $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= /examen_et_concours/ajax/load-levels/ )
        data: {
            'evaluation': EvaluationId       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_levels` view function
            $("#level").html(data);  // replace the contents of the city input with the data that came from the server
          
        }
    });

});



