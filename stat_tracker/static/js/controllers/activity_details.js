app.router.route('activities/:id', function (id) {
  console.log("Activity Details Page");

  $.ajax({
    url: '/api/activities/' + id,
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      console.log(data);
      app.show('activity-details', data);
      svgGraph(id);
    }
  });

});
