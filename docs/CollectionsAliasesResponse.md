# CollectionsAliasesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[AliasDescription]**](AliasDescription.md) |  | 

## Example

```python
from qdrant_openapi.models.collections_aliases_response import CollectionsAliasesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsAliasesResponse from a JSON string
collections_aliases_response_instance = CollectionsAliasesResponse.from_json(json)
# print the JSON string representation of the object
print CollectionsAliasesResponse.to_json()

# convert the object into a dict
collections_aliases_response_dict = collections_aliases_response_instance.to_dict()
# create an instance of CollectionsAliasesResponse from a dict
collections_aliases_response_form_dict = collections_aliases_response.from_dict(collections_aliases_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


