app.router.route('', 'login', function () {
  console.log("Login Page");

  app.show('login');

  $(".login-button").on('click', function() {
    app.goto('activities');
  });

  $(".register-button").on('click', function() {
    app.goto('registration');
  });
});
