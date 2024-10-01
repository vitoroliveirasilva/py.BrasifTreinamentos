# Estruturas do Projeto

- [Fluxo de Trabalho com Branches](#fluxo-de-trabalho-com-branches)
- [Padrões de Commit](#padrões-de-commit)

## Fluxo de Trabalho com Branches

### Branches Principais
- **Desenvolvimento**: Utilizada para o Desenvolvimento de novas funcionalidades e ajustes.
- **Homologação**: Usada para realizar testes e validações antes de liberar para produção.
- **main-(Produção)**: Contém o código estável que está em produção.

### Direções de Merge
- **Desenvolvimento → Homologação**: Quando uma nova funcionalidade ou correção é finalizada, o código da branch de Desenvolvimento é movido para a de Homologação.
- **Homologação → main-(Produção)**: Após a validação dos testes em Homologação, o código é movido para a produção.

### Fluxo de Trabalho
1. **Desenvolvimento na Branch Desenvolvimento**: Os desenvolvedores trabalham na branch `Desenvolvimento`, criando e ajustando funcionalidades.
2. **Merge para Homologação**: Após finalizar a funcionalidade ou correção, o merge é feito da branch `Desenvolvimento` para a branch `Homologação`, onde ocorrem os testes.
3. **Testes na Branch Homologação**: Realização de testes e validações. Se tudo estiver correto, o código é considerado pronto para produção.
4. **Merge para Produção**: O código aprovado é mesclado da branch `Homologação` para a branch `main-(Produção)`, sendo então liberado para o ambiente de produção.

## Padrões de Commit

### Formato do Commit
Use o formato: `TIPO - Descrição`, seguindo as boas práticas do Git.

**Exemplo de Commit**: `FEAT - Adiciona a página de login`

### Tipos de Commit

| Tipo    | Descrição                                                                 |
|---------|---------------------------------------------------------------------------|
| FEAT    | Inclusão de um novo recurso ou funcionalidade.                            |
| FIX     | Correção de um bug ou problema no código.                                 |
| DOCS    | Alterações na documentação.                                               |
| TEST    | Criação, modificação ou remoção de testes.                                |
| BUILD   | Mudanças em arquivos de build e nas dependências do projeto.              |
| RAW     | Alterações relacionadas a arquivos de configuração, dados, ou parâmetros. |
| CLEANUP | Remoção de código comentado ou desnecessário, visando melhorar a legibilidade e manutenção do projeto. |
| REMOVE  | Exclusão de arquivos, diretórios ou funcionalidades obsoletas.            |