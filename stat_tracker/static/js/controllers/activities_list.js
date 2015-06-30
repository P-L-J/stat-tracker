app.router.route('activities', function () {

  $.ajax({
    url: '/api/activities/',
    method: 'GET',
    dataType: 'json'
  }).done(renderData);

  function renderData(data) {
    console.log(data);
    app.show('activities-list', data);

    bindEvents();
  }

  function bindEvents() {
    $(".new-activity-form").submit(function() {
      var titleHash = {};
      titleHash.title = $(".activity").val();
      console.log(titleHash);

      $.ajax({
        url: '/api/activities/',
        method: 'POST',
        data: titleHash
      });

    });
  }

});
