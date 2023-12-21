# RecommendRequest

Recommendation request. Provides positive and negative examples of the vectors, which can be ids of points that are already stored in the collection, raw vectors, or even ids and vectors combined.  Service should look for the points which are closer to positive examples and at the same time further to negative examples. The concrete way of how to compare negative and positive distances is up to the `strategy` chosen.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 
**positive** | [**List[RecommendExample]**](RecommendExample.md) | Look for vectors closest to those | [optional] [default to []]
**negative** | [**List[RecommendExample]**](RecommendExample.md) | Try to avoid vectors like this | [optional] [default to []]
**strategy** | [**RecommendStrategy**](RecommendStrategy.md) |  | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**params** | [**SearchParams**](SearchParams.md) |  | [optional] 
**limit** | **int** | Max number of result to return | 
**offset** | **int** | Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues. | [optional] 
**with_payload** | [**WithPayloadInterface**](WithPayloadInterface.md) |  | [optional] 
**with_vector** | [**WithVector**](WithVector.md) |  | [optional] 
**score_threshold** | **float** | Define a minimal score threshold for the result. If defined, less similar results will not be returned. Score of the returned result might be higher or smaller than the threshold depending on the Distance function used. E.g. for cosine similarity only higher scores will be returned. | [optional] 
**using** | **str** |  | [optional] 
**lookup_from** | [**LookupLocation**](LookupLocation.md) |  | [optional] 

## Example

```python
from openapi_client.models.recommend_request import RecommendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendRequest from a JSON string
recommend_request_instance = RecommendRequest.from_json(json)
# print the JSON string representation of the object
print RecommendRequest.to_json()

# convert the object into a dict
recommend_request_dict = recommend_request_instance.to_dict()
# create an instance of RecommendRequest from a dict
recommend_request_form_dict = recommend_request.from_dict(recommend_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


