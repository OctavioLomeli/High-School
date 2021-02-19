/*
How can you produce a list of all members who have used a tennis court? 
Include in your output the name of the court, and the name of the member
formatted as a single column. Ensure no duplicate data, and order by the
member name followed by the facility name.
*/

SELECT DISTINCT (m.firstname || ' ' || m.surname) AS name, f.name AS facility
FROM public.facilities f
	JOIN public.bookings b ON b.facid = f.facid
	JOIN public.members m ON m.memid = b.memid
WHERE f.name LIKE '%Tennis Court%'
ORDER BY 1, 2
