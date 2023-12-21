# TextIndexParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TextIndexType**](TextIndexType.md) |  | 
**tokenizer** | [**TokenizerType**](TokenizerType.md) |  | [optional] 
**min_token_len** | **int** |  | [optional] 
**max_token_len** | **int** |  | [optional] 
**lowercase** | **bool** | If true, lowercase all tokens. Default: true | [optional] 

## Example

```python
from qdrant_openapi.models.text_index_params import TextIndexParams

# TODO update the JSON string below
json = "{}"
# create an instance of TextIndexParams from a JSON string
text_index_params_instance = TextIndexParams.from_json(json)
# print the JSON string representation of the object
print TextIndexParams.to_json()

# convert the object into a dict
text_index_params_dict = text_index_params_instance.to_dict()
# create an instance of TextIndexParams from a dict
text_index_params_form_dict = text_index_params.from_dict(text_index_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


