from problem_set.bitmask_dp_problems import (
    can_partition_k_subsets,
    max_students,
    min_number_of_semesters,
    number_ways,
    smallest_sufficient_team,
)


def test_can_partition_k_subsets_empty():
    assert can_partition_k_subsets([], 0) is True


def test_can_partition_k_subsets_single_bucket():
    assert can_partition_k_subsets([1, 2, 3, 4], 1) is True


def test_can_partition_k_subsets_normal():
    assert can_partition_k_subsets([4, 3, 2, 3, 5, 2, 1], 4) is True


def test_can_partition_k_subsets_impossible():
    assert can_partition_k_subsets([1, 2, 3, 4], 3) is False


def test_smallest_sufficient_team_single_skill():
    req_skills = ["java"]
    people = [["java"]]
    result = smallest_sufficient_team(req_skills, people)
    assert result == [0]


def test_smallest_sufficient_team_normal():
    req_skills = ["java", "nodejs", "reactjs"]
    people = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    result = smallest_sufficient_team(req_skills, people)
    covered = set()
    for person in result:
        covered.update(people[person])
    assert covered == set(req_skills)
    assert len(result) == 2


def test_smallest_sufficient_team_one_person_covers_all():
    req_skills = ["java", "nodejs"]
    people = [["java", "nodejs"], ["java"]]
    result = smallest_sufficient_team(req_skills, people)
    assert result == [0]


def test_min_number_of_semesters_no_relations():
    assert min_number_of_semesters(4, [], 4) == 1


def test_min_number_of_semesters_single_course():
    assert min_number_of_semesters(1, [], 1) == 1


def test_min_number_of_semesters_chain_with_limit():
    assert min_number_of_semesters(4, [[2, 1], [3, 1], [1, 4]], 2) == 3


def test_min_number_of_semesters_no_limit_needed():
    assert min_number_of_semesters(5, [[2, 1], [3, 1], [4, 1], [1, 5]], 2) == 4


def test_max_students_normal():
    seats = [
        ["#", ".", "#", "#", ".", "#"],
        [".", "#", "#", "#", "#", "."],
        ["#", ".", "#", "#", ".", "#"],
    ]
    assert max_students(seats) == 4


def test_number_ways_single_assignment():
    assert number_ways([[3, 4], [4, 5], [5]]) == 1


def test_number_ways_several_assignments():
    assert number_ways([[3, 5, 1], [3, 5]]) == 4


def test_number_ways_five_people():
    hats = [[1, 2, 3], [2, 3, 5, 6], [1, 3, 7, 9], [1, 8, 9], [2, 5, 7]]
    assert number_ways(hats) == 111
