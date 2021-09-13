/*****  URL: https://www.hackerrank.com/challenges/print-prime-numbers/problem *****/
CREATE TABLE #PN
(num INT, dummy int);

DECLARE @start INT = 2, @i INT = 2, @end INT = 1000;
    WHILE (@i <= @end) BEGIN
        DECLARE @deno INT = 2, @flag INT = 1;
        WHILE (@deno < @i) BEGIN
            --select 'i=',@i,'d=',@deno,'mod=',(@i% @deno);
            IF (@i% @deno) = 0  SET @flag = 0;
            SET @deno = @deno+1;
        END
        IF @flag = 1  INSERT INTO #PN VALUES(@i,0);
    SET @i = @i+1;
    END

select STRING_AGG(num,'&') from #PN
GROUP BY dummy;
DROP TABLE #PN;