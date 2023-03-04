--Number of invalid Title_Actor relationships with respect to characters. (That is, entries in Title_Actor which do not appear in Actor_Title_Character.)
select title, actor from title_actor where concat(title, actor) not in (select concat(title, actor) from atc )


--Alive actors whose name starts with “Phi” and did not participate in any title in 2014.
select m.name, t.title, t.startYear from title_actor a 
inner join member m on a.actor = m.id
inner join title t on a.title = t.id
where m.deathYear = 0 and t.startYear != 2014 and endYear != 2014
and lower(m.name) like 'phi%'

--   Producers who have produced the most talk shows in 2017 and whose name contains “Gill”. (Hint: talk show is a genre)
select m.name, count(t.id) from member m
join title_producer p on m.id = p.producer
join title t on t.id = p.title
join title_genre tg on tg.title = t.id
join genre g on tg.genre = g.id
where m.name like '%gill%' and t.startYear = 2017 and lower(g.genre) like '%talk-show%'
group by m.name
order by count(t.id) desc

select m.name, count(t.title)
from title_producer p 
join member m on p.producer = m.id
join title t on t.id = p.title
where t.runtime > 120 and m.deathYear != 0
group by m.name
order by count(t.title) desc


		
-- Alive actors who have portrayed Jesus Christ (simply look for a character with this specific name)
explain select distinct(m.name) from member m
-- join title_actor ta on ta.actor = m.id
join atc atc on atc.actor = m.id
join character c on c.id = atc.character
where lower(c.character) like '%jesus christ%' and m.deathYear != 0
		
	
	--index
create index q2 on member(name)

create index q3 on title(id, endYear, startYear)

create index q4 on genre(genre)

create index  q5 on title_actor(title, actor)

create index q6 on character(id, character)
		
		
create index q7 on actor_title_character(actor, character)
		
		

																		

																		




