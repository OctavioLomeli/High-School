/*
Produce a list of each member name, id, and their first booking after September 1st 2012. Order by member ID.
*/
SELECT mem.surname || ' ' || mem.firstname AS name, mem.memid, MIN(book.starttime) AS first_booking
FROM public.members mem
	JOIN public.bookings book ON book.memid = mem.memid
WHERE DATE_TRUNC('day', book.starttime) >= '2012-09-01'
GROUP BY 1, 2
ORDER BY 2
