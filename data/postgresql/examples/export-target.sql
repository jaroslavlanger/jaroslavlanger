COPY "student"      TO '/var/lib/postgresql/target/student.csv'      DELIMITER ',' CSV HEADER;
COPY "student_logs" TO '/var/lib/postgresql/target/student_logs.csv' DELIMITER ',' CSV HEADER;
COPY "session"      TO '/var/lib/postgresql/target/session.csv'      DELIMITER ',' CSV HEADER;
COPY "final_exam"   TO '/var/lib/postgresql/target/final_exam.csv'   DELIMITER ',' CSV HEADER;
COPY "inter_exam"   TO '/var/lib/postgresql/target/inter_exam.csv'   DELIMITER ',' CSV HEADER;
COPY "grade"        TO '/var/lib/postgresql/target/grade.csv'        DELIMITER ',' CSV HEADER;
COPY "log"          TO '/var/lib/postgresql/target/log.csv'          DELIMITER ',' CSV HEADER;
COPY "exercise"     TO '/var/lib/postgresql/target/exercise.csv'     DELIMITER ',' CSV HEADER;
