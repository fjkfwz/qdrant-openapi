# SearchRequest

Search request. Holds all conditions and parameters for the search of most similar points by vector similarity given the filtering restrictions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 
**vector** | [**NamedVectorStruct**](NamedVectorStruct.md) |  | 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**params** | [**SearchParams**](SearchParams.md) |  | [optional] 
**limit** | **int** | Max number of result to return | 
**offset** | **int** | Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues. | [optional] 
**with_payload** | [**WithPayloadInterface**](WithPayloadInterface.md) |  | [optional] 
**with_vector** | [**WithVector**](WithVector.md) |  | [optional] 
**score_threshold** | **float** | Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned. | [optional] 

## Example

```python
from openapi_client.models.search_request import SearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequest from a JSON string
search_request_instance = SearchRequest.from_json(json)
# print the JSON string representation of the object
print SearchRequest.to_json()

# convert the object into a dict
search_request_dict = search_request_instance.to_dict()
# create an instance of SearchRequest from a dict
search_request_form_dict = search_request.from_dict(search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


