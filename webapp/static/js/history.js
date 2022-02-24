// MODAL MANAGEMENT
const modal = document.querySelector(".modal");
const closeButton = document.querySelector(".close-button");

function toggleModal(id_session, data, shots) {
    $("#id_session").html(id_session)

    $("#edit_date").val(data)
    $("#edit_shots").val(shots)
    modal.classList.toggle("show-modal");
    $("#modal_edit").show();
    $("#modal_text").hide();
}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

closeButton.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);

// LOAD DATA
$(document).ready(function(){

    // DATA LOADING
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
                                                    '<td> <i onclick="toggleModal(' + item.id + ',\'' + item.data + '\',\'' + item.shot_list + '\')" class="fas fa-edit"></i> &nbsp;&nbsp;'+
                                                    '<i onclick="deletesession(' + item.id + ')" class="fas fa-trash"></i> </td>'+
                                                '</tr>');
            });

            //console.log(data)
        })
        .fail(function(jqxhr, settings, ex) { 
            alert(LOADING_ERROR + ex); 
        });

});

function editing(){
    // Show waiting modal
    $("#modal_edit").hide();
    $("#modal_text").show();
    $("#modal_text_content").html("WAIT . . .")

    // API REQUEST
    $.post('/API/historyedit', {"id_session": $("#id_session").html(), 
                                "date": $("#edit_date").val(),
                                "shots": $("#edit_shots").val()}, 
        function(data, status, xhr) {

            // Reload page if editing succeeded or show error
            if (data["status"]){
                modal.classList.toggle("show-modal");
                location.reload();
            }else{
                modal.classList.toggle("show-modal");
                alert("DATA ERROR, TRY AGAIN."); 
            }
            
            //console.log(data)
        })

        // Show error for failed request
        .fail(function(jqxhr, settings, ex) { 
            modal.classList.toggle("show-modal");
            alert(LOADING_ERROR + ex); 
        });
};

function deletesession(id_session){

    modal.classList.toggle("show-modal");
    $("#modal_edit").hide();
    $("#modal_text").show();

    // API REQUEST
    $.post('/API/historydelete', {"id_session": id_session}, 
    function(data, status, xhr) {

        // Reload page if editing succeeded or show error
        if (data["status"]){
            modal.classList.toggle("show-modal");
            location.reload();
        }else{
            modal.classList.toggle("show-modal");
            alert(LOADING_ERROR); 
        }

    //console.log(data)
    })

    // Show error for failed request
    .fail(function(jqxhr, settings, ex) { 
        modal.classList.toggle("show-modal");
        alert(LOADING_ERROR + ex); 
    });
}