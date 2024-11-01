
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


----------------------------------------------
with subquery:
SELECT
    (SELECT count(tripnum)
     FROM rdm01.ods_ssam_lnt_exceptions AS sub
     WHERE extract(day from sub.STARTDATE) = extract(day from main.STARTDATE)
    ) as exceptions_by_day,
    main.tripnum,
    main.depotcode,
    main.transporter,
    main.vehiclereg,
    main.startdate,
    main.stopdate,
    main.avg_percent,
    main.loaddate,
    main.total_trip_time,
    main.total_distance
FROM
    rdm01.ods_ssam_lnt_exceptions AS main;
