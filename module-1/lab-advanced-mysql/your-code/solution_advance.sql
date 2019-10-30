select ta.title_id as TITLE_ID, ta.au_id as AUTHOR_ID, ta.royaltyper as ROYAL_TYPER, t.price as PRICE, t.royalty as ROYALTY, 
s.qty as QTY, (t.price * s.qty * t.royalty / 100) * (ta.royaltyper / 100) as PROFIT
from titleauthor ta
inner join titles as t
on ta.title_id = t.title_id
inner join sales as s
on s.title_id = t.title_id
;


SELECT new.AUTHOR_ID, new.TITLE_ID, COALESCE(sum(PROFIT),0) as ACUMULATE
FROM
(select ta.title_id as TITLE_ID, ta.au_id as AUTHOR_ID, ta.royaltyper as ROYAL_TYPER, t.price as PRICE, t.royalty as ROYALTY, 
s.qty as QTY, (t.price * s.qty * t.royalty / 100) * (ta.royaltyper / 100) as PROFIT
from titleauthor ta
left join titles as t
on ta.title_id = t.title_id
left join sales as s
on s.title_id = t.title_id) as new
GROUP BY AUTHOR_ID, TITLE_ID
;


create temporary table M_PROFIT_AUTHORS
select ta.title_id as TITLE_ID, ta.au_id as AUTHOR_ID, ta.royaltyper as ROYAL_TYPER, t.price as PRICE, t.royalty as ROYALTY, 
s.qty as QTY, (t.price * s.qty * t.royalty / 100) * (ta.royaltyper / 100) as PROFIT
from titleauthor ta
inner join titles as t
on ta.title_id = t.title_id
inner join sales as s
on s.title_id = t.title_id
;


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