DROP TABLE IF EXISTS ski_area;
DROP TABLE IF EXISTS users;

CREATE TABLE ski_area (
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB;

INSERT INTO ski_area VALUES (1, "Snowbird", "", "", "", "", "", "", "", "");
INSERT INTO ski_area VALUES (2, "Jackson Hole", "", "", "", "", "", "", "", "");
INSERT INTO ski_area VALUES (3, "Mt Bachelor", "", "", "", "", "", "", "", "");
INSERT INTO ski_area VALUES (4, "Alta", "", "", "", "", "", "", "", "");
INSERT INTO ski_area VALUES (5, "Aspen", "", "", "", "", "", "", "", "");


CREATE TABLE users (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password`varchar(255) NOT NULL,
  `api_key` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB;


/* TODO create monthly totals and averages with ski area name as foreign key*/
CREATE TABLE monthly_data (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ski_area_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ski_area_name` (`ski_area_name`)
) ENGINE=InnoDB;