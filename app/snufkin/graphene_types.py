import graphene
from django.contrib.gis.db.models.fields import PointField
from graphene_django.converter import convert_django_field


class GraphenePointField(graphene.Scalar):
    """
    The `GraphenePointField` type represents a postgis Point object
    """

    @staticmethod
    def serialize(point):
        return {
            "latitude": point.x,
            "longitude": point.y,
        }

@convert_django_field.register(PointField)
def convert_point_field(field, registry=None):
    return GraphenePointField(description=field.help_text, required=not field.null)
