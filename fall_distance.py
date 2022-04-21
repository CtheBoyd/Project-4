# Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 4/20/2022
# Description: Determines the distance an object falls due to gravity in a specific time period.
#


def fall_distance(time):
    """Determines the distance an object falls due to gravity in a specific time period."""
    gravity = 9.8
    distance = ((time ** 2) * gravity) / 2
    return distance

