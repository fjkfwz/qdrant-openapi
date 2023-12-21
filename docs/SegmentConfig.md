# SegmentConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vector_data** | [**Dict[str, VectorDataConfig]**](VectorDataConfig.md) |  | [optional] 
**sparse_vector_data** | [**Dict[str, SparseVectorDataConfig]**](SparseVectorDataConfig.md) |  | [optional] 
**payload_storage_type** | [**PayloadStorageType**](PayloadStorageType.md) |  | 

## Example

```python
from openapi_client.models.segment_config import SegmentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentConfig from a JSON string
segment_config_instance = SegmentConfig.from_json(json)
# print the JSON string representation of the object
print SegmentConfig.to_json()

# convert the object into a dict
segment_config_dict = segment_config_instance.to_dict()
# create an instance of SegmentConfig from a dict
segment_config_form_dict = segment_config.from_dict(segment_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


