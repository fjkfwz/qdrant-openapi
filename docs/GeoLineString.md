# GeoLineString

Ordered sequence of GeoPoints representing the line

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | [**List[GeoPoint]**](GeoPoint.md) |  | 

## Example

```python
from openapi_client.models.geo_line_string import GeoLineString

# TODO update the JSON string below
json = "{}"
# create an instance of GeoLineString from a JSON string
geo_line_string_instance = GeoLineString.from_json(json)
# print the JSON string representation of the object
print GeoLineString.to_json()

# convert the object into a dict
geo_line_string_dict = geo_line_string_instance.to_dict()
# create an instance of GeoLineString from a dict
geo_line_string_form_dict = geo_line_string.from_dict(geo_line_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


