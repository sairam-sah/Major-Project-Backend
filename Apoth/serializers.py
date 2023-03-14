from rest_framework import serializers
class FlowerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=1000)
    sname = serializers.CharField(max_length=1000)
    property = serializers.CharField(max_length=1000)
    location = serializers.CharField(max_length=1000)


# class FLowerForm(forms.Form):
#     name = forms.CharField(max_length=1000)
#     sname = forms.CharField(max_length=1000)
#     property = forms.CharField(max_length=1000)
#     location = forms.CharField(max_length=1000)
