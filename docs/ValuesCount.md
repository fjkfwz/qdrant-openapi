# ValuesCount

Values count filter request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lt** | **int** | point.key.length() &lt; values_count.lt | [optional] 
**gt** | **int** | point.key.length() &gt; values_count.gt | [optional] 
**gte** | **int** | point.key.length() &gt;&#x3D; values_count.gte | [optional] 
**lte** | **int** | point.key.length() &lt;&#x3D; values_count.lte | [optional] 

## Example

```python
from qdrant_openapi.models.values_count import ValuesCount

# TODO update the JSON string below
json = "{}"
# create an instance of ValuesCount from a JSON string
values_count_instance = ValuesCount.from_json(json)
# print the JSON string representation of the object
print ValuesCount.to_json()

# convert the object into a dict
values_count_dict = values_count_instance.to_dict()
# create an instance of ValuesCount from a dict
values_count_form_dict = values_count.from_dict(values_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


