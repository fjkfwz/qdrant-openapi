# SnapshotRecover


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Examples: - URL &#x60;http://localhost:8080/collections/my_collection/snapshots/my_snapshot&#x60; - Local path &#x60;file:///qdrant/snapshots/test_collection-2022-08-04-10-49-10.snapshot&#x60; | 
**priority** | [**SnapshotPriority**](SnapshotPriority.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.snapshot_recover import SnapshotRecover

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotRecover from a JSON string
snapshot_recover_instance = SnapshotRecover.from_json(json)
# print the JSON string representation of the object
print SnapshotRecover.to_json()

# convert the object into a dict
snapshot_recover_dict = snapshot_recover_instance.to_dict()
# create an instance of SnapshotRecover from a dict
snapshot_recover_form_dict = snapshot_recover.from_dict(snapshot_recover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


