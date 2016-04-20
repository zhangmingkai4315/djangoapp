$('#search_form').submit(function(e){
	// debugger
	$.post('/search/',$(this).serialize(),function(data){
		$('.tweets').html(data);
	});
	// debugger
	e.preventDefault();;
})