# WalConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wal_capacity_mb** | **int** | Size of a single WAL segment in MB | 
**wal_segments_ahead** | **int** | Number of WAL segments to create ahead of actually used ones | 

## Example

```python
from qdrant_openapi.models.wal_config import WalConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WalConfig from a JSON string
wal_config_instance = WalConfig.from_json(json)
# print the JSON string representation of the object
print WalConfig.to_json()

# convert the object into a dict
wal_config_dict = wal_config_instance.to_dict()
# create an instance of WalConfig from a dict
wal_config_form_dict = wal_config.from_dict(wal_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


