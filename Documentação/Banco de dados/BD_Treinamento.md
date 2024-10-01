Aqui está a documentação completa atualizada, incorporando as novas informações e comentários conforme solicitado:

## Estrutura de Arquivos

A divisão dos modelos por arquivos visa facilitar a organização. O projeto está estruturado da seguinte maneira:

```
/models
  ├── enum_filiais.py
  ├── tb_responsaveis.py
  ├── tb_tipos.py
  ├── tb_marcas.py
  ├── tb_treinamentos.py
  ├── tb_empresas.py
  ├── tb_colaboradores.py
  ├── tb_logins.py
  ├── tb_inscricoes.py
  └── __init__.py
```

Cada arquivo contém a classe que representa a tabela no banco de dados. O arquivo `__init__.py` inicializa os modelos para serem utilizados no projeto.

---

### 1. **Responsável** (`tb_responsaveis.py`)

**Tabela: `tb_responsaveis`**

Armazena informações dos responsáveis pelos colaboradores.

- **Campos:**
  - `id`: Chave primária.
  - `nome`: Nome do responsável.
  - `email`: E-mail do responsável.
  - `id_azure_ad`: ID único no Azure AD.
  - `permissao`: Define se o responsável tem permissões administrativas.
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração.
  - `status`: Indica se o registro está ativo.

- **Relacionamento:**
  - Um responsável pode estar associado a vários colaboradores.

```python
class Responsavel(db.Model):
    # Definição dos campos e relacionamento
```

---

### 2. **Filiais** (`enum_filiais.py`)

**Tabela: `enum_filiais`**

Armazena as filiais com valores fixos.

- **Valores possíveis:**
  - Jundiaí
  - Belo Horizonte
  - Ribeirão Preto
  - Cuiabá
  - Rio de Janeiro
  - Tocantins
  - Brasília
  - Goiânia
  - Curitiba

```python
class Filiais(Enum):
    # Definição dos valores da enumeração
```

---

### 3. **Tipo** (`tb_tipos.py`)

**Tabela: `tb_tipos`**

Armazena os diferentes tipos de treinamentos.

- **Campos:**
  - `id_tipo`: Chave primária.
  - `nome`: Nome único do tipo de treinamento.
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração.
  - `status`: Indica se o tipo está ativo.

- **Relacionamento:**
  - Um tipo pode ter várias marcas associadas.

```python
class Tipo(db.Model):
    # Definição dos campos e relacionamento
```

---

### 4. **Marca** (`tb_marcas.py`)

**Tabela: `tb_marcas`**

Armazena informações sobre as marcas relacionadas aos treinamentos.

- **Campos:**
  - `id_marca`: Chave primária.
  - `nome`: Nome único da marca.
  - `id_tipo`: Chave estrangeira referenciando `tb_tipos`.
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração.
  - `status`: Indica se a marca está ativa.

- **Relacionamento:**
  - Uma marca está associada a um tipo de treinamento e pode ter vários treinamentos e logins.

```python
class Marca(db.Model):
    # Definição dos campos e relacionamento
```

---

### 5. **Treinamento** (`tb_treinamentos.py`)

**Tabela: `tb_treinamentos`**

Armazena informações sobre os treinamentos disponíveis.

- **Campos:**
  - `id_treinamento`: Chave primária.
  - `id_marca`: Chave estrangeira referenciando `tb_marcas`.
  - `treinamento`: Nome do treinamento.
  - `descricao`: Descrição do treinamento.
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração.
  - `status`: Indica se o treinamento está ativo.

- **Relacionamento:**
  - Um treinamento pertence a uma marca e pode ter várias inscrições.

```python
class Treinamento(db.Model):
    # Definição dos campos e relacionamento
```

---

### 6. **Empresa** (`tb_empresas.py`)

**Tabela: `tb_empresas`**

Armazena informações sobre as empresas a que os colaboradores pertencem.

- **Campos:**
  - `id_empresa`: Chave primária.
  - `nome_empresa`: Nome da empresa.
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração.
  - `status`: Indica se a empresa está ativa.

- **Relacionamento:**
  - Uma empresa pode ter vários colaboradores.

```python
class Empresa(db.Model):
    # Definição dos campos e relacionamento
```

---

### 7. **Colaborador** (`tb_colaboradores.py`)

**Tabela: `tb_colaboradores`**

Armazena informações sobre os colaboradores.

- **Campos:**
  - `id_colaborador`: Chave primária.
  - `nome`: Nome do colaborador.
  - `email`: E-mail do colaborador.
  - `cargo`: Cargo do colaborador.
  - `id_empresa`: Chave estrangeira referenciando `tb_empresas`.
  - `id_responsavel`: Chave estrangeira referenciando `tb_responsaveis`.
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração.
  - `status`: Indica se o colaborador está ativo.

- **Relacionamento:**
  - Um colaborador pertence a uma empresa e tem um responsável.
  - Um colaborador pode ter vários logins e inscrições.

```python
class Colaborador(db.Model):
    # Definição dos campos e relacionamento
```

---

### 8. **Login** (`tb_logins.py`)

**Tabela: `tb_logins`**

Armazena as informações de login dos colaboradores para cada marca.

- **Campos:**
  - `id_login`: Chave primária.
  - `id_colaborador`: Chave estrangeira referenciando `tb_colaboradores`.
  - `id_marca`: Chave estrangeira referenciando `tb_marcas`.
  - `usuario`: Nome de usuário do login.
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração.
  - `status`: Indica se o login está ativo.

```python
class Login(db.Model):
    # Definição dos campos e relacionamento
```

---

### 9. **Inscrição** (`tb_inscricoes.py`)

**Tabela: `tb_inscricoes`**

Armazena as informações das inscrições dos colaboradores nos treinamentos.

- **Campos:**
  - `id_inscricao`: Chave primária.
  - `id_colaborador`: Chave estrangeira referenciando `tb_colaboradores`.
  - `id_treinamento`: Chave estrangeira referenciando `tb_treinamentos`.
  - `data_inscricao`: Data da inscrição.
  - `status`: Status da inscrição (ex: "Completo", "Pendente").
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração.

```python
class Inscricao(db.Model):
    # Definição dos campos e relacionamento
```

---

### 10. **Inicialização dos Models** (`__init__.py`)

Este arquivo é responsável por inicializar os modelos no banco de dados e conectá-los ao aplicativo Flask.

```python
from .enum_filiais import Filiais
from .tb_responsaveis import Responsavel
from .tb_tipos import Tipo
from .tb_marcas import Marca
from .tb_treinamentos import Treinamento
from .tb_empresas import Empresa
from .tb_colaboradores import Colaborador
from .tb_logins import Login
from .tb_inscricoes import Inscricao
```

---

### Considerações Finais

- Cada model tem um método `__repr__` que permite exibir uma representação legível da instância.
- As colunas `data_criacao`, `data_alteracao` e `status` foram adicionadas em tabelas apropriadas para permitir auditoria e controle de estado.
- As relações entre tabelas são mapeadas com `ForeignKey` e `relationship`. 
