from rest_framework import serializers
from app.models import SkiArea

# converts to JSON
class SkiAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkiArea
        fields = [
            "name",
            "cur_temp",
            "cur_depth",
            "ytd",
            "wind_dir",
            "wind_dir",
            "new_snow_12",
            "new_snow_24",
            "new_snow_48",
        ]