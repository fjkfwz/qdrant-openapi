# ClusterConfigTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grpc_timeout_ms** | **int** |  | 
**p2p** | [**P2pConfigTelemetry**](P2pConfigTelemetry.md) |  | 
**consensus** | [**ConsensusConfigTelemetry**](ConsensusConfigTelemetry.md) |  | 

## Example

```python
from openapi_client.models.cluster_config_telemetry import ClusterConfigTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterConfigTelemetry from a JSON string
cluster_config_telemetry_instance = ClusterConfigTelemetry.from_json(json)
# print the JSON string representation of the object
print ClusterConfigTelemetry.to_json()

# convert the object into a dict
cluster_config_telemetry_dict = cluster_config_telemetry_instance.to_dict()
# create an instance of ClusterConfigTelemetry from a dict
cluster_config_telemetry_form_dict = cluster_config_telemetry.from_dict(cluster_config_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


