/* -- Tables
 exercise
 final_exam
 grade
 inter_exam
 log
 session
 student
 student_logs
 */


/* Grade Queries
select * from grade ;
select count(*) from grade ;
select distinct(inter_exam_id) from grade ;
select distinct(final_exam_id) from grade ;
select distinct(exam_id) from grade ;

select * from grade where inter_exam_id = 0;
select (inter_exam_id + final_exam_id) as exam_id from grade ;

select student_id, count(*) from grade group by student_id;

select * from grade where exam_id is null ;
 */

/* Log queries
select * from log limit 10 ;
select "end" - "start" from log limit 10 ;
select count(distinct(duration)) from log ;
select count(*) from log ;
select * from log where date_part('hour', "start") = 12 ;
select ("start" + interval '12 hour') from log where date_part('hour', "start") = 0 ;
select sum(duration) from log ;
select * from log where duration < interval '0';
select count(distinct(seconds)) from log;
-- alter table log drop column seconds ;
select max(hours) from log ;

select max(it)
from (
    select count(*) as it
    from log
    group by student_id, session_id, exercise_id, activity, "start", "end", idle, mouse_wheel, mouse_wheel_click, mouse_click_left, mouse_click_right, mouse_movement, keystrokes
) as g;

select max(cnt) from ( select count(*) as cnt from log group by id ) as t ;

select exercise_id, session_id, name
from log join exercise on log.exercise_id = exercise.id ;

select substring(name from 5 for 1) from exercise ;

select NULLIF(substring(name from 5 for 1), '')::int from exercise ;

select column_name, data_type from information_schema.columns where table_name = 'log';

-- where exercise session is different from session_id
select exercise_id, session_id, name
from log join exercise on log.exercise_id = exercise.id
where session_id <> NULLIF(substring(name from 5 for 1), '')::int
;

-- 2828
-- select count ( distinct ( student_id, session_id, exercise_id ) ) from log ;
select student_id, exercise_id, sum(duration) from log
group by student_id, exercise_id
;

-- check 1014 hours
select sum(d) from
(select sum(duration) as d from log group by student_id, exercise_id) as t ;

select student_id, exercise_id, sum(duration) as duration from log group by student_id, exercise_id
;



select sum(duration) from duration_dm ;
 */
-- select id, student_id, session_id, exercise_id, activity, start, end, idle, mouse_wheel, mouse_wheel_click, mouse_click_left, mouse_click_right, mouse_movement, keystrokes, tk, version, date_from, date_to, lastupdate, duration, seconds, minutes, hours

-- select sum(exer_duration_id) from fact_points;


/*
  0 |  Es    

  1 |  Es_1_1
  2 |  Es_1_2
  3 |  Es_1_3
  4 |  Es_1_4

  5 |  Es_2_1
  6 |  Es_2_2
  7 |  Es_2_3
  8 |  Es_2_4
  9 |  Es_2_5
 10 |  Es_2_6

 11 |  Es_3_1
 12 |  Es_3_2
 13 |  Es_3_3
 14 |  Es_3_4

 15 |  Es_4_1
 16 |  Es_4_2
 17 |  Es_4_3
 18 |  Es_4_4
 19 |  Es_4_5

 20 |  Es_5_1
 21 |  Es_5_2
 22 |  Es_5_3
 23 |  Es_5_4

 24 |  Es_6_1
 25 |  Es_6_2
 26 |  Es_6_3
 27 |  Es_6_4
 28 |  Es_6_5
 29 |  Es_6_6
 */

/*
(1, 2, 3, 4)             -- Es_1_all 30
(5, 6, 7, 8, 9, 10)      -- Es_2_all 31
(11, 12, 13, 14)         -- Es_3_all 32
(15, 16, 17, 18, 19)     -- Es_4_all 33
(20, 21, 22, 23)         -- Es_5_all 34
(24, 25, 26, 27, 28, 29) -- Es_6_all 35
                                     36
*/

/*
select *
from duration_dm as t join duration_dim as dur
on t.duration_id = dur.id
where t.duration <> dur.duration
;
*/

-- select exam_id, exercise_id, duration_id, student_id, exam_points from fact_points;
-- For every student and exam there is about 27 exercises
-- 7 | 26.6284470246734398 |  37
/*
select min(n), avg(n), max(n)
from (
select count(*) n
from fact_points
group by student_id, exam_id
) as t
;
*/

-- For each student and exercise there is about 6 exams
/* 
select min(n), avg(n), max(n)
from (
select count(*) n
from fact_points
group by student_id, exercise_id, duration_id
) as t
*/

-- select * from fact_points where exercise_id = 36 ;

-- select percentile_cont(.99) within group (order by exam_points) from fact_points ;

/*
select percentile_cont(.10) within group (order by duration) as q10
    , percentile_cont(.20) within group (order by duration) as q20
    , percentile_cont(.30) within group (order by duration) as q30
    , percentile_cont(.40) within group (order by duration) as q40
    , percentile_cont(.50) within group (order by duration) as q50
    , percentile_cont(.60) within group (order by duration) as q60
    , percentile_cont(.70) within group (order by duration) as q70
    , percentile_cont(.80) within group (order by duration) as q80
    , percentile_cont(.90) within group (order by duration) as q90
    */


select max(duration) from activity where session_id > 0;
-- select percentile_cont(.90) within group (order by duration) from activity where session_id > 0;

-- <2 <4 <6 <8 <10 <12 other

-- 
