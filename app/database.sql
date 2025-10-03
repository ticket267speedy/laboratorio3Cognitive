-- database.sql
CREATE DATABASE IF NOT EXISTS flask_crud_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE flask_crud_db;

-- laboratorio 3
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol ENUM('admin', 'usuario') NOT NULL
);

INSERT INTO usuarios (nombre, email, password, rol) VALUES 
('Administrador', 'admin@mail.com', 'admin123', 'admin'),
('Carlos Vega', 'carlos@abc.com', 'userpass', 'usuario'),
('Ana Luna', 'ana@abc.com', 'userpass', 'usuario');


-- ########################################################################

-- ESTO ES DE LAS CLASES DE COGNITIVE(OMITIR)
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    cantidad INT NOT NULL DEFAULT 0,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Datos de ejemplo
INSERT INTO productos (nombre, descripcion, precio, cantidad) VALUES
('Laptop Dell', 'Laptop para trabajo y gaming', 1200.50, 15),
('Mouse Logitech', 'Mouse inalámbrico ergonómico', 25.99, 50),
('Teclado Mecánico', 'Teclado mecánico RGB', 89.99, 30);

CREATE TABLE IF NOT EXISTS cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    creditos INT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Datos de ejemplo
INSERT INTO cursos (nombre, creditos) VALUES
('Economia', 3),
('Interconectados', 4),
('ICC', 5),
('Redes Digitales', 4);

