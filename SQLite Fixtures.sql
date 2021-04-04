INSERT INTO b_item (id, name)
VALUES  (1, 'ITEM B 1'),
        (2, 'ITEM B 2');

INSERT INTO a_item (id, name, b_item_id)
VALUES  (1, 'ITEM A 1', 1),
        (2, 'ITEM A 2', 2),
        (3, 'ITEM A 3', 2);

INSERT INTO c_item (id, name)
VALUES  (1, 'ITEM C 1'),
        (2, 'ITEM C 2');

-- M2M RELATIONSHIP
INSERT INTO a_item_to_c_item (a_item_id, c_item_id)
VALUES  (1, 1),
        (2, 1),
        (3, 2);
