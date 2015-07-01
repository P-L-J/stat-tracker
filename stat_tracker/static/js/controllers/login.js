(function() {

  app.router.route('', loginController);

  app.router.route('login', loginController);

  function loginController() {

    app.show('login');

    $(".login-button").on('click', function() {
      app.goto('activities');
    });

    $(".register-button").on('click', function() {
      app.goto('registration');
    });
  }

})();
