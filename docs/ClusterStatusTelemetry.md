# ClusterStatusTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_peers** | **int** |  | 
**term** | **int** |  | 
**commit** | **int** |  | 
**pending_operations** | **int** |  | 
**role** | [**StateRole**](StateRole.md) |  | [optional] 
**is_voter** | **bool** |  | 
**peer_id** | **int** |  | [optional] 
**consensus_thread_status** | [**ConsensusThreadStatus**](ConsensusThreadStatus.md) |  | 

## Example

```python
from openapi_client.models.cluster_status_telemetry import ClusterStatusTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStatusTelemetry from a JSON string
cluster_status_telemetry_instance = ClusterStatusTelemetry.from_json(json)
# print the JSON string representation of the object
print ClusterStatusTelemetry.to_json()

# convert the object into a dict
cluster_status_telemetry_dict = cluster_status_telemetry_instance.to_dict()
# create an instance of ClusterStatusTelemetry from a dict
cluster_status_telemetry_form_dict = cluster_status_telemetry.from_dict(cluster_status_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


