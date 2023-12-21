# FieldCondition

All possible payload filtering conditions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Payload key | 
**match** | [**Match**](Match.md) |  | [optional] 
**range** | [**Range**](Range.md) |  | [optional] 
**geo_bounding_box** | [**GeoBoundingBox**](GeoBoundingBox.md) |  | [optional] 
**geo_radius** | [**GeoRadius**](GeoRadius.md) |  | [optional] 
**geo_polygon** | [**GeoPolygon**](GeoPolygon.md) |  | [optional] 
**values_count** | [**ValuesCount**](ValuesCount.md) |  | [optional] 

## Example

```python
from openapi_client.models.field_condition import FieldCondition

# TODO update the JSON string below
json = "{}"
# create an instance of FieldCondition from a JSON string
field_condition_instance = FieldCondition.from_json(json)
# print the JSON string representation of the object
print FieldCondition.to_json()

# convert the object into a dict
field_condition_dict = field_condition_instance.to_dict()
# create an instance of FieldCondition from a dict
field_condition_form_dict = field_condition.from_dict(field_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


