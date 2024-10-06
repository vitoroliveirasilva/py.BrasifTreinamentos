# ========== FUNÇÕES GENÉRICAS ==========

# Função genérica para verificar se o registro existe no banco de dados
def registro_existe(model, **kwargs):
    return model.query.filter_by(**kwargs).first() is not None
