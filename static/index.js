(function updateQuote() {
    $.ajax({
        url: $SCRIPT_ROOT + '/latest-quote',
        success: function(data) {
            console.log(data);
            $('#jordan').text(data.latest_quote);
        },
        complete: function() {
            setTimeout(updateQuote, 10000);
        }
    });
})();
