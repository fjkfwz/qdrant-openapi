# CreateAliasOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_alias** | [**CreateAlias**](CreateAlias.md) |  | 

## Example

```python
from qdrant_openapi.models.create_alias_operation import CreateAliasOperation

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAliasOperation from a JSON string
create_alias_operation_instance = CreateAliasOperation.from_json(json)
# print the JSON string representation of the object
print CreateAliasOperation.to_json()

# convert the object into a dict
create_alias_operation_dict = create_alias_operation_instance.to_dict()
# create an instance of CreateAliasOperation from a dict
create_alias_operation_form_dict = create_alias_operation.from_dict(create_alias_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


