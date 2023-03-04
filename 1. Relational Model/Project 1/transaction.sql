BEGIN;
SAVEPOINT my_savepoint;
   INSERT INTO episode(tconst, parenttconst, seasonnumber, episodenumber) VALUES (2000, 20, 2, 1);
	INSERT INTO episode(tconst, parenttconst, seasonnumber, episodenumber) VALUES (200000, False, 2, 1);
	INSERT INTO episode(tconst, parenttconst, seasonnumber, episodenumber) VALUES (20000,100, 2, 1);
ROLLBACK TO my_savepoint;
COMMIT;
select * from episode where tconst = 2000