$("#modalLogin").on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
});

$('#modalLogin').click(function () {
   $('#modalLogin').modal('show');
});


// $("modal-financiero-evento.html #modal_doc_financiero").on('shown.bs.modal', function () {
//     $('#myInput').trigger('focus')
// });

// $("modal-financiero-evento.html #modal_doc_financiero").load(function () {
//    $('#modal_doc_financiero').modal('show');
// });

