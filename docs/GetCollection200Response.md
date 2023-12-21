# GetCollection200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**CollectionInfo**](CollectionInfo.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.get_collection200_response import GetCollection200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCollection200Response from a JSON string
get_collection200_response_instance = GetCollection200Response.from_json(json)
# print the JSON string representation of the object
print GetCollection200Response.to_json()

# convert the object into a dict
get_collection200_response_dict = get_collection200_response_instance.to_dict()
# create an instance of GetCollection200Response from a dict
get_collection200_response_form_dict = get_collection200_response.from_dict(get_collection200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


