# ClusterStatusOneOf1

Description of enabled cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**peer_id** | **int** | ID of this peer | 
**peers** | [**Dict[str, PeerInfo]**](PeerInfo.md) | Peers composition of the cluster with main information | 
**raft_info** | [**RaftInfo**](RaftInfo.md) |  | 
**consensus_thread_status** | [**ConsensusThreadStatus**](ConsensusThreadStatus.md) |  | 
**message_send_failures** | [**Dict[str, MessageSendErrors]**](MessageSendErrors.md) | Consequent failures of message send operations in consensus by peer address. On the first success to send to that peer - entry is removed from this hashmap. | 

## Example

```python
from qdrant_openapi.models.cluster_status_one_of1 import ClusterStatusOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStatusOneOf1 from a JSON string
cluster_status_one_of1_instance = ClusterStatusOneOf1.from_json(json)
# print the JSON string representation of the object
print ClusterStatusOneOf1.to_json()

# convert the object into a dict
cluster_status_one_of1_dict = cluster_status_one_of1_instance.to_dict()
# create an instance of ClusterStatusOneOf1 from a dict
cluster_status_one_of1_form_dict = cluster_status_one_of1.from_dict(cluster_status_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


