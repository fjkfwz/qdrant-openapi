# Range

Range filter request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lt** | **float** | point.key &lt; range.lt | [optional] 
**gt** | **float** | point.key &gt; range.gt | [optional] 
**gte** | **float** | point.key &gt;&#x3D; range.gte | [optional] 
**lte** | **float** | point.key &lt;&#x3D; range.lte | [optional] 

## Example

```python
from openapi_client.models.range import Range

# TODO update the JSON string below
json = "{}"
# create an instance of Range from a JSON string
range_instance = Range.from_json(json)
# print the JSON string representation of the object
print Range.to_json()

# convert the object into a dict
range_dict = range_instance.to_dict()
# create an instance of Range from a dict
range_form_dict = range.from_dict(range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


