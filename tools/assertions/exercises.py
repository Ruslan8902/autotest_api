from clients.exercises.exercises_schema import CreateExerciseRequestSchema, \
    GetExerciseResponseSchema, ExerciseSchema
from tools.assertions.base import assert_equal

def assert_exercise(
        actual: ExerciseSchema,
        expected: ExerciseSchema
):
    """
        Проверяет, что фактические данные задания соответствуют ожидаемым.

        :param actual: Фактические данные задания.
        :param expected: Ожидаемые данные задания.
        :raises AssertionError: Если хотя бы одно поле не совпадает.
        """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_get_exercise_response(
        request: GetExerciseResponseSchema,
        response: GetExerciseResponseSchema
):
    assert_exercise(request.exercise, response.exercise)



def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: GetExerciseResponseSchema
):
    """
    Проверяет, что ответ на создание задания соответствует данным из запроса.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными созданного задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(request.title, response.exercise.title, "title")
    assert_equal(request.course_id, response.exercise.course_id, "course_id")
    assert_equal(request.max_score, response.exercise.max_score, "max_score")
    assert_equal(request.min_score, response.exercise.min_score, "min_score")
    assert_equal(request.order_index, response.exercise.order_index, "order_index")
    assert_equal(request.description, response.exercise.description, "description")
    assert_equal(request.estimated_time, response.exercise.estimated_time, "estimated_time")
