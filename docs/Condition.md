# Condition


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
**is_empty** | [**PayloadField**](PayloadField.md) |  | 
**is_null** | [**PayloadField**](PayloadField.md) |  | 
**has_id** | [**List[ExtendedPointId]**](ExtendedPointId.md) |  | 
**nested** | [**Nested**](Nested.md) |  | 
**should** | [**List[Condition]**](Condition.md) | At least one of those conditions should match | [optional] 
**must** | [**List[Condition]**](Condition.md) | All conditions must match | [optional] 
**must_not** | [**List[Condition]**](Condition.md) | All conditions must NOT match | [optional] 

## Example

```python
from openapi_client.models.condition import Condition

# TODO update the JSON string below
json = "{}"
# create an instance of Condition from a JSON string
condition_instance = Condition.from_json(json)
# print the JSON string representation of the object
print Condition.to_json()

# convert the object into a dict
condition_dict = condition_instance.to_dict()
# create an instance of Condition from a dict
condition_form_dict = condition.from_dict(condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


