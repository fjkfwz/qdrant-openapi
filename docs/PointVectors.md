# PointVectors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ExtendedPointId**](ExtendedPointId.md) |  | 
**vector** | [**VectorStruct**](VectorStruct.md) |  | 

## Example

```python
from qdrant_openapi.models.point_vectors import PointVectors

# TODO update the JSON string below
json = "{}"
# create an instance of PointVectors from a JSON string
point_vectors_instance = PointVectors.from_json(json)
# print the JSON string representation of the object
print PointVectors.to_json()

# convert the object into a dict
point_vectors_dict = point_vectors_instance.to_dict()
# create an instance of PointVectors from a dict
point_vectors_form_dict = point_vectors.from_dict(point_vectors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


