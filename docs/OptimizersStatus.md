# OptimizersStatus

Current state of the collection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 

## Example

```python
from qdrant_openapi.models.optimizers_status import OptimizersStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizersStatus from a JSON string
optimizers_status_instance = OptimizersStatus.from_json(json)
# print the JSON string representation of the object
print OptimizersStatus.to_json()

# convert the object into a dict
optimizers_status_dict = optimizers_status_instance.to_dict()
# create an instance of OptimizersStatus from a dict
optimizers_status_form_dict = optimizers_status.from_dict(optimizers_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


