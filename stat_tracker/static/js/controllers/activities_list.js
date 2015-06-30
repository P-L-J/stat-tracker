app.router.route('activities', function () {
  console.log("Activities Page");

  $.ajax({
    url: '/api/activities',
    method: 'GET',
    dataType: 'json',
    success: function(data) {
      console.log(data);
      app.show('activities-list', data);
    }
  });

  ;
});
