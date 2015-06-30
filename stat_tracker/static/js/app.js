var app = {

  show: function (templateId, model) {
  var templateHtml = $('#' + templateId).html();
  var templateFn = _.template(templateHtml, { variable: 'm' });
  var result = templateFn(model);

  $('.main-content').html(result);
  },
  
  // $(".date").pickadate({
  //                 format: "mm/dd/yyyy"
  //           }),

  goto: function (url) {
  Backbone.history.navigate(url, { trigger: true });
  }

};
