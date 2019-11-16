$(document).ready(function(){
    $('#id_email').focus();
});

function spinner(){
    if($('#id_email').val())
        $('#spinner_id').prop('hidden',false);
}