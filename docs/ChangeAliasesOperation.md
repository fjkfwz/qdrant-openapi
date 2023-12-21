# ChangeAliasesOperation

Operation for performing changes of collection aliases. Alias changes are atomic, meaning that no collection modifications can happen between alias operations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[AliasOperations]**](AliasOperations.md) |  | 

## Example

```python
from openapi_client.models.change_aliases_operation import ChangeAliasesOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeAliasesOperation from a JSON string
change_aliases_operation_instance = ChangeAliasesOperation.from_json(json)
# print the JSON string representation of the object
print ChangeAliasesOperation.to_json()

# convert the object into a dict
change_aliases_operation_dict = change_aliases_operation_instance.to_dict()
# create an instance of ChangeAliasesOperation from a dict
change_aliases_operation_form_dict = change_aliases_operation.from_dict(change_aliases_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


