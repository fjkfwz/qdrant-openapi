# ConsensusThreadStatus

Information about current consensus thread status

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consensus_thread_status** | **str** |  | 
**last_update** | **datetime** |  | 
**err** | **str** |  | 

## Example

```python
from qdrant_openapi.models.consensus_thread_status import ConsensusThreadStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ConsensusThreadStatus from a JSON string
consensus_thread_status_instance = ConsensusThreadStatus.from_json(json)
# print the JSON string representation of the object
print ConsensusThreadStatus.to_json()

# convert the object into a dict
consensus_thread_status_dict = consensus_thread_status_instance.to_dict()
# create an instance of ConsensusThreadStatus from a dict
consensus_thread_status_form_dict = consensus_thread_status.from_dict(consensus_thread_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


