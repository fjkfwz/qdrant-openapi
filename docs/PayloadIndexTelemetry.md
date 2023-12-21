# PayloadIndexTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | [optional] 
**points_values_count** | **int** |  | 
**points_count** | **int** |  | 
**histogram_bucket_size** | **int** |  | [optional] 

## Example

```python
from qdrant_openapi.models.payload_index_telemetry import PayloadIndexTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadIndexTelemetry from a JSON string
payload_index_telemetry_instance = PayloadIndexTelemetry.from_json(json)
# print the JSON string representation of the object
print PayloadIndexTelemetry.to_json()

# convert the object into a dict
payload_index_telemetry_dict = payload_index_telemetry_instance.to_dict()
# create an instance of PayloadIndexTelemetry from a dict
payload_index_telemetry_form_dict = payload_index_telemetry.from_dict(payload_index_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


