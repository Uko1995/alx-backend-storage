-- script that creates an index idx_name_first on names table
-- with the first letter of name amd score

CREATE INDEX idx_name_first_score ON names(name(1), score);
