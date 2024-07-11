-- script that creates a trigger that decreases quantity of items after
-- adding a new order

CREATE TRIGGER decrease_after_order AFTER INSERT on orders
FOR EACH ROW
  UPDATE items
  SET quantity = quantity - NEW.number
  WHERE name = NEW.item_name;
