/*
Retrieve the sales rep that has the highest sales for each region
*/
WITH rep_and_sales AS (
	SELECT s.name, r.name region, SUM(o.total_amt_usd) sales
	FROM public.accounts a
		JOIN public.orders o ON o.account_id = a.id
		JOIN public.sales_reps s ON s.id = a.sales_rep_id
		JOIN public.region r ON r.id = s.region_id
	GROUP BY 1, 2)

SELECT name, region, sales
FROM rep_and_sales
	WHERE sales IN (SELECT max
			FROM
			    (SELECT region, MAX(sales)
			     FROM rep_and_sales
				GROUP BY 1)sub2)
