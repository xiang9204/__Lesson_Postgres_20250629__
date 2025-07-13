ALTER TABLE "台鐵車站資訊"
	ADD PRIMARY KEY ("stationCode");

ALTER TABLE "每日各站進出站人數"
	RENAME COLUMN "trnOpDate" TO "日期";

ALTER TABLE "每日各站進出站人數"
	RENAME COLUMN "staCode" TO "車站代碼";

ALTER TABLE "每日各站進出站人數"
	RENAME COLUMN "gateInComingCnt" TO "進站人數";

ALTER TABLE "每日各站進出站人數"
	RENAME COLUMN "gateOutGoingCnt" TO "出站人數";

-- 匯入資料時，如果日期要修改資料型別，則需在匯入時就先修改。


