
create table IF NOT EXISTS title
(
	tconst integer PRIMARY KEY NOT NULL,
	titleType	varchar(20),
	primaryTitle varchar(500),	
	originalTitle varchar(500),
	isAdult integer,
	startYear integer,
	endYear integer,
	runtimeMinutes integer
	--genres text[]
);

create table IF NOT EXISTS ratings
(
	tconst integer,	
	averageRating float,
	numVotes integer,
	 CONSTRAINT tconst
      FOREIGN KEY(tconst) 
	  REFERENCES title(tconst)
);

create table IF NOT EXISTS genre_title
(
	tconst integer,
	genre_tconst integer
	
);
Alter table genre_title ADD FOREIGN KEY(TCONST) REFERENCES TITLE(TCONST);

Alter table genre_title ADD FOREIGN KEY(GENRE_TCONST) REFERENCES GENRE(GENRE_TCONST);

Alter table genre_title ADD PRIMARY KEY(GENRE_TCONST, TCONST) ;

create table IF NOT EXISTS genre
(
	genre_tconst integer PRIMARY KEY,
	genre varchar(15)
	
)

create table IF NOT EXISTS episode
(
	tconst integer PRIMARY KEY,
	parentTconst integer ,
	seasonNumber integer,
	episodeNumber integer,
	FOREIGN KEY(PARENTTCONST) REFERENCES TITLE(TCONST)
	
);

create table IF NOT EXISTS akas
(
titleId integer ,
ordering integer,
title varchar(50),
region varchar(20),
language varchar(20),
types varchar(20),
attibutes varchar(20),
isOriginalTitle integer,
PRIMARY KEY (titleId, ordering)

);
Alter table akas ADD FOREIGN KEY(titleId) REFERENCES TITLE(TCONST);
Alter table akas rename attibutes to attributes;
alter table akas alter column isoriginaltitle type boolean USING isoriginaltitle::boolean;

--For testing:
select * from akas join title on akas.titleid = title.tconst

create table IF NOT EXISTS principals
(
	tconst integer,	
	ordering integer,
	nconst integer,
	category varchar(20),
	job text,
	characters text,
	 CONSTRAINT tconst
     FOREIGN KEY(tconst) 
	 REFERENCES title(tconst),
	 PRIMARY KEY(tconst,ordering)
)

create table IF NOT EXISTS people
(
	nconst integer PRIMARY KEY,	
	primaryName text,
	birthYear integer,
	deathYear integer,
	primaryProfession text,
	knownForTitles text[]
	
)
Alter table PRINCIPALS ADD FOREIGN KEY(NCONST) REFERENCES PEOPLE(NCONST);

create table IF NOT EXISTS director_title_mapping
(
	tconst integer,	
	directorId integer,
	PRIMARY KEY(tconst,directorId),
	CONSTRAINT tconst FOREIGN KEY(tconst) REFERENCES title(tconst)
	
	
)

create table IF NOT EXISTS writer_title_mapping
(
	tconst integer,	
	writerId integer,
	PRIMARY KEY(tconst,writerId),
	CONSTRAINT tconst FOREIGN KEY(tconst) REFERENCES title(tconst)
	
	
)
Alter table director_title_mapping ADD FOREIGN KEY(directorId) REFERENCES PEOPLE(NCONST);
Alter table writer_title_mapping ADD FOREIGN KEY(directorId) REFERENCES PEOPLE(NCONST);


