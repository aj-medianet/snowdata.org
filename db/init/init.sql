/* drop tables in reverse order so fk constraints dont break it first */
DROP TABLE IF EXISTS api_keys;
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

INSERT INTO ski_areas VALUES (1, "Mt Bachelor", "", "", "", "", "", "", "", "", curdate());
/*,(2, "Jackson Hole", "", "", "", "", "", "", "", "",""),(3, "Mt Bachelor", "", "", "", "", "", "", "", "",""),(4, "Alta", "", "", "", "", "", "", "", "",""),(5, "Aspen", "", "", "", "", "", "", "", "","");
*/

CREATE TABLE monthly_data (
    `id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `month` varchar(255) NOT NULL,
    `year` varchar(255) NOT NULL,
    `ski_area_name` varchar(255) NOT NULL,
    `total_new_snow` varchar(255) NOT NULL,
    `snow_depth` varchar(255) NOT NULL,
    `avg_temp` varchar(255) NOT NULL,
    CONSTRAINT `ski_area_fk1` FOREIGN KEY (`ski_area_name`) REFERENCES ski_areas(`name`) 
      ON DELETE CASCADE 
      ON UPDATE CASCADE,
    KEY `ski_area_name` (`ski_area_name`)
) ENGINE=InnoDB;

INSERT INTO monthly_data VALUES (1, MONTH(curdate()), YEAR(CURDATE()), "Mt Bachelor", "10", "100", "32");

CREATE TABLE users (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pwd`varchar(255) NOT NULL,
  `api_key` varchar(255) NOT NULL,
  `api_count` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB;

INSERT INTO users VALUES (1, "aj", "josephan@oregonstate.edu", "tmpadmin", "tmpkey", 0);

