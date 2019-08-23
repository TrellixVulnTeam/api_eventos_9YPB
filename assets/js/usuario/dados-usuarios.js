jQuery(function ($) {
    // $("#alert-success").fadeTo(2000, 500).slideUp(500, function () {
    //     $("#success-alert").slideUp(500);
    // });

    $("#alert").fadeTo(2000, 500).slideUp().slideUp(500, function () {
        $('.alert-success').slideUp(4000);
    })
});