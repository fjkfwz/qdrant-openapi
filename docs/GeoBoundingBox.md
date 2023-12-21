# GeoBoundingBox

Geo filter request  Matches coordinates inside the rectangle, described by coordinates of lop-left and bottom-right edges

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top_left** | [**GeoPoint**](GeoPoint.md) |  | 
**bottom_right** | [**GeoPoint**](GeoPoint.md) |  | 

## Example

```python
from openapi_client.models.geo_bounding_box import GeoBoundingBox

# TODO update the JSON string below
json = "{}"
# create an instance of GeoBoundingBox from a JSON string
geo_bounding_box_instance = GeoBoundingBox.from_json(json)
# print the JSON string representation of the object
print GeoBoundingBox.to_json()

# convert the object into a dict
geo_bounding_box_dict = geo_bounding_box_instance.to_dict()
# create an instance of GeoBoundingBox from a dict
geo_bounding_box_form_dict = geo_bounding_box.from_dict(geo_bounding_box_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


