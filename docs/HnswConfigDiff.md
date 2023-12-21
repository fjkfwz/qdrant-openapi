# HnswConfigDiff


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m** | **int** | Number of edges per node in the index graph. Larger the value - more accurate the search, more space required. | [optional] 
**ef_construct** | **int** | Number of neighbours to consider during the index building. Larger the value - more accurate the search, more time required to build the index. | [optional] 
**full_scan_threshold** | **int** | Minimal size (in kilobytes) of vectors for additional payload-based indexing. If payload chunk is smaller than &#x60;full_scan_threshold_kb&#x60; additional indexing won&#39;t be used - in this case full-scan search should be preferred by query planner and additional indexing is not required. Note: 1Kb &#x3D; 1 vector of size 256 | [optional] 
**max_indexing_threads** | **int** | Number of parallel threads used for background index building. If 0 - auto selection. | [optional] 
**on_disk** | **bool** | Store HNSW index on disk. If set to false, the index will be stored in RAM. Default: false | [optional] 
**payload_m** | **int** | Custom M param for additional payload-aware HNSW links. If not set, default M will be used. | [optional] 

## Example

```python
from openapi_client.models.hnsw_config_diff import HnswConfigDiff

# TODO update the JSON string below
json = "{}"
# create an instance of HnswConfigDiff from a JSON string
hnsw_config_diff_instance = HnswConfigDiff.from_json(json)
# print the JSON string representation of the object
print HnswConfigDiff.to_json()

# convert the object into a dict
hnsw_config_diff_dict = hnsw_config_diff_instance.to_dict()
# create an instance of HnswConfigDiff from a dict
hnsw_config_diff_form_dict = hnsw_config_diff.from_dict(hnsw_config_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


