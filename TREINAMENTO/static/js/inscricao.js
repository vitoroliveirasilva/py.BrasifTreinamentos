$(document).ready(function () {
    // Quando o tipo é selecionado, buscar as marcas associadas
    $('#tipo-select').change(function () {
        // Obtém o valor selecionado do dropdown de tipos
        var tipo_id = $(this).val();
        
        // Verificar se o valor selecionado é válido (maior que 0)
        if (tipo_id > 0) {
            // Realiza uma chamada AJAX para buscar as marcas associadas ao tipo selecionado
            $.ajax({
                url: "/inscricao/get_marcas", // URL da rota para buscar marcas
                type: 'GET', // Método HTTP
                data: { tipo_id: tipo_id }, // Envia o tipo_id como parâmetro
                success: function (data) {
                    // Atualiza o dropdown de marcas com as opções retornadas
                    $('#marca-select').html(data).prop('disabled', false);
                    // Desabilita o dropdown de treinamentos até que uma marca seja selecionada
                    $('#treinamento-select').prop('disabled', true);
                }
            });
        } else {
            // Se um tipo inválido (ou nenhum) for selecionado, desabilita os dropdowns de marcas e treinamentos
            $('#marca-select').prop('disabled', true).html('<option value="">Selecione uma Marca</option>');
            $('#treinamento-select').prop('disabled', true).html('<option value="">Selecione um Treinamento</option>');
        }
    });

    // Quando a marca é selecionada, buscar os treinamentos associados
    $('#marca-select').change(function () {
        // Obtém o valor selecionado do dropdown de marcas
        var marca_id = $(this).val();
        // Verifica se uma marca foi selecionada
        if (marca_id) {
            // Realiza uma chamada AJAX para buscar os treinamentos associados à marca selecionada
            $.ajax({
                url: "/inscricao/get_treinamentos", // URL da rota para buscar treinamentos
                type: 'GET', // Método HTTP
                data: { marca_id: marca_id }, // Envia o marca_id como parâmetro
                success: function (data) {
                    // Atualiza o dropdown de treinamentos com as opções retornadas
                    $('#treinamento-select').html(data).prop('disabled', false);
                }
            });
        } else {
            // Se nenhuma marca for selecionada, desabilita o dropdown de treinamentos
            $('#treinamento-select').prop('disabled', true).html('<option value="">Selecione um Treinamento</option>');
        }
    });
});
