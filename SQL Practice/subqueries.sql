/*
What is the lifetime average amount spent in terms of total_amt_usd,
including only the companies that spent more per order, on average, than the average of all orders.
*/
SELECT ROUND(AVG(round), 2) average
FROM (
	SELECT o.account_id, ROUND(AVG(o.total_amt_usd), 2)
	FROM public.orders o
		GROUP BY 1
		HAVING ROUND(AVG(o.total_amt_usd), 2) >	(
													SELECT ROUND(AVG(o.total_amt_usd), 2)
													FROM public.orders o
												) -- This is the average amount spent
	)sub
  
/*
  This also works
  WITH average_higher_than_rest AS (
    SELECT o.account_id, ROUND(AVG(o.total_amt_usd), 2)
    FROM public.orders o
      GROUP BY 1
      HAVING ROUND(AVG(o.total_amt_usd), 2) >	(
                            SELECT ROUND(AVG(o.total_amt_usd), 2)
                            FROM public.orders o
                          ) -- This is the average amount spent
  )

  SELECT ROUND(AVG(round), 2) average
  FROM average_higher_than_rest
*/
