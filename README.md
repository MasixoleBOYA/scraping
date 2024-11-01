
select
	count(tripnum) over(partition by extract(day from STARTDATE)) as exceptions_by_day,
--	sum(distinct exceptions_by_day) over(partition by extract(month from STARTDATE)),
--	sum(distinct exceptions_by_day) over(partition by extract(month from STARTDATE)),
	tripnum,
	depotcode,
	transporter,
	vehiclereg,
	startdate,
	stopdate,
	avg_percent,
	loaddate,
	total_trip_time,
	total_distance
from
	rdm01.ods_ssam_lnt_exceptions
