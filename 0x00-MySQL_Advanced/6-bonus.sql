-- stored procedure that adds correction for a new student

DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
  declare project_id INT;
  -- check if project_id exists
  SELECT id INTO project_id FROM projects WHERE name = project_name;
  IF project_id IS NULL
  THEN INSERT INTO projects(name) VALUES(project_name);
  END IF;
  SELECT id INTO project_id FROM projects WHERE name = project_name;
  -- add new corrections
  INSERT INTO corrections(user_id, project_id, score) VALUES(user_id, project_id, score);
END //

DELIMITER ;
