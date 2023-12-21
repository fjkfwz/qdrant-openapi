# GeoPolygon

Geo filter request  Matches coordinates inside the polygon, defined by `exterior` and `interiors`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exterior** | [**GeoLineString**](GeoLineString.md) |  | 
**interiors** | [**List[GeoLineString]**](GeoLineString.md) | Interior lines (if present) bound holes within the surface each GeoLineString must consist of a minimum of 4 points, and the first and last points must be the same. | [optional] 

## Example

```python
from openapi_client.models.geo_polygon import GeoPolygon

# TODO update the JSON string below
json = "{}"
# create an instance of GeoPolygon from a JSON string
geo_polygon_instance = GeoPolygon.from_json(json)
# print the JSON string representation of the object
print GeoPolygon.to_json()

# convert the object into a dict
geo_polygon_dict = geo_polygon_instance.to_dict()
# create an instance of GeoPolygon from a dict
geo_polygon_form_dict = geo_polygon.from_dict(geo_polygon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


