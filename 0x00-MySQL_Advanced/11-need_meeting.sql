-- view that lists all students that have score under 80(strict)
-- and no last meeting or more than 1 month

CREATE VIEW need_meeting AS SELECT name FROM students
WHERE score < 80 AND (last_meeting IS NULL OR DATEDIFF(CURDATE(), last_meeting) < 30);
