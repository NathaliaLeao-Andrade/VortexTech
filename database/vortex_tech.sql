CREATE DATABASE vortex_tech;
USE vortex_tech;

-- =========================
-- USUÁRIOS
-- =========================
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- PERFIS
-- =========================
CREATE TABLE perfis (
    id_perfil INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    idade INT,
    cidade VARCHAR(100),
    interesse VARCHAR(100),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =========================
-- CATEGORIAS
-- =========================
CREATE TABLE categorias (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nome_categoria VARCHAR(100) NOT NULL
);

-- =========================
-- MÓDULOS
-- =========================
CREATE TABLE modulos (
    id_modulo INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT
);

-- =========================
-- CONTEÚDOS
-- =========================
CREATE TABLE conteudos (
    id_conteudo INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(150) NOT NULL,
    descricao TEXT,
    link_conteudo VARCHAR(255),
    id_categoria INT,
    id_modulo INT,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_modulo) REFERENCES modulos(id_modulo)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =========================
-- INTERAÇÕES
-- =========================
CREATE TABLE interacoes (
    id_interacao INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT,
    id_conteudo INT,
    tipo_interacao VARCHAR(50),
    data_interacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_conteudo) REFERENCES conteudos(id_conteudo)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);