INSERT INTO "main"."Logs" ("TimeStamp", "TrackerID", "Value", "Note") VALUES ('2022-05-26T11:42:00.73+05:30', 'tracker1', '98.3', 'I was feeling okay');

DROP TABLE Logs;

CREATE TABLE "Logs" (
	"TimeStamp"	TEXT,
	"TrackerID"	TEXT,
	"Value"	TEXT,
	"Note"	TEXT,
	PRIMARY KEY("TimeStamp"),
	CONSTRAINT "FK_LogsTracker" FOREIGN KEY("TrackerID") REFERENCES "Tracker"("ID")
)