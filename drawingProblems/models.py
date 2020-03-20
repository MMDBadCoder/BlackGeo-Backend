import json

from django.db import models
from problemManager.models import Problem

available_objects = [
    {
        'name': 'reward',
        'image_url': 'https://cdn1.iconfinder.com/data/icons/talent-management/64/rewarding-reward-gift-value-award-512.png',
        'value': 100,
        'code': 99999999
    },
    {
        "name": "POINT",
        "image_url": "https://wiki.geogebra.org/uploads/d/dc/Tool_New_Point.gif",
        "value": 0,
        "code": 1
    },
    {
        "name": "JOIN",
        "image_url": "https://wiki.geogebra.org/uploads/d/d2/Tool_Line_through_Two_Points.gif",
        "value": 1,
        "code": 2
    },
    {
        "name": "SEGMENT15",
        "image_url": "https://wiki.geogebra.org/uploads/c/cd/Tool_Segment_between_Two_Points.gif",
        "value": 1,
        "code": 15
    },
    {
        "name": "CIRCLE_TWO_POINTS",
        "image_url": "https://wiki.geogebra.org/uploads/1/1e/Tool_Circle_Center_Point.gif",
        "value": 1,
        "code": 10
    },
    {
        "name": "COMPASSES",
        "image_url": "https://wiki.geogebra.org/uploads/e/e3/Tool_Compasses.gif",
        "value": 1,
        "code": 53
    },
    {
        "name": "CIRCLE_THREE_POINTS",
        "image_url": "https://wiki.geogebra.org/uploads/b/bc/Tool_Circle_3Points.gif",
        "value": 5,
        "code": 11
    },
    {
        "name": "LINE_BISECTOR",
        "image_url": "https://wiki.geogebra.org/uploads/1/10/Tool_Perpendicular_Bisector.gif",
        "value": 3,
        "code": 8
    },
    {
        "name": "ORTHOGONAL",
        "image_url": "https://wiki.geogebra.org/uploads/7/78/Tool_Perpendicular_Line.gif",
        "value": 4,
        "code": 4
    },
    {
        "name": "MIDPOINT",
        "image_url": "https://wiki.geogebra.org/uploads/1/1c/Tool_Midpoint_or_Center.gif",
        "value": 3,
        "code": 19
    },
    {
        "name": "PARALLEL",
        "image_url": "https://wiki.geogebra.org/uploads/f/fc/Tool_Parallel_Line.gif",
        "value": 4,
        "code": 3
    },
    {
        "name": "ANGULAR_BISECTOR",
        "image_url": "https://wiki.geogebra.org/uploads/e/ed/Tool_Angular_Bisector.gif",
        "value": 3,
        "code": 9
    }
]


class DrawingProblem(Problem, models.Model):
    goals_elements = models.CharField(max_length=1000, blank=True, default='[]')
    costs = models.CharField(max_length=10000, blank=True, default=json.dumps(available_objects))
