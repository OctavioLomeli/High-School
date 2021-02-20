/*
Retrieve the sales rep that has the highest sales for each region
*/
SELECT s.name, r.name region, SUM(o.total_amt_usd)
FROM public.accounts a
	JOIN public.orders o ON o.account_id = a.id
	JOIN public.sales_reps s ON s.id = a.sales_rep_id
	JOIN public.region r ON r.id = s.region_id
GROUP BY 1, 2
HAVING SUM(o.total_amt_usd) IN (SELECT max
	FROM
		(SELECT region, MAX(sum)
		FROM (
			SELECT s.name, r.name region, SUM(o.total_amt_usd)
			FROM public.accounts a
				JOIN public.orders o ON o.account_id = a.id
				JOIN public.sales_reps s ON s.id = a.sales_rep_id
				JOIN public.region r ON r.id = s.region_id
			GROUP BY 1, 2
			)sub
		GROUP BY 1)sub2)
