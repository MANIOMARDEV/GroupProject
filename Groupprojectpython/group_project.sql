-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema group_project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema group_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `group_project` DEFAULT CHARACTER SET utf8 ;
USE `group_project` ;

-- -----------------------------------------------------
-- Table `group_project`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `group_project`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `group_project`.`repairs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `group_project`.`repairs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `location` VARCHAR(255) NULL,
  `description` VARCHAR(255) NULL,
  `phone` INT (8) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `user_id_posted` INT NOT NULL,
  `user_id_worker` INT NOT NULL,
  PRIMARY KEY (`id`, `user_id_posted`, `user_id_worker`),
  INDEX `fk_repairs_users2_idx` (`user_id_posted` ASC) VISIBLE,
  INDEX `fk_repairs_users3_idx` (`user_id_worker` ASC) VISIBLE,
  CONSTRAINT `fk_repairs_users2`
    FOREIGN KEY (`user_id_posted`)
    REFERENCES `group_project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_repairs_users3`
    FOREIGN KEY (`user_id_worker`)
    REFERENCES `group_project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `group_project`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `group_project`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `group_project`.`repairs`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `group_project`.`repairs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `location` VARCHAR(255) NULL,
  `description` VARCHAR(255) NULL,
  `phone` INT (8) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `updated_at` DATETIME NULL DEFAULT NOW(),
  `user_id_posted` INT NOT NULL,
  `user_id_worker` INT NOT NULL,
  PRIMARY KEY (`id`, `user_id_posted`, `user_id_worker`),
  INDEX `fk_repairs_users2_idx` (`user_id_posted` ASC) VISIBLE,
  INDEX `fk_repairs_users3_idx` (`user_id_worker` ASC) VISIBLE,
  CONSTRAINT `fk_repairs_users2`
    FOREIGN KEY (`user_id_posted`)
    REFERENCES `group_project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_repairs_users3`
    FOREIGN KEY (`user_id_worker`)
    REFERENCES `group_project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
