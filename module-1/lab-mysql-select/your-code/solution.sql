SELECT a.au_id as AUTHOR_ID, a.au_lname as LAST_NAME, a.au_fname as FIRST_NAME, t.title as TITLE,
pu.pub_name as PUBLISHER
FROM authors as a
left join titleauthor as ta
on ta.au_id= a.au_id
inner join titles t
on ta.title_id = t.title_id
inner join publishers pu
on t.pub_id = pu.pub_id
;

SELECT AUTHOR_ID, LAST_NAME, FIRST_NAME,PUBLISHER, COUNT(TITLE) as TITLE_COUNT
FROM
(SELECT a.au_id as AUTHOR_ID, a.au_lname as LAST_NAME, a.au_fname as FIRST_NAME, t.title as TITLE,
pu.pub_name as PUBLISHER
FROM authors as a
left join titleauthor as ta
on ta.au_id= a.au_id
inner join titles t
on ta.title_id = t.title_id
inner join publishers pu
on t.pub_id = pu.pub_id) as result
GROUP BY AUTHOR_ID, PUBLISHER
;


SELECT au.au_id as AUTHOR_ID, au.au_lname as LAST_NAME, au.au_fname as FIRST_NAME, sum(s.qty) as TOTAL
FROM authors au
inner join titleauthor as ta
on au.au_id = ta.au_id
inner join sales as s
on ta.title_id = s.title_id
group by AUTHOR_ID
order by TOTAL desc
limit 3 
;

select au.au_id as AUTHOR_ID, au.au_lname as LAST_NAME, au.au_fname as FIRST_NAME, COALESCE(sum(s.qty),0) as TOTAL
from authors au
left join titleauthor as ta
on au.au_id = ta.au_id
left join sales as s
on ta.title_id = s.title_id
group by AUTHOR_ID
order by TOTAL desc
;

#BONUS
SELECT new.AUTHOR_ID, new.TITLE_ID, COALESCE(sum(PROFIT+TITLE_ADVANCE),0) as ACUMULATE
FROM
(select ta.title_id as TITLE_ID, ta.au_id as AUTHOR_ID, ta.royaltyper as ROYAL_TYPER, t.price as PRICE, t.royalty as ROYALTY, 
s.qty as QTY, (t.price * s.qty * t.royalty / 100) * (ta.royaltyper / 100) as PROFIT, t.advance as TITLE_ADVANCE
from titleauthor ta
left join titles as t
on ta.title_id = t.title_id
left join sales as s
on s.title_id = t.title_id) as new
GROUP BY AUTHOR_ID, TITLE_ID
;

