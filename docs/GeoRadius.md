# GeoRadius

Geo filter request  Matches coordinates inside the circle of `radius` and center with coordinates `center`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**center** | [**GeoPoint**](GeoPoint.md) |  | 
**radius** | **float** | Radius of the area in meters | 

## Example

```python
from openapi_client.models.geo_radius import GeoRadius

# TODO update the JSON string below
json = "{}"
# create an instance of GeoRadius from a JSON string
geo_radius_instance = GeoRadius.from_json(json)
# print the JSON string representation of the object
print GeoRadius.to_json()

# convert the object into a dict
geo_radius_dict = geo_radius_instance.to_dict()
# create an instance of GeoRadius from a dict
geo_radius_form_dict = geo_radius.from_dict(geo_radius_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


