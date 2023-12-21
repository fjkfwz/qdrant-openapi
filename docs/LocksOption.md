# LocksOption


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** |  | [optional] 
**write** | **bool** |  | 

## Example

```python
from qdrant_openapi.models.locks_option import LocksOption

# TODO update the JSON string below
json = "{}"
# create an instance of LocksOption from a JSON string
locks_option_instance = LocksOption.from_json(json)
# print the JSON string representation of the object
print LocksOption.to_json()

# convert the object into a dict
locks_option_dict = locks_option_instance.to_dict()
# create an instance of LocksOption from a dict
locks_option_form_dict = locks_option.from_dict(locks_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


