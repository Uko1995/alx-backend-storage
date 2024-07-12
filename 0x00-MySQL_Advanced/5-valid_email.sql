-- script that creates a trigger that resets valid_email when email has been changed
DELIMITER &


CREATE TRIGGER reset_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email != OLD.email THEN
    SET NEW.valid_email = 0;
  ELSE
    SET NEW.valid_email = 1;
  END IF;
END;
&

DELIMITER ;
