# GetCollectionAliases200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**CollectionsAliasesResponse**](CollectionsAliasesResponse.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_collection_aliases200_response import GetCollectionAliases200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCollectionAliases200Response from a JSON string
get_collection_aliases200_response_instance = GetCollectionAliases200Response.from_json(json)
# print the JSON string representation of the object
print GetCollectionAliases200Response.to_json()

# convert the object into a dict
get_collection_aliases200_response_dict = get_collection_aliases200_response_instance.to_dict()
# create an instance of GetCollectionAliases200Response from a dict
get_collection_aliases200_response_form_dict = get_collection_aliases200_response.from_dict(get_collection_aliases200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


