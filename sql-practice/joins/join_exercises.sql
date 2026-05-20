-- 1 Clientes e faturas

select C1.first_name,I1.total
from customer C1
inner join invoice I1
on C1.customer_id=I1.customer_id

--2 — Clientes brasileiros

select C1.first_name,C1.country,I1.total
from Customer C1
inner join invoice I1
on C1.customer_id=I1.customer_id
where C1.country = 'Brazil'

--3 — Faturas acima de 10

select C1.first_name,I1.total
from customer C1
inner join invoice I1
on C1.customer_id=I1.customer_id
where I1.total > 10
order by I1.total desc

--4 — Quantidade de faturas por cliente
--Liste:
--first_name
--quantidade de faturas

select C1.First_name, count(I1.total)
from customer C1
inner join invoice I1
on C1.customer_id=I1.customer_id
group by C1.First_name