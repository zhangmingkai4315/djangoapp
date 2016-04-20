$('#search_form').submit(function(e){
	// debugger
	$.post('/search/',$(this).serialize(),function(data){
		$('.tweets').html(data);
	});
	// debugger
	e.preventDefault();;
});

function search_submit(){
	var query = $("#id_query").val();
	$('#search-result').load('/search/?AJAX&query='+encodeURIComponent(query));
	return false;
}