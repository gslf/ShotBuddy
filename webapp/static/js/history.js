// LOAD DATA
$(document).ready(function(){

    $.post('/API/history', {}, 
        function(data, status, xhr) {
            
            // Add sessions data to the table
            sessions = data.data.sessions
            sessions.forEach(function (item, index) {

                $('#result_table tr:last').after('<tr>'+
                                                    '<td>'+ item.data + '</td>'+
                                                    '<td> # '+ item.shots + '</td>'+
                                                    '<td>'+ item.score + '</td>'+
                                                    '<td>'+ parseFloat(item.percentage).toFixed(2) + '</td>'+
                                                    // TODO Link to element editing
                                                    '<td> <i class="fas fa-edit"></i> </td>'+
                                                '</tr>');
                console.log(item, index);
            });

            //console.log(data)
        })
        .fail(function(jqxhr, settings, ex) { 
            alert(LOADING_ERROR + ex); 
        });

});