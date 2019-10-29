SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Cars`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `mydb`.`Cars` (
  `c_ID` INT NOT NULL ,
  `c_VIN` VARCHAR(45) NULL ,
  `c_manuf` VARCHAR(45) NULL ,
  `c_model` VARCHAR(45) NULL ,
  `c_year` VARCHAR(45) NULL ,
  `c_color` VARCHAR(45) NULL ,
  PRIMARY KEY (`c_ID`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Customers`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `mydb`.`Customers` (
  `c_ID` INT NOT NULL ,
  `c_c_ID` VARCHAR(45) NULL ,
  `c_name` VARCHAR(45) NULL ,
  `c_phone` VARCHAR(45) NULL ,
  `c_email` VARCHAR(45) NULL ,
  `c_address` VARCHAR(45) NULL ,
  `c_city` VARCHAR(45) NULL ,
  `c_state_prov` VARCHAR(45) NULL ,
  `c_country` VARCHAR(45) NULL ,
  `c_postal` VARCHAR(45) NULL ,
  PRIMARY KEY (`c_ID`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Salesperson`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `mydb`.`Salesperson` (
  `s_ID` INT NOT NULL ,
  `s_s_ID` VARCHAR(45) NULL ,
  `s_name` VARCHAR(45) NULL ,
  `s_store` VARCHAR(45) NULL ,
  PRIMARY KEY (`s_ID`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Invoice`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `mydb`.`Invoice` (
  `in_ID` INT NOT NULL ,
  `in_num` VARCHAR(45) NULL ,
  `in_date` VARCHAR(45) NULL ,
  `c_VIN` VARCHAR(45) NULL ,
  `c_c_ID` VARCHAR(45) NULL ,
  `s_s_ID` VARCHAR(45) NULL ,
  `Cars_c_ID` INT NOT NULL ,
  PRIMARY KEY (`in_ID`, `Cars_c_ID`) )
ENGINE = InnoDB;

USE `mydb` ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
