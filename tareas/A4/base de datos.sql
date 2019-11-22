CREATE TABLE venta (
id_venta int  UNIQUE AUTO_INCREMENT,
total INT )ENGINE=InnoDB;

CREATE TABLE producto(
nombre_producto VARCHAR(20) not null,
costo INT NOT NULL,
id_venta INT not null ,
FOREIGN KEY (id_venta)  REFERENCES venta (id_venta)
	on delete cascade
	on update cascade,
FOREIGN KEY (nombre_producto) REFERENCES inventario (nombre_producto)
	on delete cascade
	on update cascade
	)ENGINE=InnoDB;

Create TABLE inventario(
nombre_producto VARCHAR(20) UNIQUE NOT NULL,
 stock INT
)ENGINE=InnoDB;


