# GetCollections200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**CollectionsResponse**](CollectionsResponse.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.get_collections200_response import GetCollections200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCollections200Response from a JSON string
get_collections200_response_instance = GetCollections200Response.from_json(json)
# print the JSON string representation of the object
print GetCollections200Response.to_json()

# convert the object into a dict
get_collections200_response_dict = get_collections200_response_instance.to_dict()
# create an instance of GetCollections200Response from a dict
get_collections200_response_form_dict = get_collections200_response.from_dict(get_collections200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


