app.router.route('activities/:id/edit', function () {
  console.log("Activity Edit Page");

  app.show('activity-edit');

  $(".date").pickadate({
    format: "mm/dd/yyyy"
  });
});
