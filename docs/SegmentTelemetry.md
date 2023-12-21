# SegmentTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**SegmentInfo**](SegmentInfo.md) |  | 
**config** | [**SegmentConfig**](SegmentConfig.md) |  | 
**vector_index_searches** | [**List[VectorIndexSearchesTelemetry]**](VectorIndexSearchesTelemetry.md) |  | 
**payload_field_indices** | [**List[PayloadIndexTelemetry]**](PayloadIndexTelemetry.md) |  | 

## Example

```python
from qdrant_openapi.models.segment_telemetry import SegmentTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentTelemetry from a JSON string
segment_telemetry_instance = SegmentTelemetry.from_json(json)
# print the JSON string representation of the object
print SegmentTelemetry.to_json()

# convert the object into a dict
segment_telemetry_dict = segment_telemetry_instance.to_dict()
# create an instance of SegmentTelemetry from a dict
segment_telemetry_form_dict = segment_telemetry.from_dict(segment_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


