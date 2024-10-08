$(document).ready(function () {
    // Quando a filial é selecionada, buscar as empresas associadas
    $('#filial-select').change(function () {
        var filial_name = $(this).val();

        if (filial_name && filial_name !== "") {
            // Realiza a chamada AJAX para buscar as empresas associadas
            $.ajax({
                url: "/colaborador/get_empresas", 
                type: 'GET',
                data: { filial: filial_name }, 
                success: function (data) {
                    // Atualiza o dropdown de empresas com as opções retornadas
                    $('#empresa-select').html(data).prop('disabled', false);
                },
                error: function () {
                    alert("Erro ao carregar empresas.");
                }
            });
        } else {
            $('#empresa-select').prop('disabled', true).html('<option value="">Selecione uma Empresa</option>');
        }
    });
});
