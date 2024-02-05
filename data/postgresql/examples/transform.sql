/* TODO
 * Think about the visualizations before working on something 
 * Add type to exercise and duration q exercises / q sessions
 */
 /*
-- EXAM BEGIN
delete from exam ;
alter table exam add column category varchar(20) ;
insert into exam values (1, false, null, 1,    1, 1, '1000-01-01', '2999-01-01', '2023-05-23', 'Session 1') ;
insert into exam values (2, false, null, 2,    2, 1, '1000-01-01', '2999-01-01', '2023-05-23', 'Session 2') ;
insert into exam values (3, false, null, 3,    3, 1, '1000-01-01', '2999-01-01', '2023-05-23', 'Session 3') ;
insert into exam values (4, false, null, 4,    4, 1, '1000-01-01', '2999-01-01', '2023-05-23', 'Session 4') ;
insert into exam values (5, false, null, 5,    5, 1, '1000-01-01', '2999-01-01', '2023-05-23', 'Session 5') ;
insert into exam values (6, false, null, 6,    6, 1, '1000-01-01', '2999-01-01', '2023-05-23', 'Session 6') ;
insert into exam values (7, true,  1,    null, 7, 1, '1000-01-01', '2999-01-01', '2023-05-23', 'Term 1') ;
insert into exam values (8, true,  2,    null, 8, 1, '1000-01-01', '2999-01-01', '2023-05-23', 'Term 2') ;

-- EXAM_DIM BEGIN
create table exam_dim as
select id, final as is_final, category, session_id as "session", final_id as final_attempt
from exam
;
-- EXAM_DIM END
-- EXAM END

-- GRADE
delete from grade where student_id = -1 ;
ALTER TABLE grade ADD COLUMN exam_id bigint ;
UPDATE grade SET exam_id = (6 + final_exam_id) WHERE final_exam_id > 0 ;
UPDATE grade SET exam_id = inter_exam_id WHERE inter_exam_id > 0 and inter_exam_id < 7 ;

create table grade_dm as
select student_id, exam_id, max(points) as points
from grade
group by student_id, exam_id
order by student_id
;
-- GRADE END

-- LOG BEGIN
delete from log where student_id = -1 ;
alter table log add column duration interval ;
update log set "start" = ("start" + interval '12 hour') where date_part('hour', "start") = 0 ;
update log set "end" = ("end" + interval '12 hour') where date_part('hour', "end") = 0 ;
update log set duration = ("end" - "start") ;
delete from log where duration < interval '0' ;
-- LOG END

-- EXERCISE BEGIN
delete from exercise where tk = 0 ;
insert into exercise values (30, ' Es_1_all', 31, 1, '1900-01-01', '2199-12-31', '2023-05-23') ;
insert into exercise values (31, ' Es_2_all', 32, 1, '1900-01-01', '2199-12-31', '2023-05-23') ;
insert into exercise values (32, ' Es_3_all', 33, 1, '1900-01-01', '2199-12-31', '2023-05-23') ;
insert into exercise values (33, ' Es_4_all', 34, 1, '1900-01-01', '2199-12-31', '2023-05-23') ;
insert into exercise values (34, ' Es_5_all', 35, 1, '1900-01-01', '2199-12-31', '2023-05-23') ;
insert into exercise values (35, ' Es_6_all', 36, 1, '1900-01-01', '2199-12-31', '2023-05-23') ;
insert into exercise values (36, ' all',      37, 1, '1900-01-01', '2199-12-31', '2023-05-23') ;

create table exercise_dim as
select id
    , name
    , NULLIF(substring(name from ' Es_(\d)'), '')::int as intended_session
    , NULLIF(substring(name from ' Es_\d_(\d)'), '')::int as serial_number
from exercise
;
-- EXERCISE END

alter table log add column intended_session bigint ;

update log as l
set intended_session = e.intended_session
from exercise_dim as e
where l.exercise_id = e.id
;

-- ACTIVITY BEGIN
create table activity as
select row_number() over () as id, t.student_id, t.session_id, t.intended_session, t.name, sum(t.duration) as duration
from (
    select *
    from log
    join exercise on log.exercise_id = exercise.id
) as t
group by t.student_id, t.session_id, t.intended_session, t.name
;

insert into activity
select 2827 + row_number() over () as id, student_id, -1, -1, 'total', sum(duration)
from activity group by student_id
;

insert into activity select max(a.id) + 1, null, null, null, 'no time', interval '0'
from activity as a
;

alter table activity add column hours float8 ;
alter table activity add column minutes float8 ;
alter table activity add column seconds float8 ;
update activity set seconds = extract(epoch from duration) ;
update activity set minutes = seconds / 60 ;
update activity set hours = seconds / 3600 ;

alter table activity add column time_category varchar(10) ;
update activity set time_category = '< 2h' where session_id = -1 and duration < interval '2 hour' ;
update activity set time_category = '< 4h' where session_id = -1 and duration >= interval '2 hour' and duration < interval '4 hour' ;
update activity set time_category = '< 6h' where session_id = -1 and duration >= interval '4 hour' and duration < interval '6 hour' ;
update activity set time_category = '< 8h' where session_id = -1 and duration >= interval '6 hour' and duration < interval '8 hour' ;
update activity set time_category = '<10h' where session_id = -1 and duration >= interval '8 hour' and duration < interval '10 hour' ;
update activity set time_category = '<12h' where session_id = -1 and duration >= interval '10 hour' and duration < interval '12 hour' ;
update activity set time_category = '>12h' where session_id = -1 and duration >= interval '12 hour' ;

update activity set time_category = '< 10m' where session_id > 0 and                                      duration < interval '10 minute' ;
update activity set time_category = '< 20m' where session_id > 0 and duration >= interval '10 minute' and duration < interval '20 minute' ;
update activity set time_category = '< 30m' where session_id > 0 and duration >= interval '20 minute' and duration < interval '30 minute' ;
update activity set time_category = '< 40m' where session_id > 0 and duration >= interval '30 minute' and duration < interval '40 minute' ;
update activity set time_category = '< 50m' where session_id > 0 and duration >= interval '40 minute' and duration < interval '50 minute' ;
update activity set time_category = '> 50m'  where session_id > 0 and duration >= interval '50 minute' ;

update activity set time_category = 'no time'  where name ~ 'no time' ;
-- ACTIVITY END

-- POINTS BEGIN
create table points_fact as
select g.student_id, exam_id, a.id as activity_id, points
from grade_dm as g left join activity as a
on g.student_id = a.student_id and g.exam_id = a.session_id
;

update points_fact as p
set activity_id = a.id
from activity as a
where p.exam_id > 6 and p.student_id = a.student_id and a.name ~ 'total'
;

update points_fact as p
set activity_id = a.id
from activity as a
where p.activity_id is null and p.points > 0 and a.name ~ 'no time'
;

delete from points_fact where activity_id is null and points = 0 ;
-- POINTS END

-- STUDENT_DIM BEGIN
create table student_dim as
select id, name || trim(both ' ' from lastname) as fullname, name, lastname
from student ;
-- STUDENT_DIM END
*/

