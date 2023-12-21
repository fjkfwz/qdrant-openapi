# DeleteAlias

Delete alias if exists

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias_name** | **str** |  | 

## Example

```python
from openapi_client.models.delete_alias import DeleteAlias

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAlias from a JSON string
delete_alias_instance = DeleteAlias.from_json(json)
# print the JSON string representation of the object
print DeleteAlias.to_json()

# convert the object into a dict
delete_alias_dict = delete_alias_instance.to_dict()
# create an instance of DeleteAlias from a dict
delete_alias_form_dict = delete_alias.from_dict(delete_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


