# PointsBatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch** | [**Batch**](Batch.md) |  | 
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 

## Example

```python
from openapi_client.models.points_batch import PointsBatch

# TODO update the JSON string below
json = "{}"
# create an instance of PointsBatch from a JSON string
points_batch_instance = PointsBatch.from_json(json)
# print the JSON string representation of the object
print PointsBatch.to_json()

# convert the object into a dict
points_batch_dict = points_batch_instance.to_dict()
# create an instance of PointsBatch from a dict
points_batch_form_dict = points_batch.from_dict(points_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


