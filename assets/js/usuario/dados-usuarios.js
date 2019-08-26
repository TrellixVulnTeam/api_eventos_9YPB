$(function ($) {
   animacaoAlertAlteracaoDadosUsuario();
   animacaoAlertCadastroUsuario();
   $('#spinner').toggle();
   bloquear_formulario_dados_pessoais();
   somenteNumeros();
   consultaCep();


});

function animacaoAlertAlteracaoDadosUsuario() {
     $("#alert").fadeTo(2000, 500).slideUp().slideUp(500, function () {
        $('.alert-success').slideUp(4500);
    })
}

function animacaoAlertCadastroUsuario() {
    $("#cadastro").fadeTo(2000, 500).slideUp().slideUp(500, function () {
        $('#cadastro').slideUp(6000)
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

function somenteNumeros() {
     $('#inputCEP').on( 'keydown', function(e) {
        var keyCode = e.keyCode || e.which,
          pattern = /\d/,
          // Permite somente Backspace, Delete e as setas direita e esquerda, números do teclado numérico - 96 a 105 - (além dos números)
          keys = [ 46, 8, 9, 37, 39, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105 ];

        if( ! pattern.test( String.fromCharCode( keyCode ) ) && $.inArray( keyCode, keys ) === -1 ) {
          return false;
        }
      });
}

function bloquear_formulario_dados_pessoais(){
    formulario.on('submit', function (e) {

        //stop submitting the form to see the disabled button effect
        //e.preventDefault();

        //disable the submit button
        // $("#spinner").toggle();
        // $("#salvar-alteracoes").attr("disabled", true);

        //disable formulario
        // $("#inputNome").attr("disabled", true);
        // $("#inputCracha").attr("disabled", true);
        // $("#inputCPF").attr("disabled", true);
        // $("#inputEmail4").attr("disabled", true);
        // $("#inputPass").attr("disabled", true);
        // $("#inputGenero").attr("disabled", true);
        //
        // $("#inputCEP").attr("disabled", true);
        // $("#inputLogradouro").attr("disabled", true);
        // $("#inputBairro").attr("disabled", true);
        // $("#inputCidade").attr("disabled", true);
        // $("#inputState").attr("disabled", true);
        // $("#inputPais").attr("disabled", true);

        setInterval(function() {
              e.preventDefault();

              $("#spinner").toggle();
              $("#inputNome").attr("disabled", true);



            }, 1000);

                });
}




