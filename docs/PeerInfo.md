# PeerInfo

Information of a peer in the cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | 

## Example

```python
from openapi_client.models.peer_info import PeerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PeerInfo from a JSON string
peer_info_instance = PeerInfo.from_json(json)
# print the JSON string representation of the object
print PeerInfo.to_json()

# convert the object into a dict
peer_info_dict = peer_info_instance.to_dict()
# create an instance of PeerInfo from a dict
peer_info_form_dict = peer_info.from_dict(peer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


