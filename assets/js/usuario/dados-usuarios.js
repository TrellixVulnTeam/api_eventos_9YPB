$(function ($) {
   animacaoAlertAlteracaoDadosUsuario();
   //bloquear_formulario_dados_pessoais();
   consultaCep();


});

function animacaoAlertAlteracaoDadosUsuario() {
     $("#alert").fadeTo(2000, 500).slideUp().slideUp(500, function () {
        $('.alert-success').slideUp(4500);
    })
}

function consultaCep() {
    $("#inputCEP").blur(function() {
        var cep = $(this).val();
        $.getJSON("http://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {
            if (!("erro" in dados)) {
                limparCampos();
                $("#inputLogradouro").val(dados.logradouro);
                $("#inputBairro").val(dados.bairro);
                $("#inputCidade").val(dados.localidade);
                $("#inputState").val(dados.uf);

            }
        });
    });
}

function limparCampos() {
     $('#inputLogradouro').val("");
     $('#inputBairro').val("");
     $('#inputCidade').val("");
     $('#inputState').val("");

}









//
//
// var formulario = $("#form-dados-pessoais");

// function bloquear_formulario_dados_pessoais(){
//     formulario.on('submit', function (e) {
//
//         //stop submitting the form to see the disabled button effect
//         //e.preventDefault();
//
//         //disable the submit button
//         $("#salvar-alteracoes").attr("disabled", true);
//
//         //disable formulario
//         $("#inputNome").attr("disabled", true);
//         $("#inputCracha").attr("disabled", true);
//         $("#inputCPF").attr("disabled", true);
//         $("#inputEmail4").attr("disabled", true);
//         $("#inputPass").attr("disabled", true);
//         $("#inputGenero").attr("disabled", true);
//
//         $("#inputCEP").attr("disabled", true);
//         $("#inputLogradouro").attr("disabled", true);
//         $("#inputBairro").attr("disabled", true);
//         $("#inputCidade").attr("disabled", true);
//         $("#inputState").attr("disabled", true);
//         $("#inputPais").attr("disabled", true);
//
//     });
// }




