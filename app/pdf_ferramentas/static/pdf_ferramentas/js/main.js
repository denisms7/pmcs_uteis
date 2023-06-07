document.addEventListener('DOMContentLoaded', function () {
    function ExibeCampos() {
        const formulario = document.getElementById('formulario');
        const aguarde = document.getElementById('aguarde');
        formulario.classList.add('d-none');
        aguarde.classList.remove('d-none');
        aguarde.classList.add('d-block');
    }

    ExibeCampos();
});



