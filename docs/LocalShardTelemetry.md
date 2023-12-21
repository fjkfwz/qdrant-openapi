# LocalShardTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variant_name** | **str** |  | [optional] 
**segments** | [**List[SegmentTelemetry]**](SegmentTelemetry.md) |  | 
**optimizations** | [**OptimizerTelemetry**](OptimizerTelemetry.md) |  | 

## Example

```python
from openapi_client.models.local_shard_telemetry import LocalShardTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of LocalShardTelemetry from a JSON string
local_shard_telemetry_instance = LocalShardTelemetry.from_json(json)
# print the JSON string representation of the object
print LocalShardTelemetry.to_json()

# convert the object into a dict
local_shard_telemetry_dict = local_shard_telemetry_instance.to_dict()
# create an instance of LocalShardTelemetry from a dict
local_shard_telemetry_form_dict = local_shard_telemetry.from_dict(local_shard_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


