// script.js
$(document).ready(function() {
    $('#searchButton').click(function() {
        var startDate = $('#startDate').val();
        var endDate = $('#endDate').val();
        $.ajax({
            type: 'POST',
            url: '/search_customers',
            data: { start_date: startDate, end_date: endDate },
            success: function(data) {
                $('#searchResults').empty();
                $.each(data, function(index, row) {
                    $('#searchResults').append('<div>' + row + '</div>');
                });
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });
});
