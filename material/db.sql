
-- -----------------------------------------------------
-- Table `mydb`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `User` (
  `id` VARCHAR(32) NOT NULL,
  `login` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `surname` VARCHAR(45) NOT NULL,
  `default_account` VARCHAR(32) NULL,
  `password_type` VARCHAR(32) NULL,
  `state` CHAR(1) NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `mydb`.`AcountType`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `AcountType` (
  `id` VARCHAR(32) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `type` VARCHAR(15) NOT NULL,
  `module` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `mydb`.`AccountGroup`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `AccountGroup` (
  `id` VARCHAR(32) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `mydb`.`Currency`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Currency` (
  `id` VARCHAR(32) NOT NULL,
  `denomination` VARCHAR(3) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `bid` FLOAT NULL,
  `ask` FLOAT NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `mydb`.`Account`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Account` (
  `id` VARCHAR(32) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `parent` VARCHAR(32) NULL,
  `id_account_type` VARCHAR(32) NOT NULL,
  `id_currency` VARCHAR(32) NOT NULL,
  `id_account_group` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `mydb`.`Category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Category` (
  `id` VARCHAR(32) NOT NULL,
  `parent` VARCHAR(32) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `mydb`.`transaction`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `transaction` (
  `id` VARCHAR(32) NOT NULL,
  `origin` VARCHAR(32) NOT NULL,
  `destiny` VARCHAR(32) NOT NULL,
  `id_category` VARCHAR(32) NOT NULL,
  `number` VARCHAR(45) NOT NULL,
  `id_instrument` VARCHAR(32) NOT NULL,
  `transaction_member` VARCHAR(32) NULL,
  `notes` BLOB NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `mydb`.`CurrencyHistory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `CurrencyHistory` (
  `id` INT NOT NULL,
  `id_currency` VARCHAR(32) NOT NULL,
  `date` DATE NULL,
  `bid` FLOAT NULL,
  `ask` FLOAT NULL,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `mydb`.`Instrument`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Instrument` (
  `id` VARCHAR(32) NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `denomination` VARCHAR(45) NULL,
  `notes` VARCHAR(200) NULL,
  `id_currency` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`id`));
