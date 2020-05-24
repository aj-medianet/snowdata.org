/* drop tables in reverse order so fk constraints dont break it first */
DROP TABLE IF EXISTS websites;
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
(10, 4, 2020, "Alpental", "5", "10", "20", "70"),
(11, 4, 2020, "Big Sky", "5", "10", "20", "70"),
(12, 4, 2020, "Bridger Bowl", "5", "10", "20", "70"),
(13, 4, 2020, "Jackson Hole", "5", "10", "20", "70"),
(14, 4, 2020, "Mt Bachelor", "5", "10", "20", "70"),
(15, 4, 2020, "Mt Hood", "5", "10", "20", "70"),
(16, 4, 2020, "49 Degrees North", "5", "10", "20", "70"),
(17, 4, 2020, "Snowbird", "5", "10", "20", "70"),
(18, 4, 2020, "Whitefish", "5", "10", "20", "70"),
(19, 3, 2020, "Alpental", "5", "10", "20", "60"),
(20, 3, 2020, "Big Sky", "5", "10", "20", "60"),
(21, 3, 2020, "Bridger Bowl", "5", "10", "20", "60"),
(22, 3, 2020, "Jackson Hole", "5", "10", "20", "60"),
(23, 3, 2020, "Mt Bachelor", "5", "10", "20", "60"),
(24, 3, 2020, "Mt Hood", "5", "10", "20", "60"),
(25, 3, 2020, "49 Degrees North", "5", "10", "20", "60"),
(26, 3, 2020, "Snowbird", "5", "10", "20", "60"),
(27, 3, 2020, "Whitefish", "5", "10", "20", "60");


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
  `total_temp` varchar(255) NOT NULL,
  `count` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ski_area_name` (`ski_area_name`)
) ENGINE=InnoDB;

INSERT INTO avg_temps VALUES 
(1, "Alpental", "0", "0", 0),
(2, "Big Sky", "0","0", 0),
(3, "Bridger Bowl","0", "0", 0),
(4, "Jackson Hole","0", "0", 0),
(5, "Mt Bachelor", "0","0", 0),
(6, "Mt Hood", "0","0", 0),
(7, "49 Degrees North", "0","0", 0),
(8, "Snowbird", "0","0", 0),
(9, "Whitefish", "0","0", 0);


CREATE TABLE websites (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ski_area_name` varchar(255) NOT NULL,
  `content` TEXT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB;

INSERT INTO websites VALUES
(1, "Alpental", ""),
(2, "Big Sky", ""),
(3, "Bridger Bowl",""),
(4, "Jackson Hole",""),
(5, "Mt Bachelor", ""),
(6, "Mt Hood", ""),
(7, "49 Degrees North", ""),
(8, "Snowbird", ""),
(9, "Whitefish", "");