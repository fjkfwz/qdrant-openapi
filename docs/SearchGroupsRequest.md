# SearchGroupsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 
**vector** | [**NamedVectorStruct**](NamedVectorStruct.md) |  | 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**params** | [**SearchParams**](SearchParams.md) |  | [optional] 
**with_payload** | [**WithPayloadInterface**](WithPayloadInterface.md) |  | [optional] 
**with_vector** | [**WithVector**](WithVector.md) |  | [optional] 
**score_threshold** | **float** | Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned. | [optional] 
**group_by** | **str** | Payload field to group by, must be a string or number field. If the field contains more than 1 value, all values will be used for grouping. One point can be in multiple groups. | 
**group_size** | **int** | Maximum amount of points to return per group | 
**limit** | **int** | Maximum amount of groups to return | 
**with_lookup** | [**WithLookupInterface**](WithLookupInterface.md) |  | [optional] 

## Example

```python
from openapi_client.models.search_groups_request import SearchGroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchGroupsRequest from a JSON string
search_groups_request_instance = SearchGroupsRequest.from_json(json)
# print the JSON string representation of the object
print SearchGroupsRequest.to_json()

# convert the object into a dict
search_groups_request_dict = search_groups_request_instance.to_dict()
# create an instance of SearchGroupsRequest from a dict
search_groups_request_form_dict = search_groups_request.from_dict(search_groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


