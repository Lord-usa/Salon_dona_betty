function enviar(formName) {
    //Obtención de la información del formulario
    let nombres = document.getElementById("txt-nombres").value;
    let apellidoPaterno = document.getElementById("txt-apellido-paterno").value;
    let apellidoMaterno = document.getElementById("txt-apellido-materno").value;
    let email = document.getElementById("txt-email").value;
    let telefono = document.getElementById("txt-telefono").value;
    let asunto = document.getElementById("txt-asunto").value;

    //Validaciones de campos
    let message = isEmpty(nombres, "NOMBRES");
    message = message + isMaxLength(nombres, "NOMBRES", 500);
    message = message + isEmpty(apellidoPaterno, "APELLIDO PATERNO");
    message = message + isMaxLength(apellidoPaterno, "APELLIDO PATERNO", 81);
    message = message + isEmpty(apellidoMaterno, "APELLIDO MATERNO");
    message = message + isMaxLength(apellidoMaterno, "APELLIDO MATERNO", 81);
    message = message + isEmpty(email, "EMAIL");
    message = message + isMaxLength(email, "EMAIL", 71);
    message = message + validateEmail(email,"EMAIL");
    message = message + isEmpty(telefono, "TELÉFONO");
    message = message + isMaxLength(telefono, "TELÉFONO", 12);
    message = message + validatePhone(telefono,"TELÉFONO");
    message = message + isEmpty(asunto, "ASUNTO");
    message = message + isMaxLength(asunto, "ASUNTO", 501);

    if (message.length > 0) {
        alert("ERROR: \n" + message);
    } else {
        document.getElementById(formName).submit();
    }
}

function limpiar() {
    
    console.log("EJECUTANDO MÉTODO LIMPIAR.");
    //Validar si los campos existen (undefined o null)
    editElementText("txt-nombres", "");
    editElementText("txt-apellido-paterno", "");
    editElementText("txt-apellido-materno", "");
    editElementText("txt-email", "");
    editElementText("txt-telefono", "");
    editElementText("txt-asunto", "");
    
    console.log("FINALIZANDO MÉTODO LIMPIAR.");
}
    
function editElementText(elementName, value) {

    let element = document.getElementById(elementName);
    
    if (element != null) {
        element.value = value;
    } else {
        console.warn("El elemento " + elementName + " no se encuentra en el documento HTML");
    }
}

function validatePhone(phone, name) {
    let value = phone
    if (/^([0-9])*$/g.test(value)) {
        return "";
    } else {
        return "El campo " + name + " debe ser númerico.";
    }
}
    
function validateEmail(email, name) {
    
    let value = email
    if (/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i.test(value)) {
        return "";
    } else {
        return "El campo " + name + " no es un correo electrónico válido\n";
    }
}


