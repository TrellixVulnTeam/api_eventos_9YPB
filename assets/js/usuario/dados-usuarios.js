jQuery(function ($) {
    $("#alert").fadeTo(2000, 500).slideUp().slideUp(500, function () {
        $('.alert-success').slideUp(4000);
    })
});