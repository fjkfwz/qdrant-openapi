# SearchParams

Additional parameters of the search

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hnsw_ef** | **int** | Params relevant to HNSW index Size of the beam in a beam-search. Larger the value - more accurate the result, more time required for search. | [optional] 
**exact** | **bool** | Search without approximation. If set to true, search may run long but with exact results. | [optional] [default to False]
**quantization** | [**QuantizationSearchParams**](QuantizationSearchParams.md) |  | [optional] 
**indexed_only** | **bool** | If enabled, the engine will only perform search among indexed or small segments. Using this option prevents slow searches in case of delayed index, but does not guarantee that all uploaded vectors will be included in search results | [optional] [default to False]

## Example

```python
from qdrant_openapi.models.search_params import SearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of SearchParams from a JSON string
search_params_instance = SearchParams.from_json(json)
# print the JSON string representation of the object
print SearchParams.to_json()

# convert the object into a dict
search_params_dict = search_params_instance.to_dict()
# create an instance of SearchParams from a dict
search_params_form_dict = search_params.from_dict(search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


