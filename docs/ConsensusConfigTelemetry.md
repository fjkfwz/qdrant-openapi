# ConsensusConfigTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_message_queue_size** | **int** |  | 
**tick_period_ms** | **int** |  | 
**bootstrap_timeout_sec** | **int** |  | 

## Example

```python
from qdrant_openapi.models.consensus_config_telemetry import ConsensusConfigTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of ConsensusConfigTelemetry from a JSON string
consensus_config_telemetry_instance = ConsensusConfigTelemetry.from_json(json)
# print the JSON string representation of the object
print ConsensusConfigTelemetry.to_json()

# convert the object into a dict
consensus_config_telemetry_dict = consensus_config_telemetry_instance.to_dict()
# create an instance of ConsensusConfigTelemetry from a dict
consensus_config_telemetry_form_dict = consensus_config_telemetry.from_dict(consensus_config_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


