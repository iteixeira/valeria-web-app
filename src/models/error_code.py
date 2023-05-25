from enum import Enum

def get_errors():
    return Enum(
        "CONTACT_ERROR",[
            ("SUCCESS", "Nenhum erro encontrado"),
            ("ERROR_MISSING", "Por favor preencha todos os campos."),
            ("ERROR_MAIL", "E-mail informado é invlálido")
        ] 
    )