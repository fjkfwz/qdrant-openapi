# DeleteOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete** | [**PointsSelector**](PointsSelector.md) |  | 

## Example

```python
from qdrant_openapi.models.delete_operation import DeleteOperation

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOperation from a JSON string
delete_operation_instance = DeleteOperation.from_json(json)
# print the JSON string representation of the object
print DeleteOperation.to_json()

# convert the object into a dict
delete_operation_dict = delete_operation_instance.to_dict()
# create an instance of DeleteOperation from a dict
delete_operation_form_dict = delete_operation.from_dict(delete_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


