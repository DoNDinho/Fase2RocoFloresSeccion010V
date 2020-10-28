$(document).ready(function () {
    /*=============================================
    GALERIA DE IMAGENES FANCY BOX
    =============================================*/
    // Opciones fancybox
    $().fancybox({
        buttons: ['slideShow', 'share', 'zoom', 'fullScreen', 'close'],
        selector: '.imglist a:visible',
        loop: true,
        slideShow: {
            autoStart: true,
            speed: 3000
        }
    });
});
