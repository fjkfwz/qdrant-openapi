# HnswConfig

Config of HNSW index

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m** | **int** | Number of edges per node in the index graph. Larger the value - more accurate the search, more space required. | 
**ef_construct** | **int** | Number of neighbours to consider during the index building. Larger the value - more accurate the search, more time required to build index. | 
**full_scan_threshold** | **int** | Minimal size (in KiloBytes) of vectors for additional payload-based indexing. If payload chunk is smaller than &#x60;full_scan_threshold_kb&#x60; additional indexing won&#39;t be used - in this case full-scan search should be preferred by query planner and additional indexing is not required. Note: 1Kb &#x3D; 1 vector of size 256 | 
**max_indexing_threads** | **int** | Number of parallel threads used for background index building. If 0 - auto selection. | [optional] [default to 0]
**on_disk** | **bool** | Store HNSW index on disk. If set to false, index will be stored in RAM. Default: false | [optional] 
**payload_m** | **int** | Custom M param for hnsw graph built for payload index. If not set, default M will be used. | [optional] 

## Example

```python
from qdrant_openapi.models.hnsw_config import HnswConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HnswConfig from a JSON string
hnsw_config_instance = HnswConfig.from_json(json)
# print the JSON string representation of the object
print HnswConfig.to_json()

# convert the object into a dict
hnsw_config_dict = hnsw_config_instance.to_dict()
# create an instance of HnswConfig from a dict
hnsw_config_form_dict = hnsw_config.from_dict(hnsw_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


