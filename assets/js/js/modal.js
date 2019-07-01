$("#modalLogin").on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
});

$('#modalLogin').click(function () {
   $('#modalLogin').modal('show');
});