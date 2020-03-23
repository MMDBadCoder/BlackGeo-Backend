# Generated by Django 3.0.4 on 2020-03-23 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drawingProblems', '0002_auto_20200320_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawingproblem',
            name='costs',
            field=models.CharField(blank=True, default='[{"name": "reward", "image_url": "https://cdn1.iconfinder.com/data/icons/talent-management/64/rewarding-reward-gift-value-award-512.png", "value": 100, "code": 99999999}, {"name": "POINT", "image_url": "https://wiki.geogebra.org/uploads/d/dc/Tool_New_Point.gif", "value": 0, "code": 1}, {"name": "JOIN", "image_url": "https://wiki.geogebra.org/uploads/d/d2/Tool_Line_through_Two_Points.gif", "value": 1, "code": 2}, {"name": "SEGMENT15", "image_url": "https://wiki.geogebra.org/uploads/c/cd/Tool_Segment_between_Two_Points.gif", "value": 1, "code": 15}, {"name": "CIRCLE_TWO_POINTS", "image_url": "https://wiki.geogebra.org/uploads/1/1e/Tool_Circle_Center_Point.gif", "value": 1, "code": 10}, {"name": "COMPASSES", "image_url": "https://wiki.geogebra.org/uploads/e/e3/Tool_Compasses.gif", "value": 1, "code": 53}, {"name": "CIRCLE_THREE_POINTS", "image_url": "https://wiki.geogebra.org/uploads/b/bc/Tool_Circle_3Points.gif", "value": 5, "code": 11}, {"name": "LINE_BISECTOR", "image_url": "https://wiki.geogebra.org/uploads/1/10/Tool_Perpendicular_Bisector.gif", "value": 3, "code": 8}, {"name": "ORTHOGONAL", "image_url": "https://wiki.geogebra.org/uploads/7/78/Tool_Perpendicular_Line.gif", "value": 4, "code": 4}, {"name": "MIDPOINT", "image_url": "https://wiki.geogebra.org/uploads/1/1c/Tool_Midpoint_or_Center.gif", "value": 3, "code": 19}, {"name": "PARALLEL", "image_url": "https://wiki.geogebra.org/uploads/f/fc/Tool_Parallel_Line.gif", "value": 4, "code": 3}, {"name": "ANGULAR_BISECTOR", "image_url": "https://wiki.geogebra.org/uploads/e/ed/Tool_Angular_Bisector.gif", "value": 3, "code": 9}]', max_length=10000),
        ),
    ]
