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
  `id_tipo` INT NOT NULL,
  `data_criacao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `data_alteracao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP),
  `status` BOOLEAN DEFAULT true
);

CREATE TABLE `tb_treinamentos` (
  `id_treinamento` INT PRIMARY KEY AUTO_INCREMENT,
  `id_marca` INT NOT NULL,
  `treinamento` VARCHAR(100) NOT NULL,
  `descricao` TEXT,
  `data_criacao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `data_alteracao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP),
  `status` BOOLEAN DEFAULT true
);

CREATE TABLE `tb_empresas` (
  `id_empresa` INT PRIMARY KEY AUTO_INCREMENT,
  `nome_empresa` VARCHAR(100) NOT NULL,
  `filial` ENUM('Jundiaí', 'Belo Horizonte', 'Ribeirão Preto', 'Cuiabá', 'Rio de Janeiro', 'Tocantins', 'Brasília', 'Goiânia', 'Curitiba') NOT NULL,
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
  `status` BOOLEAN DEFAULT true
);

CREATE TABLE `tb_logins` (
  `id_login` INT PRIMARY KEY AUTO_INCREMENT,
  `id_colaborador` INT NOT NULL,
  `id_marca` INT NOT NULL,
  `usuario` VARCHAR(100) NOT NULL,
  `data_criacao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `data_alteracao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP),
  `status` BOOLEAN DEFAULT true
);

CREATE TABLE `tb_inscricoes` (
  `id_inscricao` INT PRIMARY KEY AUTO_INCREMENT,
  `id_colaborador` INT NOT NULL,
  `id_treinamento` INT NOT NULL,
  `id_responsavel` INT NOT NULL,
  `data_inscricao` DATE NOT NULL,
  `status` ENUM('Pendente', 'Concluída', 'Cancelada') NOT NULL,
  `data_criacao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP),
  `data_alteracao` TIMESTAMP DEFAULT (CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)
);

-- Relações
ALTER TABLE `tb_marcas` ADD FOREIGN KEY (`id_tipo`) REFERENCES `tb_tipos` (`id_tipo`);

ALTER TABLE `tb_treinamentos` ADD FOREIGN KEY (`id_marca`) REFERENCES `tb_marcas` (`id_marca`);

ALTER TABLE `tb_colaboradores` ADD FOREIGN KEY (`id_empresa`) REFERENCES `tb_empresas` (`id_empresa`);

ALTER TABLE `tb_colaboradores` ADD FOREIGN KEY (`id_responsavel`) REFERENCES `tb_responsaveis` (`id`);

ALTER TABLE `tb_logins` ADD FOREIGN KEY (`id_colaborador`) REFERENCES `tb_colaboradores` (`id_colaborador`);

ALTER TABLE `tb_logins` ADD FOREIGN KEY (`id_marca`) REFERENCES `tb_marcas` (`id_marca`);

ALTER TABLE `tb_inscricoes` ADD FOREIGN KEY (`id_colaborador`) REFERENCES `tb_colaboradores` (`id_colaborador`);

ALTER TABLE `tb_inscricoes` ADD FOREIGN KEY (`id_treinamento`) REFERENCES `tb_treinamentos` (`id_treinamento`);

ALTER TABLE `tb_inscricoes` ADD FOREIGN KEY (`id_responsavel`) REFERENCES `tb_responsaveis` (`id`);