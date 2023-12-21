# SegmentInfo

Aggregated information about segment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**segment_type** | [**SegmentType**](SegmentType.md) |  | 
**num_vectors** | **int** |  | 
**num_points** | **int** |  | 
**num_indexed_vectors** | **int** |  | 
**num_deleted_vectors** | **int** |  | 
**ram_usage_bytes** | **int** |  | 
**disk_usage_bytes** | **int** |  | 
**is_appendable** | **bool** |  | 
**index_schema** | [**Dict[str, PayloadIndexInfo]**](PayloadIndexInfo.md) |  | 
**vector_data** | [**Dict[str, VectorDataInfo]**](VectorDataInfo.md) |  | 

## Example

```python
from qdrant_openapi.models.segment_info import SegmentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentInfo from a JSON string
segment_info_instance = SegmentInfo.from_json(json)
# print the JSON string representation of the object
print SegmentInfo.to_json()

# convert the object into a dict
segment_info_dict = segment_info_instance.to_dict()
# create an instance of SegmentInfo from a dict
segment_info_form_dict = segment_info.from_dict(segment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


