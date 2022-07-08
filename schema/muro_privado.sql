-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema muro_privado
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `muro_privado` ;

-- -----------------------------------------------------
-- Schema muro_privado
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `muro_privado` DEFAULT CHARACTER SET utf8 ;
USE `muro_privado` ;

-- -----------------------------------------------------
-- Table `muro_privado`.`usuarios`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `muro_privado`.`usuarios` ;

CREATE TABLE IF NOT EXISTS `muro_privado`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(100) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `muro_privado`.`mensajes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `muro_privado`.`mensajes` ;

CREATE TABLE IF NOT EXISTS `muro_privado`.`mensajes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `contenido` VARCHAR(255) NULL,
  `de_usuario_id` INT NOT NULL,
  `para_ususario_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_mensajes_usuarios_idx` (`de_usuario_id` ASC) VISIBLE,
  INDEX `fk_mensajes_usuarios1_idx` (`para_ususario_id` ASC) VISIBLE,
  CONSTRAINT `fk_mensajes_usuarios`
    FOREIGN KEY (`de_usuario_id`)
    REFERENCES `muro_privado`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mensajes_usuarios1`
    FOREIGN KEY (`para_ususario_id`)
    REFERENCES `muro_privado`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
