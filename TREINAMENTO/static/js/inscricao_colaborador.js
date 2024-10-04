$(document).ready(function () {
    // Função para carregar colaboradores
    function loadColaboradores() {
        var filial_name = $('#filial-select').val();
        
        if (filial_name && filial_name !== "") {
            $.ajax({
                url: "/inscricao/get_colaboradores",
                type: 'GET',
                data: { filial: filial_name },
                success: function (data) {
                    $('#colaborador-select').html(data).prop('disabled', false);
                },
                error: function () {
                    alert("Erro ao carregar colaboradores.");
                }
            });
        } else {
            $('#colaborador-select').prop('disabled', true).html('<option value="">Selecione um colaborador</option>');
        }
    }

    // Executa a função ao carregar a página
    loadColaboradores();

    // Chama a função quando o campo de filial muda
    $('#filial-select').change(function () {
        loadColaboradores();
    });
});
