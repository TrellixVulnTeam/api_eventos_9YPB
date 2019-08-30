// $("#modalLogin").on('shown.bs.modal', function () {
//     $('#myInput').trigger('focus')
// });
//
// $('#modalLogin').click(function () {
//    $('#modalLogin').modal('show');
// });


// $("#documento_financeiro").on("click",function(e) {
//   e.preventDefault();
// // cross domain ajax call will fail, need more work to set up CORS
// //  $.get("http://textmechanic.com", function(data) {
// //    $("#myModal").html(data).foundation("open");
// //  });
//
//   $("#documento_financeiro")
//     .html()
//     .foundation("open");
//
// });
//
$('#documento_financeiro').on('show.bs.modal', function () {
    $('#documento_financeiro').trigger('focus');
});

$('#documento_financeiro').click(function () {
    $('#documento_financeiro').modal('show');
});