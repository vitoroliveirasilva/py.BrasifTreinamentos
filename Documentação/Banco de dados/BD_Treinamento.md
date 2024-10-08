# Documentação Models

## 1. Responsavel
Modelo que representa os responsáveis pelo cadastro de colaboradores e inscrições.

### Campos:
- **id** (INT, PK): Identificador único do responsável.
- **nome** (VARCHAR(100), NOT NULL): Nome completo do responsável.
- **email** (VARCHAR(100), NOT NULL): Endereço de e-mail do responsável.
- **id_azure_ad** (VARCHAR(100), UNIQUE, NOT NULL): Identificador único do Azure AD.
- **permissao** (BOOLEAN, NOT NULL, DEFAULT false): Indica se o responsável tem permissão especial.
- **data_criacao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP)): Data e hora da criação do registro.
- **data_alteracao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)): Data e hora da última alteração do registro.
- **status** (BOOLEAN, DEFAULT true): Indica se o responsável está ativo.

### Métodos:
- **__repr__()**: Representa a instância como uma string, mostrando os principais atributos.

---

## 2. Tipo
Modelo que representa os tipos de marcas.

### Campos:
- **id_tipo** (INT, PK): Identificador único do tipo.
- **nome** (VARCHAR(100), UNIQUE, NOT NULL): Nome do tipo.
- **data_criacao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP)): Data e hora da criação do registro.
- **data_alteracao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)): Data e hora da última alteração do registro.
- **status** (BOOLEAN, DEFAULT true): Indica se o tipo está ativo.

### Métodos:
- **__repr__()**: Representa a instância como uma string, mostrando os principais atributos.

---

## 3. Marca
Modelo que representa as marcas.

### Campos:
- **id_marca** (INT, PK): Identificador único da marca.
- **nome** (VARCHAR(100), UNIQUE, NOT NULL): Nome da marca.
- **data_criacao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP)): Data e hora da criação do registro.
- **data_alteracao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)): Data e hora da última alteração do registro.
- **status** (BOOLEAN, DEFAULT true): Indica se a marca está ativa.

### Métodos:
- **__repr__()**: Representa a instância como uma string, mostrando os principais atributos.

---

## 4. MarcaTipo
Modelo que representa a relação entre marcas e tipos.

### Campos:
- **id_marca_tipo** (INT, PK): Identificador único da relação.
- **id_marca** (INT, FK): Identificador da marca associada.
- **id_tipo** (INT, FK): Identificador do tipo associado.

### Métodos:
- **__repr__()**: Representa a instância como uma string, mostrando os principais atributos.

---

## 5. Treinamento
Modelo que representa os treinamentos oferecidos.

### Campos:
- **id_treinamento** (INT, PK): Identificador único do treinamento.
- **id_marca_tipo** (INT, FK): Identificador da relação entre marca e tipo.
- **treinamento** (VARCHAR(100), NOT NULL): Nome do treinamento.
- **descricao** (TEXT): Descrição detalhada do treinamento.
- **data_criacao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP)): Data e hora da criação do registro.
- **data_alteracao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)): Data e hora da última alteração do registro.
- **status** (BOOLEAN, DEFAULT true): Indica se o treinamento está ativo.

### Métodos:
- **__repr__()**: Representa a instância como uma string, mostrando os principais atributos.

---

## 6. Empresa
Modelo que representa as empresas cadastradas.

### Campos:
- **id_empresa** (INT, PK): Identificador único da empresa.
- **nome_empresa** (VARCHAR(100), NOT NULL): Nome da empresa.
- **filial** (ENUM, NOT NULL): Filial da empresa (opções: Jundiaí, Belo Horizonte, etc.).
- **data_criacao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP)): Data e hora da criação do registro.
- **data_alteracao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)): Data e hora da última alteração do registro.
- **status** (BOOLEAN, DEFAULT true): Indica se a empresa está ativa.

### Métodos:
- **__repr__()**: Representa a instância como uma string, mostrando os principais atributos.

---

## 7. Colaborador
Modelo que representa os colaboradores das empresas.

### Campos:
- **id_colaborador** (INT, PK): Identificador único do colaborador.
- **nome** (VARCHAR(100), NOT NULL): Nome completo do colaborador.
- **email** (VARCHAR(100), NOT NULL): Endereço de e-mail do colaborador.
- **cargo** (VARCHAR(100)): Cargo do colaborador na empresa.
- **id_empresa** (INT, FK): Identificador da empresa onde o colaborador está vinculado.
- **id_responsavel** (INT, FK): Identificador do responsável pelo colaborador.
- **filial** (ENUM, NOT NULL): Filial onde o colaborador está localizado.
- **data_criacao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP)): Data e hora da criação do registro.
- **data_alteracao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)): Data e hora da última alteração do registro.
- **status** (BOOLEAN, DEFAULT true): Indica se o colaborador está ativo.

### Métodos:
- **__repr__()**: Representa a instância como uma string, mostrando os principais atributos.

---

## 8. Login
Modelo que representa os logins dos colaboradores.

### Campos:
- **id_login** (INT, PK): Identificador único do login.
- **id_colaborador** (INT, FK): Identificador do colaborador associado ao login.
- **id_marca_tipo** (INT, FK): Identificador da relação entre marca e tipo.
- **usuario** (VARCHAR(100), NOT NULL): Nome de usuário utilizado para login.
- **data_criacao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP)): Data e hora da criação do registro.
- **data_alteracao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)): Data e hora da última alteração do registro.
- **status** (BOOLEAN, DEFAULT true): Indica se o login está ativo.

### Métodos:
- **__repr__()**: Representa a instância como uma string, mostrando os principais atributos.

---

## 9. Inscricao
Modelo que representa as inscrições em treinamentos.

### Campos:
- **id_inscricao** (INT, PK): Identificador único da inscrição.
- **id_colaborador** (INT, FK): Identificador do colaborador inscrito.
- **id_treinamento** (INT, FK): Identificador do treinamento no qual o colaborador está inscrito.
- **id_responsavel** (INT, FK): Identificador do responsável pela inscrição.
- **data_inscricao** (DATE, NOT NULL): Data em que a inscrição foi realizada.
- **status** (ENUM, NOT NULL): Status da inscrição (opções: Pendente, Concluída, Cancelada).
- **data_criacao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP)): Data e hora da criação do registro.
- **data_alteracao** (TIMESTAMP, DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)): Data e hora da última alteração do registro.

### Métodos:
- **__repr__()**: Representa a instância como uma string, mostrando os principais atributos.
