# SnapshotDescription


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**creation_time** | **str** |  | [optional] 
**size** | **int** |  | 

## Example

```python
from openapi_client.models.snapshot_description import SnapshotDescription

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotDescription from a JSON string
snapshot_description_instance = SnapshotDescription.from_json(json)
# print the JSON string representation of the object
print SnapshotDescription.to_json()

# convert the object into a dict
snapshot_description_dict = snapshot_description_instance.to_dict()
# create an instance of SnapshotDescription from a dict
snapshot_description_form_dict = snapshot_description.from_dict(snapshot_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


