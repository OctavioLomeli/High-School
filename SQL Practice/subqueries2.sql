-- What is the lifetime average amount spentin terms of total_amt_usd for the top 10 total spending accounts?
SELECT ROUND(AVG(sum), 2)
FROM (
		SELECT o.account_id, SUM(o.total_amt_usd)
		FROM orders o
		GROUP BY 1
		ORDER BY 2 DESC
		LIMIT 10
	)sub
	
