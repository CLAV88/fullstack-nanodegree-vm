CREATE VIEW http_errors_per_day AS (
SELECT time AS datelog, count(*) AS numerrors 
FROM log 
WHERE left(log.status,3) > 400 
GROUP BY datelog)
GO

CREATE VIEW http_errors_per_day AS (
select time as datelog, count(*) as numhttprequests 
from log 
group by datelog)
GO