// Manejo de eventos

(function(){
    const linkEliminacion = document.querySelectorAll('.link-eliminacion');

    linkEliminacion.forEach(btn=>{
        btn.addEventListener('click', (e)=>{
        let confirmacion = confirm('¿Seguro quiere eliminar la indumentaria?');
            if (!confirmacion){
                e.preventDefault();
            }
        })
    })
})();

// Alert boostrap desvanececer

window.setTimeout(() => {
    $(".alert").fadeTo(1500, 0).slideDown(1000,()=> {
        $(this).remove();
    });;
}, 2000);