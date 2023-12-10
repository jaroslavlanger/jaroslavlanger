# Data

------------|--------------------------------|
            | row_id                         |
            | timestamp                      |
train       | user_id                        |
.           | content_id                     |
csv         | content_type_id                |
            | task_container_id              | 0 ~ question, 1 ~ lecture
            | user_answer                    |
            | answered_correctly             |
            | prior_question_elapsed_time    |
            | prior_question_had_explanation |
------------|--------------------------------|
            | question_id                    | foreign key for the train/test `content_id` (when the `content_type_id` = 0)
questions   | bundle_id                      | (code for which questions are served together)
.           | correct_answer                 | (can be checked with user_answer)
csv         | part                           |
            | tags                           | (sufficient for question clustering)
------------|--------------------------------|
lectures    | lecture_id                     | foreign key for the train/test `content_id` (when the `content_type_id` = 1)
.           | part                           |
csv         | tag                            | (sufficient for lectures clustering)
            | type_of                        |
------------|--------------------------------|
example     | row_id
_submission | answered_correctly
_sample.csv | group_num
------------|---------------------------------
example     | row_id
_           | timestamp
test        | user_id
_           | content_id
rows        | content_type_id
.           | task_container_id
csv         | user_answer
            | answered_correctly
            | prior_question_elapsed_time
            | prior_question_had_explanation
            | **prior_group_responses**
            | **prior_group_answers_correct**

