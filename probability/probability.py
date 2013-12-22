from __future__ import division

import sys
import random

def generate_families(N_families, N_children_per_family):
    """
    Generates a list of two-child families, where each family is a two-element
    list of (birth day of week, gender) pairs.
    """
    all_families = []
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']
    genders = ['boy', 'girl']
    for ii in xrange(N_families):
        family = []
        for child in xrange(N_children_per_family):
            day = random.choice(days)
            gender = random.choice(genders)
            family.append((day,gender))
        all_families.append(family)
    return all_families

def test_condition(family):
    """ Tests whether a family has a boy born on Tuesday. """
    for child in family:
        (day, gender) = child
        if day == 'Tuesday' and gender == 'boy':
            return True
    return False

def test_two_boys(family):
    """ Tests whether a family has two boys. """
    ((day1, gender1), (day2, gender2)) = family
    return (gender1 == gender2 == 'boy')

def example_problem(families):
    """
    Given a list of families, returns the conditional probability
    of having two boys given that one is a boy born on a Tuesday.
    """
    conditioned = [fam for fam in families if test_condition(fam)]
    fully_satisfied = [fam for fam in conditioned if test_two_boys(fam)]

    conditional_probability = len(fully_satisfied) / len(conditioned)

    print("Conditional probability was %f."%conditional_probability)

if __name__ == '__main__':
    N_families = int(sys.argv[1])
    families = generate_families(N_families, 2)
    example_problem(families)
