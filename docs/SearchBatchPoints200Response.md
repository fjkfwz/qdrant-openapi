# SearchBatchPoints200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | **List[List[ScoredPoint]]** |  | [optional] 

## Example

```python
from qdrant_openapi.models.search_batch_points200_response import SearchBatchPoints200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchBatchPoints200Response from a JSON string
search_batch_points200_response_instance = SearchBatchPoints200Response.from_json(json)
# print the JSON string representation of the object
print SearchBatchPoints200Response.to_json()

# convert the object into a dict
search_batch_points200_response_dict = search_batch_points200_response_instance.to_dict()
# create an instance of SearchBatchPoints200Response from a dict
search_batch_points200_response_form_dict = search_batch_points200_response.from_dict(search_batch_points200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


