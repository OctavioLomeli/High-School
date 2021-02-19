/*
How can you produce a list of bookings on the day of 2012-09-14 which will cost the member (or guest)
more than $30? Remember that guests have different costs to members (the listed costs are per half-hour
'slot'), and the guest user is always ID 0. Include in your output the name of the facility, the name of
the member formatted as a single column, and the cost. Order by descending cost.
*/

SELECT member, facility, cost
	FROM (
	 	SELECT  (mem.firstname || ' ' || mem.surname) AS member,
            fac.name AS facility,
            book.starttime,
            CASE
		            WHEN mem.memid = 0 THEN book.slots * fac.guestcost
                ELSE book.slots * fac.membercost
            END AS cost
      
		FROM public.facilities fac
			JOIN public.bookings book ON book.facid = fac.facid
			JOIN public.members mem ON mem.memid = book.memid
	  )sub
	
	WHERE DATE_TRUNC('day', sub.starttime) = '2012-09-14' AND cost > 30
ORDER BY 3 DESC

