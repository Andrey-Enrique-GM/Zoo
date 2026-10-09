-- Se crea la tabla chihuahuas si no existe
CREATE TABLE IF NOT EXISTS chihuahuas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    imagen VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Se ingresan 6 chihuahuas iniciales a la tabla chihuahuas
INSERT INTO chihuahuas (tipo, descripcion, imagen) VALUES 
('Cabeza de Manzana', 'Craneo redondo, frente alta, ojos grandes y saltones.', 'images/chihuahua_manzana.png'),
('Cabeza de Venado', 'Hocico mas largo y estrecho, craneo plano como el de un ciervo.', 'images/chihuahua_venado.png'),
('Pelo corto', 'Manto liso, suave y pegado al cuerpo.', 'images/chihuahua_pelo_corto.png'),
('Pelo largo', 'Pelo fino, sedoso, ondulado. Flecos en orejas y cola.', 'images/chihuahua_pelo_largo.png'),
('Miniatura (Toy)', 'Tamaño extremadamente pequeño y pesa menos de 2kg.', 'images/chihuahua_miniatura.png'),
('Sin pelo (Hairless)', 'Variacion genetica menos comun de piel expuesta.', 'images/chihuahua_sin_pelo.png');