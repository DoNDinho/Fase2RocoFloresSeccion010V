$(document).ready(function () {
    /*=============================================
    ARTICULOS Y CARRITO DE COMPRAS LOCALSTORAGE
    =============================================*/
    // Invoca funcion para cargar los items de local storage en carrito
    cargarCarrito();

    $('.btn-articulo').click(guardarLocalStorage);
    $('.carrito-cantidad').bind('keyup input', modificarCantidad);
    $('.carrito-eliminar').on('click', eliminarArticulo);
    $('.botonPagar').click(pagar);

    // Funcion para guardar datos en localStorage
    function guardarLocalStorage(evt) {
        // Selecciona el div que contiene la clase .item
        let item = evt.target.closest('.item');
        let id = item.querySelector('.item-id').getAttribute('value');
        let nombre = item.querySelector('.item-nombre').getAttribute('value');
        let precio = item.querySelector('.item-precio').getAttribute('value');
        let imagen = item.querySelector('.item-imagen').src;
        let cantidad = 1;

        // Crea objeto con articulos
        let articulo = {
            id,
            nombre,
            precio,
            imagen,
            cantidad
        };

        // Si no existen articulos en local storage
        if (localStorage.getItem('articulos') === null) {
            let articulos = []; // Crea un arreglo
            articulos.push(articulo); // Inserta objeto en arreglo creado
            localStorage.setItem('articulos', JSON.stringify(articulos)); // Setea arreglo en localStorage
        } else {
            let articulos = JSON.parse(localStorage.getItem('articulos'));
            let existe = false;

            // Valida si el articulo ya esta agregado
            for (let i = 0; i < articulos.length; i++) {
                if (articulos[i].nombre === nombre) {
                    cantidad = articulos[i].cantidad++;
                    existe = true;
                    break;
                }
            }

            // Si no existe el articulo, lo agrega a la lista
            if (!existe) {
                articulos.push(articulo);
            }

            localStorage.setItem('articulos', JSON.stringify(articulos));
        }

        cargarCarrito();
    }

    // Funcion para cargar datos en tabla de carrito de compras
    function cargarCarrito() {
        if (localStorage.getItem('articulos') === null) {
            $('.alerta-carrito').remove();
        } else {
            let articulos = JSON.parse(localStorage.getItem('articulos'));

            if (articulos.length != 0) {
                let columnas = '';

                articulos.forEach((i) => {
                    let nombre = i.nombre;
                    let precio = i.precio;
                    let imagen = i.imagen;
                    let cantidad = i.cantidad;

                    let articulos = `<tr class="carrito-columna">
                        <td scope="row"> 
                            <img class="carrito-imagen carrito-nombre" src="${imagen}" value="${nombre}" alt="">${nombre}
                        </td>
                        <td class="carrito-precio" value="${precio}">$${precio}</td>
                        <td> <input class="carrito-cantidad" type="number"  min="1" value="${cantidad}"></td>
                        <td><button class="btn btn-danger carrito-eliminar"><i class="fas fa-trash-alt"></i></button> </td>
                    </tr>`;

                    columnas += articulos;
                });

                columnas += `
                <td></td>
                <td></td>
                <td></td>
                <td>
                    <button class="btn btn-primary botonPagar"><i class="fas fa-dollar-sign"></i>Pagar</button>
                </td> `;

                $('#tablaCarrito').html(columnas);
                $('#alerta-carrito').html('<div class="alerta-carrito"></div>');
            }
        }
    }

    // Funcion para aumentar o disminuir cantidad de articulo.
    function modificarCantidad(evt) {
        let item = evt.target.closest('.carrito-columna');
        let nombre = item.querySelector('.carrito-nombre').getAttribute('value');
        let cantidad = item.querySelector('.carrito-cantidad').value;

        let articulos = JSON.parse(localStorage.getItem('articulos'));

        // Valida si el articulo ya esta agregado
        for (let i = 0; i < articulos.length; i++) {
            if (articulos[i].nombre === nombre) {
                articulos[i].cantidad = cantidad;
                break;
            }
        }

        localStorage.setItem('articulos', JSON.stringify(articulos));
    }

    // Funcion para eliminar articulo de local storage
    function eliminarArticulo(evt) {
        let item = evt.target.closest('.carrito-columna');
        let nombre = item.querySelector('.carrito-nombre').getAttribute('value');

        let articulos = JSON.parse(localStorage.getItem('articulos'));

        // Valida si el articulo ya esta agregado
        for (let i = 0; i < articulos.length; i++) {
            if (articulos[i].nombre === nombre) {
                articulos.splice(i, 1); // funcion para eliminar item de arreglo
                $('.alerta-carrito').remove();
                break;
            }
        }

        localStorage.setItem('articulos', JSON.stringify(articulos));

        cargarCarrito();
        location.reload();
    }
    function pagar(evt) {
        if (localStorage.getItem('articulos') === null) {
            $('.alerta-carrito').remove();
        } else {
            let articulos = JSON.parse(localStorage.getItem('articulos'));
            $('#pagar').html('');

            $.ajax({
                url: '/register/',
                type: 'POST',
                data: {
                    articulos: JSON.stringify(articulos)
                },
                processData: false,
                contentType: false,
                success: (response) => {
                    console.log('Respuesta');
                    console.log(response);
                }
            });

            /////////////////////////////////////////////////////////////////

            // let total = 0;
            // let listaComprobante = '';
            // let listaconcar = '';

            // articulos.forEach((i) => {
            //     let nombre = i.nombre;
            //     let precio = i.precio;
            //     let cantidad = i.cantidad;

            //     listaComprobante += `<li id="listaComprobante" style="display:inline-block"> <span id ="textnombre"><B>Nombre:</B></span> <span id="Lnombre" >${nombre}</span> <span id="Nprecio">Precio$</span> <mark>${precio}</mark> <span id="textcantidad">Cantidad:</span>${cantidad}</li>`;
            //     listaconcar = listaconcar.concat(articulos.nombre + articulos.precio + articulos.cantidad);

            //     total += precio * cantidad;
            // });

            // let comprobante = `<div class="panel panel-default">
            //     <div class="row boleta >
            //         <main class="col-sm-8 row " ></main>
            //         <div  class= "col-sm-4" >
            //             <h2 id=tcomprobante >Comprobante</h2>
            //             <ul id="comprobante" class="list-group ">
            //             </ul>
            //             <hr>
            //             <p id="ptotal" class="text-left">Total: $ <span id="toli" >${total} </span></p>
            //         </div>
            //         <button id="botonvolver" class="btn btn-primary"><a id="refvoler" href="index.html">Volver</a></button>
            //     </div>
            // </div>
            // `;

            // $('refvolver').click(localStorage.clear());
            // $('#pagar').html(comprobante);
            // $('#comprobante').html(listaComprobante);
        }
    }

    /*=============================================
    VALIDACION FORMULARIO
    =============================================*/
    // Valida si los password son iguales cuando hay un cambio de focus
    $('#registroPasswordValidar').blur(function () {
        let password = $('#registroPassword').val();
        let passwordValidar = $('#registroPasswordValidar').val();

        if (password != passwordValidar) {
            $('.alert').remove();
            $('.registroPasswordValidar').before("<div class='alert alert-danger alert-dismissible'><button type='button' class='close' data-dismiss='alert'>&times;</button><strong>Error!</strong> Debe ingresar misma contraseña</div>");
        }
    });

    $('#formularioRegistro').submit(function () {
        let nombre = $('#registroNombre').val();
        let email = $('#registroEmail').val();
        let telefono = $('#registroTelefono').val();
        let edad = $('#registroEdad').val();
        let password = $('#registroPassword').val();
        let passwordValidar = $('#registroPasswordValidar').val();
        let terminos = $('#registroTerminos').prop('checked');

        // El nombre permite solo letras
        if (nombre != '') {
            let pattern = new RegExp('^[a-zA-ZáéíóúàèìòùÀÈÌÒÙÁÉÍÓÚñÑüÜ_s]+$');

            if (!nombre.match(pattern)) {
                $('.alert').remove();
                $('.registroNombre').before("<div class='alert alert-danger alert-dismissible'><button type='button' class='close' data-dismiss='alert'>&times;</button><strong>Error!</strong> Debe ingresar solo letras</div>");
                return false;
            }
        }

        // Password debe tener entre 8 y 10 caracteres, por lo menos un digito y un alfanumérico, y no puede contener caracteres espaciales
        if (password != '') {
            let pattern = new RegExp('(?!^[0-9]*$)(?!^[a-zA-Z]*$)^([a-zA-Z0-9]{8,10})$');

            if (!password.match(pattern)) {
                $('.alert').remove();
                $('.registroPassword').before(
                    "<div class='alert alert-danger alert-dismissible'><button type='button' class='close' data-dismiss='alert'>&times;</button><strong>Error!</strong> Entre 8 y 10 caracteres, por lo menos un digito y un alfanumérico, y no puede contener caracteres espaciales</div>"
                );
                return false;
            }
        }

        // Valida que el password sea el mismo password ingresado
        if (passwordValidar != '') {
            if (password != passwordValidar) {
                $('.alert').remove();
                $('.registroPasswordValidar').before("<div class='alert alert-danger alert-dismissible'><button type='button' class='close' data-dismiss='alert'>&times;</button><strong>Error!</strong> Debe ingresar misma contraseña</div>");
                return false;
            }
        }

        // Valida formato de telefono
        if (telefono != '') {
            let pattern = new RegExp('^[0-9]{2,3}-? ?[0-9]{6,7}$');

            if (!telefono.match(pattern)) {
                $('.alert').remove();
                $('.registroTelefono').before("<div class='alert alert-danger alert-dismissible'><button type='button' class='close' data-dismiss='alert'>&times;</button><strong>Error!</strong> Debe ingresar formato de teléfono válido</div>");
                return false;
            }
        }

        // Valida solo numeros
        if (edad != '') {
            let pattern = new RegExp('^([0-9])*$');

            if (!edad.match(pattern)) {
                $('.alert').remove();
                $('.registroEdad').before("<div class='alert alert-danger alert-dismissible'><button type='button' class='close' data-dismiss='alert'>&times;</button><strong>Error!</strong> Debe ingresar solo números</div>");
                return false;
            }
        }

        // Valida que el checkbox de terminos esté checkeado
        if (!terminos) {
            alert('Debe haceptar términos y condiciones');
            return false;
        } else {
            return true;
        }
    });
});
