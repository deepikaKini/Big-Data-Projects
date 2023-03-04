create table final_norm_grouped as
SELECT title.id,title.type,title.startYear, title.runtime, title.avgrating, genre.id as genre_id, genre.genre, atc.actor, member.birthyear, character.character 
from atc 
join character on atc.character = character.id
join actor on actor.actor = atc.actor
join title on actor.title = title.id and title.id = atc.title 
join title_genre on title.id = title_genre.title
join genre on title_genre.genre = genre.id
join member on actor.actor = member.id
where title.runtime>=90
and concat(title.id,member.id)  not in (select concat(title, actor) in 
from atc
group by title, actor
having count(character) >1);

select * from final_norm_grouped

ALTER TABLE final_norm_grouped ADD column primary_key varchar(50);
update final_norm_grouped set primary_key = concat(id , genre_id,actor);
ALTER TABLE final_norm_grouped ADD PRIMARY KEY (primary_key);