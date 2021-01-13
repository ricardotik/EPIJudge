import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))
Range = collections.namedtuple(
    "Range", ('starting_point', 'length', 'ending_point'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    # TODO - you fill in here.
    r1_x_range = Range(starting_point=r1.x, length=r1.width,
                       ending_point=r1.x+r1.width)
    r1_y_range = Range(starting_point=r1.y, length=r1.height,
                       ending_point=r1.y+r1.height)
    r2_x_range = Range(starting_point=r2.x, length=r2.width,
                       ending_point=r2.x+r2.width)
    r2_y_range = Range(starting_point=r2.y, length=r2.height,
                       ending_point=r2.y+r2.height)
    x_intersect_range = intersect_range(r1_x_range, r2_x_range)
    y_intersect_range = intersect_range(r1_y_range, r2_y_range)
    print("x_intersection")
    print(x_intersect_range)
    print("y_intersection")
    print(y_intersect_range)
    if x_intersect_range != None and y_intersect_range != None:
        return Rect(x_intersect_range.starting_point, y_intersect_range.starting_point, x_intersect_range.length, y_intersect_range.length)
    else:
        return Rect(0, 0, -1, -1)


def intersect_range(r1: Range, r2: Range) -> Range:
    # r1 must be the range that come first
    lower_range = Range(0, 0, 0)
    higher_range = Range(0, 0, 0)

    if r1.starting_point > r2.starting_point:
        lower_range = r2
        higher_range = r1
    else:
        lower_range = r1
        higher_range = r2

    if lower_range.starting_point <= higher_range.starting_point and lower_range.ending_point >= higher_range.starting_point and lower_range.ending_point < higher_range.ending_point:
        # lower_range and higher_range collide with head and tail, return the overlap
        print("lower_range and higher_range collides with the head and tail")
        print(lower_range.ending_point - higher_range.starting_point)
        return Range(higher_range.starting_point, lower_range.ending_point - higher_range.starting_point, lower_range.ending_point)
    elif lower_range.starting_point <= higher_range.starting_point and lower_range.ending_point >= higher_range.ending_point:
        # lower_range contains higher_range
        print("containment")

        return higher_range
    else:
        # no overlap at all
        return None


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
