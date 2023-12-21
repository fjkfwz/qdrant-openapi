# UpdateVectors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | [**List[PointVectors]**](PointVectors.md) | Points with named vectors | 
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_vectors import UpdateVectors

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVectors from a JSON string
update_vectors_instance = UpdateVectors.from_json(json)
# print the JSON string representation of the object
print UpdateVectors.to_json()

# convert the object into a dict
update_vectors_dict = update_vectors_instance.to_dict()
# create an instance of UpdateVectors from a dict
update_vectors_form_dict = update_vectors.from_dict(update_vectors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


