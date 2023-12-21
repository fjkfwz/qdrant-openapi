# UpdateResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **int** | Sequential number of the operation | [optional] 
**status** | [**UpdateStatus**](UpdateStatus.md) |  | 

## Example

```python
from qdrant_openapi.models.update_result import UpdateResult

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateResult from a JSON string
update_result_instance = UpdateResult.from_json(json)
# print the JSON string representation of the object
print UpdateResult.to_json()

# convert the object into a dict
update_result_dict = update_result_instance.to_dict()
# create an instance of UpdateResult from a dict
update_result_form_dict = update_result.from_dict(update_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


