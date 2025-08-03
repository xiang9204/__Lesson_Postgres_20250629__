SELECT count(*) AS "總筆數"
FROM "台鐵車站資訊";

SELECT count(name) AS "台北車站數"
FROM "台鐵車站資訊"
WHERE "stationAddrTw"  LIKE '%臺北%';

/*
* 全省各站點 2022 年進站總人數
*/

SELECT "name" AS 站名, COUNT("name") AS 筆數, avg("進站人數") AS 進站人數
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "日期" BETWEEN '2022-01-01' AND '20222-01-31'
GROUP BY "name";

-- select 內有定義的項目，必定要在 GROUP BY 內做排組。

SELECT "name" AS 站名, date_part('year',"日期")AS 年份, COUNT("name") AS 筆數, avg("進站人數") AS 進站人數
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
GROUP BY "name","年份";


SELECT "name" AS 站名, date_part('year',"日期")AS 年份, COUNT("name") AS 筆數, avg("進站人數") AS 進站人數
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE "name" LIKE '%基隆'
GROUP BY "name","年份"
ORDER BY "進站人數" DESC;



/*
 * 全省各站點 2022 年進站總人數大於 5 佰萬人的站點
 */
-- Having 後面必須要有聚合函數
SELECT "name" AS 站名, sum("進站人數") AS "2022進站總人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE date_part('year',"日期") = 2022
GROUP BY "name"
HAVING sum("進站人數") > 5000000
ORDER BY "2022進站總人數" DESC;

/*
 * 全省各站點 2022 年進站總人數大於 5 佰萬人的站點
 */

SELECT "name" AS 站名, sum("進站人數") AS "2022進站總人數"
FROM "每日各站進出站人數" LEFT JOIN "台鐵車站資訊" ON "車站代碼" = "stationCode"
WHERE date_part('year',"日期") = 2022
GROUP BY "name"
HAVING sum("進站人數") > 5000000
ORDER BY "2022進站總人數" DESC;

/*
 * 基隆火車站 2022, 2021, 2022, 每年進站人數
 */
SELECT t."name" AS 站名, date_part('year', d."日期") AS 年份, SUM(d."進站人數") AS 每年進站人數
FROM "每日各站進出站人數" d
LEFT JOIN "台鐵車站資訊" t ON d."車站代碼" = t."stationCode"
WHERE t."name" = '基隆'
  AND date_part('year', d."日期") IN (2020, 2021, 2022)
GROUP BY 站名,年份
ORDER BY 年份;

/*
 * 基隆火車站, 臺北火車站 2020, 2021, 2022, 每年進站人數
 */
SELECT t."name" AS 站名, date_part('year', d."日期") AS 年份, SUM(d."進站人數") AS 每年進站人數
FROM "每日各站進出站人數" d
LEFT JOIN "台鐵車站資訊" t ON d."車站代碼" = t."stationCode"
WHERE t."name" IN ('基隆', '臺北')
  AND date_part('year', d."日期") IN (2020, 2021, 2022)
GROUP BY t."name", 年份
ORDER BY t."name", 年份;

/*
 * 查詢 2022 年平均每日進站人數超過 2 萬人的站點
 */
 
SELECT t."name" AS 站名,date_part('year',d.日期)AS 年份, AVG(d."進站人數")::NUMERIC(10,1) AS 平均每日進站人數
FROM "每日各站進出站人數" d
LEFT JOIN "台鐵車站資訊" t ON d."車站代碼" = t."stationCode"
WHERE date_part('year', d."日期") = 2022
GROUP BY t."name", 年份
HAVING AVG(d."進站人數") > 20000
ORDER BY 平均每日進站人數 DESC;



