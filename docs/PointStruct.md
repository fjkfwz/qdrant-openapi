# PointStruct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ExtendedPointId**](ExtendedPointId.md) |  | 
**vector** | [**VectorStruct**](VectorStruct.md) |  | 
**payload** | **Dict[str, object]** |  | [optional] 

## Example

```python
from qdrant_openapi.models.point_struct import PointStruct

# TODO update the JSON string below
json = "{}"
# create an instance of PointStruct from a JSON string
point_struct_instance = PointStruct.from_json(json)
# print the JSON string representation of the object
print PointStruct.to_json()

# convert the object into a dict
point_struct_dict = point_struct_instance.to_dict()
# create an instance of PointStruct from a dict
point_struct_form_dict = point_struct.from_dict(point_struct_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


