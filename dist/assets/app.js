$('#submit').click(function(e){
    e.preventDefault();
    var register = $('#register').serialize();
    debugger;
    $.post('https://quiet-river-50753.herokuapp.com/register/', {register: register}, function(data){
      // $('#registerSuccess').html(data);
      debugger;
    });
});
