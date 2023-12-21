# VectorDataInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_vectors** | **int** |  | 
**num_indexed_vectors** | **int** |  | 
**num_deleted_vectors** | **int** |  | 

## Example

```python
from qdrant_openapi.models.vector_data_info import VectorDataInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VectorDataInfo from a JSON string
vector_data_info_instance = VectorDataInfo.from_json(json)
# print the JSON string representation of the object
print VectorDataInfo.to_json()

# convert the object into a dict
vector_data_info_dict = vector_data_info_instance.to_dict()
# create an instance of VectorDataInfo from a dict
vector_data_info_form_dict = vector_data_info.from_dict(vector_data_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


