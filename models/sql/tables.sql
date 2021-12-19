
-- # TABLE: estado

CREATE TABLE IF NOT EXISTS `estado` (
`c_estado` INT NOT NULL,
`d_estado` VARCHAR(45) NOT NULL,
PRIMARY KEY (`c_estado`),
UNIQUE INDEX `c_estado_UNIQUE` (`c_estado` ASC));


-- # TABLE: municipio

CREATE TABLE IF NOT EXISTS `municipio` (
`c_mnpio` INT NOT NULL,
`d_mnpio` VARCHAR(45) NOT NULL,
PRIMARY KEY (`c_mnpio`),
UNIQUE INDEX `c_estado_UNIQUE` (`c_mnpio` ASC));


-- # TABLE: colonia

CREATE TABLE IF NOT EXISTS `colonia` (
  `d_codigo` INT NOT NULL,
  `d_asenta` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`d_codigo`),
  UNIQUE INDEX `c_estado_UNIQUE` (`d_codigo` ASC));


-- # TABLE: envios

CREATE TABLE IF NOT EXISTS `envio` (
  `envio_id` INT NOT NULL AUTO_INCREMENT,
  `c_estado` INT NOT NULL,
  `c_mnpio` INT NOT NULL,
  `c_colonia` INT NOT NULL,
  PRIMARY KEY (`envio_id`),
  UNIQUE INDEX `c_estado_UNIQUE` (`envio_id` ASC));


-- # SET FOREING KEYS

ALTER TABLE `envio`
ADD INDEX `estado_envio_fk_idx` (`c_estado` ASC),
ADD INDEX `municipio_envio_fk_idx` (`c_mnpio` ASC),
ADD INDEX `colonia_envio_fk_idx` (`c_colonia` ASC);
;
ALTER TABLE `envio`
ADD CONSTRAINT `estado_envio_fk`
  FOREIGN KEY (`c_estado`)
  REFERENCES `estado` (`c_estado`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `municipio_envio_fk`
  FOREIGN KEY (`c_mnpio`)
  REFERENCES `municipio` (`c_mnpio`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `colonia_envio_fk`
  FOREIGN KEY (`c_colonia`)
  REFERENCES `colonia` (`d_codigo`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
