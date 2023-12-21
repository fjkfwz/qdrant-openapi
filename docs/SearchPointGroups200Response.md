# SearchPointGroups200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**GroupsResult**](GroupsResult.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.search_point_groups200_response import SearchPointGroups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPointGroups200Response from a JSON string
search_point_groups200_response_instance = SearchPointGroups200Response.from_json(json)
# print the JSON string representation of the object
print SearchPointGroups200Response.to_json()

# convert the object into a dict
search_point_groups200_response_dict = search_point_groups200_response_instance.to_dict()
# create an instance of SearchPointGroups200Response from a dict
search_point_groups200_response_form_dict = search_point_groups200_response.from_dict(search_point_groups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


