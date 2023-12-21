# VectorIndexSearchesTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index_name** | **str** |  | [optional] 
**unfiltered_plain** | [**OperationDurationStatistics**](OperationDurationStatistics.md) |  | 
**unfiltered_hnsw** | [**OperationDurationStatistics**](OperationDurationStatistics.md) |  | 
**unfiltered_sparse** | [**OperationDurationStatistics**](OperationDurationStatistics.md) |  | 
**filtered_plain** | [**OperationDurationStatistics**](OperationDurationStatistics.md) |  | 
**filtered_small_cardinality** | [**OperationDurationStatistics**](OperationDurationStatistics.md) |  | 
**filtered_large_cardinality** | [**OperationDurationStatistics**](OperationDurationStatistics.md) |  | 
**filtered_exact** | [**OperationDurationStatistics**](OperationDurationStatistics.md) |  | 
**filtered_sparse** | [**OperationDurationStatistics**](OperationDurationStatistics.md) |  | 
**unfiltered_exact** | [**OperationDurationStatistics**](OperationDurationStatistics.md) |  | 

## Example

```python
from openapi_client.models.vector_index_searches_telemetry import VectorIndexSearchesTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of VectorIndexSearchesTelemetry from a JSON string
vector_index_searches_telemetry_instance = VectorIndexSearchesTelemetry.from_json(json)
# print the JSON string representation of the object
print VectorIndexSearchesTelemetry.to_json()

# convert the object into a dict
vector_index_searches_telemetry_dict = vector_index_searches_telemetry_instance.to_dict()
# create an instance of VectorIndexSearchesTelemetry from a dict
vector_index_searches_telemetry_form_dict = vector_index_searches_telemetry.from_dict(vector_index_searches_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


