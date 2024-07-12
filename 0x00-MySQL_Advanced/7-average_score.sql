-- stored procedure that computes the average score of student

DELIMITER //

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

CREATE PROCEDURE IF NOT EXISTS ComputeAverageScoreForUser(IN user_id INT)
BEGIN
  DECLARE total_score INT;
  DECLARE total_projects INT;

  -- total score
  SET total_score = (SELECT SUM(score) FROM corrections WHERE corrections.user_id = user_id);
  -- total projects
  SET total_projects = (SELECT COUNT(project_id) FROM corrections WHERE corrections.project_id = user_id);
  UPDATE users
  SET average_score = IF(total_projects > 0, total_score / total_projects, 0)
  WHERE id = user_id;
END //

DELIMITER ;
