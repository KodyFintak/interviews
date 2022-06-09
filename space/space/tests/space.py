"""space."""


def get_closest_space_centers(all_space_centers, number_of_centers):
    pass

def test_gets_empty_path():
    all_space_centers = []
    number_of_space_centers = 0
    assert get_closest_space_centers(all_space_centers, number_of_space_centers) == []

def test_gets_one_path():
    all_space_centers = [[1, 1]]
    number_of_space_centers = 1
    expected_closest_space_centers = [[1, 1]]
    assert get_closest_space_centers(all_space_centers, number_of_space_centers) == expected_closest_space_centers

def test_gets_shortest_path():
    all_space_centers = [[-1, 2], [3, 4], [1, 1]]
    number_of_space_centers = 2
    expected_closest_space_centers = [[1, 1], [-1, 2]]
    assert get_closest_space_centers(all_space_centers, number_of_space_centers) == expected_closest_space_centers
