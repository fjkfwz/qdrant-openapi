# CollectionParamsDiff


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_factor** | **int** | Number of replicas for each shard | [optional] 
**write_consistency_factor** | **int** | Minimal number successful responses from replicas to consider operation successful | [optional] 
**read_fan_out_factor** | **int** | Fan-out every read request to these many additional remote nodes (and return first available response) | [optional] 
**on_disk_payload** | **bool** | If true - point&#39;s payload will not be stored in memory. It will be read from the disk every time it is requested. This setting saves RAM by (slightly) increasing the response time. Note: those payload values that are involved in filtering and are indexed - remain in RAM. | [optional] 

## Example

```python
from openapi_client.models.collection_params_diff import CollectionParamsDiff

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionParamsDiff from a JSON string
collection_params_diff_instance = CollectionParamsDiff.from_json(json)
# print the JSON string representation of the object
print CollectionParamsDiff.to_json()

# convert the object into a dict
collection_params_diff_dict = collection_params_diff_instance.to_dict()
# create an instance of CollectionParamsDiff from a dict
collection_params_diff_form_dict = collection_params_diff.from_dict(collection_params_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


