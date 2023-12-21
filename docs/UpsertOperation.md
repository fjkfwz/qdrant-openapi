# UpsertOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upsert** | [**PointInsertOperations**](PointInsertOperations.md) |  | 

## Example

```python
from qdrant_openapi.models.upsert_operation import UpsertOperation

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertOperation from a JSON string
upsert_operation_instance = UpsertOperation.from_json(json)
# print the JSON string representation of the object
print UpsertOperation.to_json()

# convert the object into a dict
upsert_operation_dict = upsert_operation_instance.to_dict()
# create an instance of UpsertOperation from a dict
upsert_operation_form_dict = upsert_operation.from_dict(upsert_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


