CREATE TABLE `tb_responsaveis` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `id_azure_ad` VARCHAR(100) UNIQUE NOT NULL,
  `permissao` BOOLEAN NOT NULL DEFAULT false,
  `data_criacao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `data_alteracao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP),
  `status` BOOLEAN DEFAULT true
);

CREATE TABLE `tb_tipos` (
  `id_tipo` INT PRIMARY KEY AUTO_INCREMENT,
  `nome` VARCHAR(100) UNIQUE NOT NULL,
  `data_criacao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `data_alteracao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP),
  `status` BOOLEAN DEFAULT true
);

CREATE TABLE `tb_marcas` (
  `id_marca` INT PRIMARY KEY AUTO_INCREMENT,
  `nome` VARCHAR(100) UNIQUE NOT NULL,
  `data_criacao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `data_alteracao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP),
  `status` BOOLEAN DEFAULT true
);

CREATE TABLE `tb_marca_tipo` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `id_marca` INT NOT NULL,
  `id_tipo` INT NOT NULL,
  UNIQUE (`id_marca`, `id_tipo`),
  FOREIGN KEY (`id_marca`) REFERENCES `tb_marcas` (`id_marca`),
  FOREIGN KEY (`id_tipo`) REFERENCES `tb_tipos` (`id_tipo`)
);

CREATE TABLE `tb_treinamentos` (
  `id_treinamento` INT PRIMARY KEY AUTO_INCREMENT,
  `id_marca_tipo` INT NOT NULL,
  `treinamento` VARCHAR(100) NOT NULL,
  `descricao` TEXT,
  `data_criacao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `data_alteracao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP),
  `status` BOOLEAN DEFAULT true,
  UNIQUE (`treinamento`, `id_marca_tipo`),  -- Unicidade do treinamento por marca e tipo
  FOREIGN KEY (`id_marca_tipo`) REFERENCES `tb_marca_tipo` (`id`)
);

CREATE TABLE `tb_empresas` (
  `id_empresa` INT PRIMARY KEY AUTO_INCREMENT,
  `nome_empresa` VARCHAR(100) NOT NULL,
  `filial` ENUM('Jundiaí', 'Belo Horizonte', 'Ribeirão Preto', 'Cuiabá', 'Rio de Janeiro', 'Tocantins', 'Brasília', 'Goiânia', 'Curitiba') NOT NULL,
  UNIQUE (`nome_empresa`, `filial`),  -- Unicidade do nome da empresa dentro de cada filial
  `data_criacao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `data_alteracao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP),
  `status` BOOLEAN DEFAULT true
);

CREATE TABLE `tb_colaboradores` (
  `id_colaborador` INT PRIMARY KEY AUTO_INCREMENT,
  `nome` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `cargo` VARCHAR(100),
  `id_empresa` INT NOT NULL,
  `id_responsavel` INT NOT NULL,
  `filial` ENUM('Jundiaí', 'Belo Horizonte', 'Ribeirão Preto', 'Cuiabá', 'Rio de Janeiro', 'Tocantins', 'Brasília', 'Goiânia', 'Curitiba') NOT NULL,
  `data_criacao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `data_alteracao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP),
  `status` BOOLEAN DEFAULT true,
  FOREIGN KEY (`id_empresa`) REFERENCES `tb_empresas` (`id_empresa`),
  FOREIGN KEY (`id_responsavel`) REFERENCES `tb_responsaveis` (`id`)
);

CREATE TABLE `tb_logins` (
  `id_login` INT PRIMARY KEY AUTO_INCREMENT,
  `id_colaborador` INT NOT NULL,
  `id_marca_tipo` INT NOT NULL,
  `usuario` VARCHAR(100) NOT NULL,
  UNIQUE (`usuario`, `id_marca_tipo`),  -- Unicidade do login por marca e tipo
  `data_criacao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `data_alteracao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP),
  `status` BOOLEAN DEFAULT true,
  FOREIGN KEY (`id_colaborador`) REFERENCES `tb_colaboradores` (`id_colaborador`),
  FOREIGN KEY (`id_marca_tipo`) REFERENCES `tb_marca_tipo` (`id`)
);

CREATE TABLE `tb_inscricoes` (
  `id_inscricao` INT PRIMARY KEY AUTO_INCREMENT,
  `id_colaborador` INT NOT NULL,
  `id_treinamento` INT NOT NULL,
  `id_responsavel` INT NOT NULL,
  `data_inscricao` DATE NOT NULL,
  `status` ENUM('Pendente', 'Concluída', 'Cancelada') NOT NULL,
  `data_criacao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `data_alteracao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP),
  FOREIGN KEY (`id_colaborador`) REFERENCES `tb_colaboradores` (`id_colaborador`),
  FOREIGN KEY (`id_treinamento`) REFERENCES `tb_treinamentos` (`id_treinamento`),
  FOREIGN KEY (`id_responsavel`) REFERENCES `tb_responsaveis` (`id`)
);
