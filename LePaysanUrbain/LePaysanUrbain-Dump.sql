-- MySQL Script generated by MySQL Workbench
-- Mon Dec 16 10:38:08 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema LePaysanUrbain
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema LePaysanUrbain
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `LePaysanUrbain` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `LePaysanUrbain` ;

-- -----------------------------------------------------
-- Table `LePaysanUrbain`.`FOURNISSEUR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LePaysanUrbain`.`FOURNISSEUR` (
  `FO_ID` INT NOT NULL,
  `FO_NOM` VARCHAR(45) NULL,
  `FO_ADRESSE` VARCHAR(45) NULL,
  `FO_TEL` INT NULL,
  `FO_MAIL` VARCHAR(45) NULL,
  PRIMARY KEY (`FO_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LePaysanUrbain`.`LIGNE_COMMANDE_FOURNISSEUR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LePaysanUrbain`.`LIGNE_COMMANDE_FOURNISSEUR` (
  `id` INT NOT NULL,
  `LCF_ID` VARCHAR(45) NULL,
  `LCF_PRODUIT` VARCHAR(45) NULL,
  `LCF_QUANTITE` INT NULL,
  `LCF_PRIXUNIT` INT NULL,
  `FOURNISSEUR_FO_ID` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_LIGNE_COMMANDE_FOURNISSEUR_FOURNISSEUR1_idx` (`FOURNISSEUR_FO_ID` ASC) VISIBLE,
  CONSTRAINT `fk_LIGNE_COMMANDE_FOURNISSEUR_FOURNISSEUR1`
    FOREIGN KEY (`FOURNISSEUR_FO_ID`)
    REFERENCES `LePaysanUrbain`.`FOURNISSEUR` (`FO_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LePaysanUrbain`.`SERRE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LePaysanUrbain`.`SERRE` (
  `SER_ID` INT NOT NULL,
  `SER_TEMPERATURE` INT NULL,
  `SER_TAUXHUMID` INT NULL,
  PRIMARY KEY (`SER_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LePaysanUrbain`.`COMMANDE_FOURNISSEUR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LePaysanUrbain`.`COMMANDE_FOURNISSEUR` (
  `COFO_ID` INT NOT NULL,
  `COFO_NUMF` INT NULL,
  `COFO_DATEF` DATETIME NULL,
  `COFO_COUTF` INT NULL,
  `LIGNE_COMMANDE_FOURNISSEUR_id` INT NOT NULL,
  PRIMARY KEY (`COFO_ID`),
  INDEX `fk_COMMANDE_FOURNISSEUR_LIGNE_COMMANDE_FOURNISSEUR1_idx` (`LIGNE_COMMANDE_FOURNISSEUR_id` ASC) VISIBLE,
  CONSTRAINT `fk_COMMANDE_FOURNISSEUR_LIGNE_COMMANDE_FOURNISSEUR1`
    FOREIGN KEY (`LIGNE_COMMANDE_FOURNISSEUR_id`)
    REFERENCES `LePaysanUrbain`.`LIGNE_COMMANDE_FOURNISSEUR` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LePaysanUrbain`.`GRAINE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LePaysanUrbain`.`GRAINE` (
  `GRA_ID` INT NOT NULL,
  `GRA_NOM` VARCHAR(45) NULL,
  `GRA_VARIETE` VARCHAR(45) NULL,
  `GRA_DEBUT_PROD` DATETIME NULL,
  `GRA_FIN_PROD` DATETIME NULL,
  `COMMANDE_FOURNISSEUR_COFO_ID` INT NOT NULL,
  `SERRE_SER_ID` INT NOT NULL,
  PRIMARY KEY (`GRA_ID`),
  INDEX `fk_GRAINE_COMMANDE_FOURNISSEUR1_idx` (`COMMANDE_FOURNISSEUR_COFO_ID` ASC) VISIBLE,
  INDEX `fk_GRAINE_SERRE1_idx` (`SERRE_SER_ID` ASC) VISIBLE,
  CONSTRAINT `fk_GRAINE_COMMANDE_FOURNISSEUR1`
    FOREIGN KEY (`COMMANDE_FOURNISSEUR_COFO_ID`)
    REFERENCES `LePaysanUrbain`.`COMMANDE_FOURNISSEUR` (`COFO_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_GRAINE_SERRE1`
    FOREIGN KEY (`SERRE_SER_ID`)
    REFERENCES `LePaysanUrbain`.`SERRE` (`SER_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LePaysanUrbain`.`MATERIEL`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LePaysanUrbain`.`MATERIEL` (
  `MAT_ID` INT NOT NULL,
  `MAT_STOCK` INT NULL,
  `MAT_SERRE` VARCHAR(45) NULL,
  `MAT_CONDITIONNEMENT` VARCHAR(45) NULL,
  `COMMANDE_FOURNISSEUR_COFO_ID` INT NOT NULL,
  `SERRE_SER_ID` INT NOT NULL,
  PRIMARY KEY (`MAT_ID`),
  INDEX `fk_MATERIEL_COMMANDE_FOURNISSEUR1_idx` (`COMMANDE_FOURNISSEUR_COFO_ID` ASC) VISIBLE,
  INDEX `fk_MATERIEL_SERRE1_idx` (`SERRE_SER_ID` ASC) VISIBLE,
  CONSTRAINT `fk_MATERIEL_COMMANDE_FOURNISSEUR1`
    FOREIGN KEY (`COMMANDE_FOURNISSEUR_COFO_ID`)
    REFERENCES `LePaysanUrbain`.`COMMANDE_FOURNISSEUR` (`COFO_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_MATERIEL_SERRE1`
    FOREIGN KEY (`SERRE_SER_ID`)
    REFERENCES `LePaysanUrbain`.`SERRE` (`SER_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LePaysanUrbain`.`PRODUIT_FINALS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LePaysanUrbain`.`PRODUIT_FINALS` (
  `PF_ID` INT NOT NULL,
  `PF_NOM` VARCHAR(45) NULL,
  `PF_STOCK` INT NULL,
  `PF_PRIXVENTUNIT` INT NULL,
  `PF_DLC` DATETIME NULL,
  `SERRE_SER_ID` INT NOT NULL,
  PRIMARY KEY (`PF_ID`),
  INDEX `fk_PRODUIT_FINALS_SERRE1_idx` (`SERRE_SER_ID` ASC) VISIBLE,
  CONSTRAINT `fk_PRODUIT_FINALS_SERRE1`
    FOREIGN KEY (`SERRE_SER_ID`)
    REFERENCES `LePaysanUrbain`.`SERRE` (`SER_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LePaysanUrbain`.`CLIENT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LePaysanUrbain`.`CLIENT` (
  `CL_ID` INT NOT NULL,
  `CL_NOM` VARCHAR(45) NULL,
  `CL_PRENOM` VARCHAR(45) NULL,
  `CL_ADRESSE` VARCHAR(45) NULL,
  `CL_TEL` INT NULL,
  `CL_MAIL` VARCHAR(45) NULL,
  PRIMARY KEY (`CL_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LePaysanUrbain`.`LIGNE_COMMANDE_CLIENT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LePaysanUrbain`.`LIGNE_COMMANDE_CLIENT` (
  `LCC_ID` INT NOT NULL,
  `LCC_REFERENCE` INT NULL,
  `LCC_QIUANTITE` INT NULL,
  `LCC_PRIXUNIT` INT NULL,
  `CLIENT_CL_ID` INT NOT NULL,
  `PRODUIT_FINALS_PF_ID` INT NOT NULL,
  PRIMARY KEY (`LCC_ID`),
  INDEX `fk_LIGNE_COMMANDE_CLIENT_CLIENT1_idx` (`CLIENT_CL_ID` ASC) VISIBLE,
  INDEX `fk_LIGNE_COMMANDE_CLIENT_PRODUIT_FINALS1_idx` (`PRODUIT_FINALS_PF_ID` ASC) VISIBLE,
  CONSTRAINT `fk_LIGNE_COMMANDE_CLIENT_CLIENT1`
    FOREIGN KEY (`CLIENT_CL_ID`)
    REFERENCES `LePaysanUrbain`.`CLIENT` (`CL_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_LIGNE_COMMANDE_CLIENT_PRODUIT_FINALS1`
    FOREIGN KEY (`PRODUIT_FINALS_PF_ID`)
    REFERENCES `LePaysanUrbain`.`PRODUIT_FINALS` (`PF_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `LePaysanUrbain`.`COMMANDE_CLIENT`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `LePaysanUrbain`.`COMMANDE_CLIENT` (
  `COC_ID` INT NOT NULL,
  `COC_NUMC` INT NULL,
  `COC_DATEC` DATETIME NULL,
  `COC_COUTC` INT NULL,
  `LIGNE_COMMANDE_CLIENT_LCC_ID` INT NOT NULL,
  PRIMARY KEY (`COC_ID`),
  INDEX `fk_COMMANDE_CLIENT_LIGNE_COMMANDE_CLIENT1_idx` (`LIGNE_COMMANDE_CLIENT_LCC_ID` ASC) VISIBLE,
  CONSTRAINT `fk_COMMANDE_CLIENT_LIGNE_COMMANDE_CLIENT1`
    FOREIGN KEY (`LIGNE_COMMANDE_CLIENT_LCC_ID`)
    REFERENCES `LePaysanUrbain`.`LIGNE_COMMANDE_CLIENT` (`LCC_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;