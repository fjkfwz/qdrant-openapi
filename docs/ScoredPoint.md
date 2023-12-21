# ScoredPoint

Search result

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ExtendedPointId**](ExtendedPointId.md) |  | 
**version** | **int** | Point version | 
**score** | **float** | Points vector distance to the query vector | 
**payload** | **Dict[str, object]** |  | [optional] 
**vector** | [**VectorStruct**](VectorStruct.md) |  | [optional] 
**shard_key** | [**ShardKey**](ShardKey.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.scored_point import ScoredPoint

# TODO update the JSON string below
json = "{}"
# create an instance of ScoredPoint from a JSON string
scored_point_instance = ScoredPoint.from_json(json)
# print the JSON string representation of the object
print ScoredPoint.to_json()

# convert the object into a dict
scored_point_dict = scored_point_instance.to_dict()
# create an instance of ScoredPoint from a dict
scored_point_form_dict = scored_point.from_dict(scored_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


