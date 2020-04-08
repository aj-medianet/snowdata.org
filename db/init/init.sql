DROP TABLE IF EXISTS ski_area;

CREATE TABLE ski_area (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `cur_temp` int,
  `cur_depth` int,
  `ytd` int,
  `wind_dir` int,
  `wind_speed` int,
  `new_snow_12` int,
  `new_snow_24` int,
  `new_snow_48` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB;

INSERT INTO ski_area VALUES (1, "Snowbird", 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO ski_area VALUES (2, "Jackson Hole", 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO ski_area VALUES (3, "Mt Bachelor", 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO ski_area VALUES (4, "Alta", 0, 0, 0, 0, 0, 0, 0, 0);
INSERT INTO ski_area VALUES (5, "Aspen", 0, 0, 0, 0, 0, 0, 0, 0);