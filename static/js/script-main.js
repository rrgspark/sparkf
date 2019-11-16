var creacion = true, datos = {};

$(document).ready(function(){
    console.log(loggedin)
    if(loggedin=='False'){
        location.replace("login");
    }
    if(localStorage.getItem("toast"))
    {
        VanillaToasts.create({
            text:localStorage.getItem("toast"),
            type:'success',
            timeout: 2000
        });
        localStorage.clear();
    }
    $('#id_descripcion').on("keyup",function(e){
        if (event.keyCode === 13) {
            $('#boton-reg').focus();
            $('#boton-reg').click();
        }
    });

});
$('#modalRegistro').on('show.bs.modal', function () {
        if (creacion){
            $('#titulo-reg').text('Nueva tarea');
            $('#id_completado').prop('checked',false);
            $('#id_descripcion').val('');
            $('#boton-reg').text('Guardar');
        }
        else{
            $('#titulo-reg').text('Editar tarea');
            $('#item_id').val(datos.itemId);
            $('#id_descripcion').val(datos.desc);
            $('#id_completado').prop('checked',datos.completado);
            $('#boton-reg').text('Aceptar');
        }
    }
)
$('#modalRegistro').on('shown.bs.modal', function () {
        $('#id_descripcion').trigger('focus');
    }
)

function click_crear(){
    creacion=true;
}

function click_editar(descripcion, itemId, completado){
    datos.completado = completado;
    datos.itemId = itemId;
    datos.desc = descripcion;
    creacion=false;
}

function validarDescripcion(campo){
    if($("#id_descripcion").val()){
        $("#id_descripcion").removeClass("invalid-field");
    }else{
        $("#id_descripcion").addClass("invalid-field");
    }
}

function tareas(){
    try {
        if($('#id_descripcion').val()){
            var datos = {
                item_id: $('#item_id').val(),
                descripcion: $('#id_descripcion').val(),
                completado: $('#id_completado').prop('checked') ? 'True' : 'False',
                csrfmiddlewaretoken: token
            };
            $.post(creacion ? "registrar_item":"actualizar_item", datos ,function(data){        
                localStorage.setItem("toast", creacion ? 'Tarea registrada con éxito':'El registro se actualizó con éxito')
                location.reload();
            });
        }
    } catch (error) {
        console.log(error);
    }
}

function actualizar_checkbox(descripcion, itemId){
    try {
        var datos = {
            completado: $('#id_compl_lista'+itemId).prop('checked') ? 'True' : 'False',
            item_id: itemId,
            descripcion: descripcion,
            csrfmiddlewaretoken: token
        };   
        $.post("actualizar_item", datos ,function(data){        
            localStorage.setItem("toast",'El registro se actualizó con éxito')
            location.reload();
        });   
    } catch (error) {
        console.log(error);
    }
}

function borrar_registro(item_id){
    try {
        $.get('delete_item/'+item_id, function(){        
            localStorage.setItem("toast",'El registro se borró con éxito')
            location.reload();
        });   
    } catch (error) {
        console.log(error);
    }
}