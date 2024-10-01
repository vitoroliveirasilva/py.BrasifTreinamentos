## Estrutura de Arquivos

A divisão dos modelos por arquivos visa facilitar a organização do projeto. A estrutura do diretório está da seguinte maneira:

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

Cada arquivo contém a classe que representa uma tabela no banco de dados. O arquivo `__init__.py` serve para inicializar e disponibilizar os modelos para serem utilizados no projeto.

---

### 1. **Responsáveis** (`tb_responsaveis.py`)

**Tabela: `tb_responsaveis`**

Armazena informações sobre os responsáveis pelos colaboradores.

- **Campos:**
  - `id`: Chave primária.
  - `nome`: Nome do responsável.
  - `email`: E-mail do responsável.
  - `id_azure_ad`: ID único no Azure AD.
  - `permissao`: Define se o responsável possui permissões administrativas.
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração do registro.
  - `status`: Indica se o registro está ativo.

- **Relacionamento:**
  - Um responsável pode estar associado a vários colaboradores.

```python
class Responsavel(db.Model):
    # Definição dos campos e relacionamentos
```

---

### 2. **Filiais** (`enum_filiais.py`)

**Enumeração: `enum_filiais`**

Define as filiais disponíveis como valores fixos.

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

### 3. **Tipos de Treinamento** (`tb_tipos.py`)

**Tabela: `tb_tipos`**

Armazena os diferentes tipos de treinamentos.

- **Campos:**
  - `id_tipo`: Chave primária.
  - `nome`: Nome único do tipo de treinamento.
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração do registro.
  - `status`: Indica se o tipo de treinamento está ativo.

- **Relacionamento:**
  - Um tipo pode ter várias marcas associadas.

```python
class Tipo(db.Model):
    # Definição dos campos e relacionamentos
```

---

### 4. **Marcas** (`tb_marcas.py`)

**Tabela: `tb_marcas`**

Armazena informações sobre as marcas associadas aos treinamentos.

- **Campos:**
  - `id_marca`: Chave primária.
  - `nome`: Nome único da marca.
  - `id_tipo`: Chave estrangeira referenciando `tb_tipos`.
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração do registro.
  - `status`: Indica se a marca está ativa.

- **Relacionamento:**
  - Uma marca pertence a um tipo de treinamento e pode ter vários treinamentos e logins associados.

```python
class Marca(db.Model):
    # Definição dos campos e relacionamentos
```

---

### 5. **Treinamentos** (`tb_treinamentos.py`)

**Tabela: `tb_treinamentos`**

Armazena informações sobre os treinamentos disponíveis.

- **Campos:**
  - `id_treinamento`: Chave primária.
  - `id_marca`: Chave estrangeira referenciando `tb_marcas`.
  - `treinamento`: Nome do treinamento.
  - `descricao`: Descrição do treinamento.
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração do registro.
  - `status`: Indica se o treinamento está ativo.

- **Relacionamento:**
  - Um treinamento pertence a uma marca e pode ter várias inscrições associadas.

```python
class Treinamento(db.Model):
    # Definição dos campos e relacionamentos
```

---

### 6. **Empresas** (`tb_empresas.py`)

**Tabela: `tb_empresas`**

Armazena informações sobre as empresas às quais os colaboradores estão vinculados.

- **Campos:**
  - `id_empresa`: Chave primária.
  - `nome_empresa`: Nome da empresa.
  - `filial`: Localização da empresa (usando a enumeração `enum_filiais`).
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração do registro.
  - `status`: Indica se a empresa está ativa.

- **Relacionamento:**
  - Uma empresa pode ter vários colaboradores associados.

```python
class Empresa(db.Model):
    # Definição dos campos e relacionamentos
```

---

### 7. **Colaboradores** (`tb_colaboradores.py`)

**Tabela: `tb_colaboradores`**

Armazena informações sobre os colaboradores.

- **Campos:**
  - `id_colaborador`: Chave primária.
  - `nome`: Nome do colaborador.
  - `email`: E-mail do colaborador.
  - `cargo`: Cargo do colaborador.
  - `id_empresa`: Chave estrangeira referenciando `tb_empresas`.
  - `id_responsavel`: Chave estrangeira referenciando `tb_responsaveis`.
  - `filial`: Localização do colaborador (usando a enumeração `enum_filiais`).
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração do registro.
  - `status`: Indica se o colaborador está ativo.

- **Relacionamento:**
  - Um colaborador pertence a uma empresa e é gerenciado por um responsável.
  - Um colaborador pode ter vários logins e inscrições associadas.

```python
class Colaborador(db.Model):
    # Definição dos campos e relacionamentos
```

---

### 8. **Logins** (`tb_logins.py`)

**Tabela: `tb_logins`**

Armazena as informações de login dos colaboradores para cada marca.

- **Campos:**
  - `id_login`: Chave primária.
  - `id_colaborador`: Chave estrangeira referenciando `tb_colaboradores`.
  - `id_marca`: Chave estrangeira referenciando `tb_marcas`.
  - `usuario`: Nome de usuário para login.
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração do registro.
  - `status`: Indica se o login está ativo.

```python
class Login(db.Model):
    # Definição dos campos e relacionamentos
```

---

### 9. **Inscrições** (`tb_inscricoes.py`)

**Tabela: `tb_inscricoes`**

Armazena as informações sobre as inscrições dos colaboradores nos treinamentos.

- **Campos:**
  - `id_inscricao`: Chave primária.
  - `id_colaborador`: Chave estrangeira referenciando `tb_colaboradores`.
  - `id_treinamento`: Chave estrangeira referenciando `tb_treinamentos`.
  - `id_responsavel`: Chave estrangeira referenciando `tb_responsaveis` (responsável pela inscrição).
  - `data_inscricao`: Data da inscrição.
  - `status`: Status da inscrição (ex: "Pendente", "Concluída", "Cancelada").
  - `data_criacao`: Data de criação do registro.
  - `data_alteracao`: Data da última alteração do registro.

```python
class Inscricao(db.Model):
    # Definição dos campos e relacionamentos
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

- Cada model possui um método `__repr__` que permite exibir uma representação legível da instância.
- As colunas `data_criacao`, `data_alteracao` e `status` foram adicionadas às tabelas onde é necessário controle de auditoria e estado.
- As relações entre tabelas são definidas com `ForeignKey` e `relationship` para garantir integridade referencial e facilitar a navegação entre os dados.
