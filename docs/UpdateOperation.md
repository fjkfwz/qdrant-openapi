# UpdateOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upsert** | [**PointInsertOperations**](PointInsertOperations.md) |  | 
**delete** | [**PointsSelector**](PointsSelector.md) |  | 
**set_payload** | [**SetPayload**](SetPayload.md) |  | 
**overwrite_payload** | [**SetPayload**](SetPayload.md) |  | 
**delete_payload** | [**DeletePayload**](DeletePayload.md) |  | 
**clear_payload** | [**PointsSelector**](PointsSelector.md) |  | 
**update_vectors** | [**UpdateVectors**](UpdateVectors.md) |  | 
**delete_vectors** | [**DeleteVectors**](DeleteVectors.md) |  | 

## Example

```python
from qdrant_openapi.models.update_operation import UpdateOperation

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOperation from a JSON string
update_operation_instance = UpdateOperation.from_json(json)
# print the JSON string representation of the object
print UpdateOperation.to_json()

# convert the object into a dict
update_operation_dict = update_operation_instance.to_dict()
# create an instance of UpdateOperation from a dict
update_operation_form_dict = update_operation.from_dict(update_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


