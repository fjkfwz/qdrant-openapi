# DiscoverRequest

Use context and a target to find the most similar points, constrained by the context.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 
**target** | [**RecommendExample**](RecommendExample.md) |  | [optional] 
**context** | [**List[ContextExamplePair]**](ContextExamplePair.md) | Pairs of { positive, negative } examples to constrain the search.  When using only the context (without a target), a special search - called context search - is performed where pairs of points are used to generate a loss that guides the search towards the zone where most positive examples overlap. This means that the score minimizes the scenario of finding a point closer to a negative than to a positive part of a pair.  Since the score of a context relates to loss, the maximum score a point can get is 0.0, and it becomes normal that many points can have a score of 0.0.  For discovery search (when including a target), the context part of the score for each pair is calculated +1 if the point is closer to a positive than to a negative part of a pair, and -1 otherwise. | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**params** | [**SearchParams**](SearchParams.md) |  | [optional] 
**limit** | **int** | Max number of result to return | 
**offset** | **int** | Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues. | [optional] 
**with_payload** | [**WithPayloadInterface**](WithPayloadInterface.md) |  | [optional] 
**with_vector** | [**WithVector**](WithVector.md) |  | [optional] 
**using** | **str** |  | [optional] 
**lookup_from** | [**LookupLocation**](LookupLocation.md) |  | [optional] 

## Example

```python
from openapi_client.models.discover_request import DiscoverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoverRequest from a JSON string
discover_request_instance = DiscoverRequest.from_json(json)
# print the JSON string representation of the object
print DiscoverRequest.to_json()

# convert the object into a dict
discover_request_dict = discover_request_instance.to_dict()
# create an instance of DiscoverRequest from a dict
discover_request_form_dict = discover_request.from_dict(discover_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


