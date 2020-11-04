function confirmarEliminacion(id) {
    Swal.fire({
        title: '¿Está seguro?',
        text: 'No podra revertir esto',
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.value) {
            window.location.href = `/articulos/articulo/eliminar/${id}/`;
        }
    });
}
