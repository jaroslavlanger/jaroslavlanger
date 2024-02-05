select l.student_id, l.inter_exam_id, l.final_exam_id, l.exercise_id, l.points, r.points
from grade l inner join grade r
on l.student_id = r.student_id
and l.inter_exam_id = r.inter_exam_id
and l.final_exam_id = r.final_exam_id
and l.exercise_id = r.exercise_id
where l.points <> r.points;
