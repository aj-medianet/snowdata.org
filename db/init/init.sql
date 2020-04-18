DROP TABLE IF EXISTS ski_areas;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS monthly_data;


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
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB;

INSERT INTO ski_areas VALUES (1, "Snowbird", "", "", "", "", "", "", "", ""),(2, "Jackson Hole", "", "", "", "", "", "", "", ""),(3, "Mt Bachelor", "", "", "", "", "", "", "", ""),(4, "Alta", "", "", "", "", "", "", "", ""),(5, "Aspen", "", "", "", "", "", "", "", "");


CREATE TABLE users (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `pwd`varchar(255) NOT NULL,
  `api_key` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB;


CREATE TABLE api_keys (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `api_key` varchar(255) NOT NULL,
  `count` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `api_key` (`api_key`)
  key `username` (`username`),
  CONSTRAINT `api_keys_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;


/* TODO */
/*
CREATE TABLE monthly_data (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `month` varchar(255) NOT NULL,
  `year` varchar(255) NOT NULL,
  `ski_area` int(11) DEFAULT NULL,
  `total_new_snow` varchar(255) NOT NULL,
  `snow_depth` varchar(255) NOT NULL,
  `avg_temp` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `month` (`month`)
  key `ski_area` (`ski_area`),
  CONSTRAINT `monthly_data_ibfk_1` FOREIGN KEY (`ski_area`) REFERENCES `ski_areas` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB;
*/