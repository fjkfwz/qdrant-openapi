# SearchPoints200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**List[ScoredPoint]**](ScoredPoint.md) |  | [optional] 

## Example

```python
from openapi_client.models.search_points200_response import SearchPoints200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPoints200Response from a JSON string
search_points200_response_instance = SearchPoints200Response.from_json(json)
# print the JSON string representation of the object
print SearchPoints200Response.to_json()

# convert the object into a dict
search_points200_response_dict = search_points200_response_instance.to_dict()
# create an instance of SearchPoints200Response from a dict
search_points200_response_form_dict = search_points200_response.from_dict(search_points200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


