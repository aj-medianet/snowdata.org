DROP TABLE IF EXISTS ski_area;

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