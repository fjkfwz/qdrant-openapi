# RaftInfo

Summary information about the current raft state

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **int** | Raft divides time into terms of arbitrary length, each beginning with an election. If a candidate wins the election, it remains the leader for the rest of the term. The term number increases monotonically. Each server stores the current term number which is also exchanged in every communication. | 
**commit** | **int** | The index of the latest committed (finalized) operation that this peer is aware of. | 
**pending_operations** | **int** | Number of consensus operations pending to be applied on this peer | 
**leader** | **int** | Leader of the current term | [optional] 
**role** | [**StateRole**](StateRole.md) |  | [optional] 
**is_voter** | **bool** | Is this peer a voter or a learner | 

## Example

```python
from openapi_client.models.raft_info import RaftInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RaftInfo from a JSON string
raft_info_instance = RaftInfo.from_json(json)
# print the JSON string representation of the object
print RaftInfo.to_json()

# convert the object into a dict
raft_info_dict = raft_info_instance.to_dict()
# create an instance of RaftInfo from a dict
raft_info_form_dict = raft_info.from_dict(raft_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