-- EXPORT BEGIN
copy exam_dim     to '/var/lib/postgresql/datamart/exam.csv'     delimiter ',' csv header ;
copy activity to '/var/lib/postgresql/datamart/activity.csv'     delimiter ',' csv header ;
copy student_dim  to '/var/lib/postgresql/datamart/student.csv'  delimiter ',' csv header ;
copy points_fact  to '/var/lib/postgresql/datamart/points.csv'   delimiter ',' csv header ;
-- EXPORT END

/*
-- BEGIN OF MESS

-- select * from points_fact where duration is null and exam_id < 7;

-- select student_id, session_id, sum(duration) from log group by student_id, session_id ;
--select * from exercise ;

-- create table exercise_session as
-- select distinct session_id, intended_session, duration from points_fact ;
-- select * from activity ;
*/


/*

-- DURATION BEGIN
create table duration_dm as
select student_id, exercise_id, sum(duration) as duration
from log group by student_id, exercise_id
;
insert into duration_dm
select student_id, 30 as exercise_id, sum(duration) as duration
from duration_dm
where exercise_id in (1, 2, 3, 4)
group by student_id
;
insert into duration_dm
select student_id, 31 as exercise_id, sum(duration) as duration
from duration_dm
where exercise_id in (5, 6, 7, 8, 9, 10)
group by student_id
;
insert into duration_dm
select student_id, 32 as exercise_id, sum(duration) as duration
from duration_dm
where exercise_id in (11, 12, 13, 14)
group by student_id
;
insert into duration_dm
select student_id, 33 as exercise_id, sum(duration) as duration
from duration_dm
where exercise_id in (15, 16, 17, 18, 19)
group by student_id
;
insert into duration_dm
select student_id, 34 as exercise_id, sum(duration) as duration
from duration_dm
where exercise_id in (20, 21, 22, 23)
group by student_id
;
insert into duration_dm
select student_id, 35 as exercise_id, sum(duration) as duration
from duration_dm
where exercise_id in (24, 25, 26, 27, 28, 29)
group by student_id
;
insert into duration_dm
select student_id, 36 as exercise_id, sum(duration) as duration
from duration_dm
where exercise_id < 30
group by student_id
;

-- DURATION_DIM BEGIN
create table duration_dim as
select row_number() over () as id, d as duration
from (
    select distinct(duration) as d from duration_dm order by duration
) as t
;
alter table duration_dim add column hours float8 ;
alter table duration_dim add column minutes float8 ;
alter table duration_dim add column seconds float8 ;
update duration_dim set seconds = extract(epoch from duration) ;
update duration_dim set minutes = seconds / 60 ;
update duration_dim set hours = seconds / 3600 ;
-- DURATION_DIM END

alter table duration_dm add column duration_id bigint ;

update duration_dm as dur
set duration_id = dim.id
from duration_dim as dim
where dur.duration = dim.duration
;
-- DURATION END


-- FACT_POINTS
create table fact_points as
select exam_id, exercise_id, duration_id, g.student_id, points as exam_points
from grade_dm as g join duration_dm as d
on g.student_id = d.student_id
order by exam_id, exercise_id, g.student_id, points
;
-- FACT_POINTS END

*/
