
# TABLE: estado
STATE = """
    CREATE TABLE IF NOT EXISTS `estado` (
    `c_estado` INT NOT NULL,
    `d_estado` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`c_estado`),
    UNIQUE INDEX `c_estado_UNIQUE` (`c_estado` ASC))
"""


# TABLE: municipio
TOWNSHIP = """
CREATE TABLE IF NOT EXISTS `municipio` (
`c_mnpio` INT NOT NULL,
`d_mnpio` VARCHAR(45) NOT NULL,
PRIMARY KEY (`c_mnpio`),
UNIQUE INDEX `c_estado_UNIQUE` (`c_mnpio` ASC))
"""


# TABLE: colonia
SUBURB = """
  CREATE TABLE IF NOT EXISTS `colonia` (
  `d_codigo` INT NOT NULL,
  `d_asenta` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`d_codigo`),
  UNIQUE INDEX `c_estado_UNIQUE` (`d_codigo` ASC))
"""


# TABLE: envios
# SHIPPING = """
# CREATE TABLE IF NOT EXISTS `envio` (
#   `envio_id` INT NOT NULL AUTO_INCREMENT,
#   `c_estado` INT NOT NULL,
#   `c_mnpio` INT NOT NULL,
#   `c_colonia` INT NOT NULL,
#   PRIMARY KEY (`envio_id`),
#   UNIQUE INDEX `c_estado_UNIQUE` (`envio_id` ASC))
# """


# SET FOREING KEYS
# SET_INDEX = """
# ALTER TABLE `envio`
# ADD INDEX `estado_envio_fk_idx` (`c_estado` ASC),
# ADD INDEX `municipio_envio_fk_idx` (`c_mnpio` ASC),
# ADD INDEX `colonia_envio_fk_idx` (`c_colonia` ASC)
# """

# SET_FOREING_KEYS = """
# ALTER TABLE `envio`
# ADD CONSTRAINT `estado_envio_fk`
#   FOREIGN KEY (`c_estado`)
#   REFERENCES `estado` (`c_estado`)
#   ON DELETE NO ACTION
#   ON UPDATE NO ACTION,
# ADD CONSTRAINT `municipio_envio_fk`
#   FOREIGN KEY (`c_mnpio`)
#   REFERENCES `municipio` (`c_mnpio`)
#   ON DELETE NO ACTION
#   ON UPDATE NO ACTION,
# ADD CONSTRAINT `colonia_envio_fk`
#   FOREIGN KEY (`c_colonia`)
#   REFERENCES `colonia` (`d_codigo`)
#   ON DELETE NO ACTION
#   ON UPDATE NO ACTION;
# """

ADD_COLUM_MUNICIPIO = """
ALTER TABLE `municipio`
ADD COLUMN `c_estado` INT NOT NULL AFTER `d_mnpio`,
ADD INDEX `estado_municipio_fk_idx` (`c_estado` ASC);
;
"""

ADD_FK_MUNICIPIO = """
ALTER TABLE `municipio`
ADD CONSTRAINT `estado_municipio_fk`
  FOREIGN KEY (`c_estado`)
  REFERENCES `estado` (`c_estado`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
"""

ADD_COLUM_COLONIA = """
ALTER TABLE `curaDeuda`.`colonia`
ADD COLUMN `c_mnpio` INT NOT NULL AFTER `d_asenta`,
ADD INDEX `municipio_colonia_fk_idx` (`c_mnpio` ASC);
;
"""

ADD_FK_COLONIA = """
ALTER TABLE `colonia`
ADD CONSTRAINT `municipio_colonia_fk`
  FOREIGN KEY (`c_mnpio`)
  REFERENCES `municipio` (`c_mnpio`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
 """
