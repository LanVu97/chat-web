$(document).ready(function(){
    // $('.sidenav').sidenav();
		$(".dropdown-trigger").dropdown({
			constrainWidth: false,
			coverTrigger: false
		});

		$('#alert_close').click(function(){
			$("#alert_box").fadeOut("slow", function() {
			});
		  });
  })