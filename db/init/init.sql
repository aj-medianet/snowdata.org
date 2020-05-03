/* drop tables in reverse order so fk constraints dont break it first */
DROP TABLE IF EXISTS avg_temps;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS monthly_data;
DROP TABLE IF EXISTS ski_areas;


CREATE TABLE ski_areas (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `cur_temp` varchar(255),
  `cur_depth` varchar(255),
  `ytd` varchar(255),
  `wind_dir` varchar(255),
  `wind_speed` varchar(255),
  `new_snow_12` varchar(255),
  `new_snow_24` varchar(255),
  `new_snow_48` varchar(255),
  `ts` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY (`name`)
) ENGINE=InnoDB;

INSERT INTO ski_areas VALUES 
(1, "Alpental", "", "", "", "", "", "", "", "", curdate()),
(2, "Big Sky", "", "", "", "", "", "", "", "", curdate()),
(3, "Bridger Bowl", "", "", "", "", "", "", "", "", curdate()),
(4, "Jackson Hole", "", "", "", "", "", "", "", "", curdate()),
(5, "Mt Bachelor", "", "", "", "", "", "", "", "", curdate()),
(6, "Mt Hood", "", "", "", "", "", "", "", "", curdate()),
(7, "49 Degrees North", "", "", "", "", "", "", "", "", curdate()),
(8, "Snowbird", "", "", "", "", "", "", "", "", curdate()),
(9, "Whitefish", "", "", "", "", "", "", "", "", curdate());

CREATE TABLE monthly_data (
    `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `month` varchar(255) NOT NULL,
    `year` varchar(255) NOT NULL,
    `ski_area_name` varchar(255) NOT NULL,
    `total_new_snow` varchar(255) NOT NULL,
    `snow_depth` varchar(255) NOT NULL,
    `avg_temp` varchar(255) NOT NULL,
    `ytd` varchar(255),
    CONSTRAINT `ski_area_fk1` FOREIGN KEY (`ski_area_name`) REFERENCES ski_areas(`name`) 
      ON DELETE CASCADE 
      ON UPDATE CASCADE,
    KEY `ski_area_name` (`ski_area_name`)
) ENGINE=InnoDB;

INSERT INTO monthly_data VALUES 
(1, MONTH(curdate()), YEAR(CURDATE()), "Alpental", "0", "0", "0", "0"),
(2, MONTH(curdate()), YEAR(CURDATE()), "Big Sky", "0", "0", "0", "0"),
(3, MONTH(curdate()), YEAR(CURDATE()), "Bridger Bowl", "0", "0", "0", "0"),
(4, MONTH(curdate()), YEAR(CURDATE()), "Jackson Hole", "0", "0", "0", "0"),
(5, MONTH(curdate()), YEAR(CURDATE()), "Mt Bachelor", "0", "0", "0", "0"),
(6, MONTH(curdate()), YEAR(CURDATE()), "Mt Hood", "0", "0", "0", "0"),
(7, MONTH(curdate()), YEAR(CURDATE()), "49 Degrees North", "0", "0", "0", "0"),
(8, MONTH(curdate()), YEAR(CURDATE()), "Snowbird", "0", "0", "0", "0"),
(9, MONTH(curdate()), YEAR(CURDATE()), "Whitefish", "0", "0", "0", "0");


CREATE TABLE users (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password`varchar(255) NOT NULL,
  `api_key` varchar(255) NOT NULL,
  `api_count` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB;

INSERT INTO users VALUES (1, "aj", "josephan@oregonstate.edu", "tmpadmin", "tmpkey", 0);


CREATE TABLE avg_temps (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ski_area_name` varchar(255) NOT NULL,
  `avg_temp` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ski_area_name` (`ski_area_name`)
) ENGINE=InnoDB;

INSERT INTO avg_temps VALUES 
(1, "Alpental", "0"),
(2, "Big Sky", "0"),
(3, "Bridger Bowl", "0"),
(4, "Jackson Hole", "0"),
(5, "Mt Bachelor", "0"),
(6, "Mt Hood", "0"),
(7, "49 Degrees North", "0"),
(8, "Snowbird", "0"),
(9, "Whitefish", "0");