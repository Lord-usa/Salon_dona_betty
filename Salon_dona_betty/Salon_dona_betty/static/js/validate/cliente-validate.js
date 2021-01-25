function eliminar_contacto(id) {
    console.log("id: " + id)
    window.location.assign('/eliminar-contacto?id=' + id)
}

function editar_contacto(id) {
    console.log("id: " + id)
    window.location.assign('/form-editar-contacto?id=' + id)
}