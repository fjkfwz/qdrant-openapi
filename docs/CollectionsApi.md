# qdrant_openapi.CollectionsApi

All URIs are relative to *http://localhost:6333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collection_cluster_info**](CollectionsApi.md#collection_cluster_info) | **GET** /collections/{collection_name}/cluster | Collection cluster info
[**create_collection**](CollectionsApi.md#create_collection) | **PUT** /collections/{collection_name} | Create collection
[**create_field_index**](CollectionsApi.md#create_field_index) | **PUT** /collections/{collection_name}/index | Create index for field in collection
[**create_shard_key**](CollectionsApi.md#create_shard_key) | **PUT** /collections/{collection_name}/shards | Create shard key
[**create_shard_snapshot**](CollectionsApi.md#create_shard_snapshot) | **POST** /collections/{collection_name}/shards/{shard_id}/snapshots | Create shard snapshot
[**create_snapshot**](CollectionsApi.md#create_snapshot) | **POST** /collections/{collection_name}/snapshots | Create collection snapshot
[**delete_collection**](CollectionsApi.md#delete_collection) | **DELETE** /collections/{collection_name} | Delete collection
[**delete_field_index**](CollectionsApi.md#delete_field_index) | **DELETE** /collections/{collection_name}/index/{field_name} | Delete index for field in collection
[**delete_shard_key**](CollectionsApi.md#delete_shard_key) | **POST** /collections/{collection_name}/shards/delete | Delete shard key
[**delete_shard_snapshot**](CollectionsApi.md#delete_shard_snapshot) | **DELETE** /collections/{collection_name}/shards/{shard_id}/snapshots/{snapshot_name} | Delete shard snapshot
[**delete_snapshot**](CollectionsApi.md#delete_snapshot) | **DELETE** /collections/{collection_name}/snapshots/{snapshot_name} | Delete collection snapshot
[**get_collection**](CollectionsApi.md#get_collection) | **GET** /collections/{collection_name} | Collection info
[**get_collection_aliases**](CollectionsApi.md#get_collection_aliases) | **GET** /collections/{collection_name}/aliases | List aliases for collection
[**get_collections**](CollectionsApi.md#get_collections) | **GET** /collections | List collections
[**get_collections_aliases**](CollectionsApi.md#get_collections_aliases) | **GET** /aliases | List collections aliases
[**get_shard_snapshot**](CollectionsApi.md#get_shard_snapshot) | **GET** /collections/{collection_name}/shards/{shard_id}/snapshots/{snapshot_name} | Download collection snapshot
[**get_snapshot**](CollectionsApi.md#get_snapshot) | **GET** /collections/{collection_name}/snapshots/{snapshot_name} | Download collection snapshot
[**list_shard_snapshots**](CollectionsApi.md#list_shard_snapshots) | **GET** /collections/{collection_name}/shards/{shard_id}/snapshots | List shards snapshots for a collection
[**list_snapshots**](CollectionsApi.md#list_snapshots) | **GET** /collections/{collection_name}/snapshots | List collection snapshots
[**recover_from_snapshot**](CollectionsApi.md#recover_from_snapshot) | **PUT** /collections/{collection_name}/snapshots/recover | Recover from a snapshot
[**recover_from_uploaded_snapshot**](CollectionsApi.md#recover_from_uploaded_snapshot) | **POST** /collections/{collection_name}/snapshots/upload | Recover from an uploaded snapshot
[**recover_shard_from_snapshot**](CollectionsApi.md#recover_shard_from_snapshot) | **PUT** /collections/{collection_name}/shards/{shard_id}/snapshots/recover | Recover from a snapshot
[**recover_shard_from_uploaded_snapshot**](CollectionsApi.md#recover_shard_from_uploaded_snapshot) | **POST** /collections/{collection_name}/shards/{shard_id}/snapshots/upload | Recover shard from an uploaded snapshot
[**update_aliases**](CollectionsApi.md#update_aliases) | **POST** /collections/aliases | Update aliases of the collections
[**update_collection**](CollectionsApi.md#update_collection) | **PATCH** /collections/{collection_name} | Update collection parameters
[**update_collection_cluster**](CollectionsApi.md#update_collection_cluster) | **POST** /collections/{collection_name}/cluster | Update collection cluster setup


# **collection_cluster_info**
> CollectionClusterInfo200Response collection_cluster_info(collection_name)

Collection cluster info

Get cluster information for a collection

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.collection_cluster_info200_response import CollectionClusterInfo200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to retrieve the cluster info for

    try:
        # Collection cluster info
        api_response = api_instance.collection_cluster_info(collection_name)
        print("The response of CollectionsApi->collection_cluster_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collection_cluster_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to retrieve the cluster info for | 

### Return type

[**CollectionClusterInfo200Response**](CollectionClusterInfo200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_collection**
> CreateShardKey200Response create_collection(collection_name, timeout=timeout, create_collection=create_collection)

Create collection

Create new collection with given parameters

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_collection import CreateCollection
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the new collection
    timeout = 56 # int | Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  (optional)
    create_collection = qdrant_openapi.CreateCollection() # CreateCollection | Parameters of a new collection (optional)

    try:
        # Create collection
        api_response = api_instance.create_collection(collection_name, timeout=timeout, create_collection=create_collection)
        print("The response of CollectionsApi->create_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->create_collection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the new collection | 
 **timeout** | **int**| Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  | [optional] 
 **create_collection** | [**CreateCollection**](CreateCollection.md)| Parameters of a new collection | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_field_index**
> CreateFieldIndex200Response create_field_index(collection_name, wait=wait, ordering=ordering, create_field_index=create_field_index)

Create index for field in collection

Create index for field in collection

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_field_index import CreateFieldIndex
from qdrant_openapi.models.create_field_index200_response import CreateFieldIndex200Response
from qdrant_openapi.models.write_ordering import WriteOrdering
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    wait = True # bool | If true, wait for changes to actually happen (optional)
    ordering = qdrant_openapi.WriteOrdering() # WriteOrdering | define ordering guarantees for the operation (optional)
    create_field_index = qdrant_openapi.CreateFieldIndex() # CreateFieldIndex | Field name (optional)

    try:
        # Create index for field in collection
        api_response = api_instance.create_field_index(collection_name, wait=wait, ordering=ordering, create_field_index=create_field_index)
        print("The response of CollectionsApi->create_field_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->create_field_index: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection | 
 **wait** | **bool**| If true, wait for changes to actually happen | [optional] 
 **ordering** | [**WriteOrdering**](.md)| define ordering guarantees for the operation | [optional] 
 **create_field_index** | [**CreateFieldIndex**](CreateFieldIndex.md)| Field name | [optional] 

### Return type

[**CreateFieldIndex200Response**](CreateFieldIndex200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shard_key**
> CreateShardKey200Response create_shard_key(collection_name, timeout=timeout, create_sharding_key=create_sharding_key)

Create shard key

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.models.create_sharding_key import CreateShardingKey
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to create shards for
    timeout = 56 # int | Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  (optional)
    create_sharding_key = qdrant_openapi.CreateShardingKey() # CreateShardingKey | Shard key configuration (optional)

    try:
        # Create shard key
        api_response = api_instance.create_shard_key(collection_name, timeout=timeout, create_sharding_key=create_sharding_key)
        print("The response of CollectionsApi->create_shard_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->create_shard_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to create shards for | 
 **timeout** | **int**| Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  | [optional] 
 **create_sharding_key** | [**CreateShardingKey**](CreateShardingKey.md)| Shard key configuration | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shard_snapshot**
> CreateSnapshot200Response create_shard_snapshot(collection_name, shard_id, wait=wait)

Create shard snapshot

Create new snapshot of a shard for a collection

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_snapshot200_response import CreateSnapshot200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection for which to create a snapshot
    shard_id = 56 # int | Id of the shard
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)

    try:
        # Create shard snapshot
        api_response = api_instance.create_shard_snapshot(collection_name, shard_id, wait=wait)
        print("The response of CollectionsApi->create_shard_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->create_shard_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection for which to create a snapshot | 
 **shard_id** | **int**| Id of the shard | 
 **wait** | **bool**| If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. | [optional] 

### Return type

[**CreateSnapshot200Response**](CreateSnapshot200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**202** | operation is accepted |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot**
> CreateSnapshot200Response create_snapshot(collection_name, wait=wait)

Create collection snapshot

Create new snapshot for a collection

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_snapshot200_response import CreateSnapshot200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection for which to create a snapshot
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)

    try:
        # Create collection snapshot
        api_response = api_instance.create_snapshot(collection_name, wait=wait)
        print("The response of CollectionsApi->create_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->create_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection for which to create a snapshot | 
 **wait** | **bool**| If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. | [optional] 

### Return type

[**CreateSnapshot200Response**](CreateSnapshot200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**202** | operation is accepted |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection**
> CreateShardKey200Response delete_collection(collection_name, timeout=timeout)

Delete collection

Drop collection and all associated data

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to delete
    timeout = 56 # int | Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  (optional)

    try:
        # Delete collection
        api_response = api_instance.delete_collection(collection_name, timeout=timeout)
        print("The response of CollectionsApi->delete_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->delete_collection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to delete | 
 **timeout** | **int**| Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_field_index**
> CreateFieldIndex200Response delete_field_index(collection_name, field_name, wait=wait, ordering=ordering)

Delete index for field in collection

Delete field index for collection

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_field_index200_response import CreateFieldIndex200Response
from qdrant_openapi.models.write_ordering import WriteOrdering
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    field_name = 'field_name_example' # str | Name of the field where to delete the index
    wait = True # bool | If true, wait for changes to actually happen (optional)
    ordering = qdrant_openapi.WriteOrdering() # WriteOrdering | define ordering guarantees for the operation (optional)

    try:
        # Delete index for field in collection
        api_response = api_instance.delete_field_index(collection_name, field_name, wait=wait, ordering=ordering)
        print("The response of CollectionsApi->delete_field_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->delete_field_index: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection | 
 **field_name** | **str**| Name of the field where to delete the index | 
 **wait** | **bool**| If true, wait for changes to actually happen | [optional] 
 **ordering** | [**WriteOrdering**](.md)| define ordering guarantees for the operation | [optional] 

### Return type

[**CreateFieldIndex200Response**](CreateFieldIndex200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shard_key**
> CreateShardKey200Response delete_shard_key(collection_name, timeout=timeout, drop_sharding_key=drop_sharding_key)

Delete shard key

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.models.drop_sharding_key import DropShardingKey
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to create shards for
    timeout = 56 # int | Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  (optional)
    drop_sharding_key = qdrant_openapi.DropShardingKey() # DropShardingKey | Select shard key to delete (optional)

    try:
        # Delete shard key
        api_response = api_instance.delete_shard_key(collection_name, timeout=timeout, drop_sharding_key=drop_sharding_key)
        print("The response of CollectionsApi->delete_shard_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->delete_shard_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to create shards for | 
 **timeout** | **int**| Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  | [optional] 
 **drop_sharding_key** | [**DropShardingKey**](DropShardingKey.md)| Select shard key to delete | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shard_snapshot**
> CreateShardKey200Response delete_shard_snapshot(collection_name, shard_id, snapshot_name, wait=wait)

Delete shard snapshot

Delete snapshot of a shard for a collection

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection for which to delete a snapshot
    shard_id = 56 # int | Id of the shard
    snapshot_name = 'snapshot_name_example' # str | Name of the snapshot to delete
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)

    try:
        # Delete shard snapshot
        api_response = api_instance.delete_shard_snapshot(collection_name, shard_id, snapshot_name, wait=wait)
        print("The response of CollectionsApi->delete_shard_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->delete_shard_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection for which to delete a snapshot | 
 **shard_id** | **int**| Id of the shard | 
 **snapshot_name** | **str**| Name of the snapshot to delete | 
 **wait** | **bool**| If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**202** | operation is accepted |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot**
> CreateShardKey200Response delete_snapshot(collection_name, snapshot_name, wait=wait)

Delete collection snapshot

Delete snapshot for a collection

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection for which to delete a snapshot
    snapshot_name = 'snapshot_name_example' # str | Name of the snapshot to delete
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)

    try:
        # Delete collection snapshot
        api_response = api_instance.delete_snapshot(collection_name, snapshot_name, wait=wait)
        print("The response of CollectionsApi->delete_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->delete_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection for which to delete a snapshot | 
 **snapshot_name** | **str**| Name of the snapshot to delete | 
 **wait** | **bool**| If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**202** | operation is accepted |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection**
> GetCollection200Response get_collection(collection_name)

Collection info

Get detailed information about specified existing collection

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.get_collection200_response import GetCollection200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to retrieve

    try:
        # Collection info
        api_response = api_instance.get_collection(collection_name)
        print("The response of CollectionsApi->get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->get_collection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to retrieve | 

### Return type

[**GetCollection200Response**](GetCollection200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_aliases**
> GetCollectionAliases200Response get_collection_aliases(collection_name)

List aliases for collection

Get list of all aliases for a collection

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.get_collection_aliases200_response import GetCollectionAliases200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection

    try:
        # List aliases for collection
        api_response = api_instance.get_collection_aliases(collection_name)
        print("The response of CollectionsApi->get_collection_aliases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->get_collection_aliases: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection | 

### Return type

[**GetCollectionAliases200Response**](GetCollectionAliases200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collections**
> GetCollections200Response get_collections()

List collections

Get list name of all existing collections

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.get_collections200_response import GetCollections200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)

    try:
        # List collections
        api_response = api_instance.get_collections()
        print("The response of CollectionsApi->get_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->get_collections: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCollections200Response**](GetCollections200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collections_aliases**
> GetCollectionAliases200Response get_collections_aliases()

List collections aliases

Get list of all existing collections aliases

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.get_collection_aliases200_response import GetCollectionAliases200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)

    try:
        # List collections aliases
        api_response = api_instance.get_collections_aliases()
        print("The response of CollectionsApi->get_collections_aliases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->get_collections_aliases: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCollectionAliases200Response**](GetCollectionAliases200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shard_snapshot**
> bytearray get_shard_snapshot(collection_name, shard_id, snapshot_name)

Download collection snapshot

Download specified snapshot of a shard from a collection as a file

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    shard_id = 56 # int | Id of the shard
    snapshot_name = 'snapshot_name_example' # str | Name of the snapshot to download

    try:
        # Download collection snapshot
        api_response = api_instance.get_shard_snapshot(collection_name, shard_id, snapshot_name)
        print("The response of CollectionsApi->get_shard_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->get_shard_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection | 
 **shard_id** | **int**| Id of the shard | 
 **snapshot_name** | **str**| Name of the snapshot to download | 

### Return type

**bytearray**

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snapshot file |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot**
> bytearray get_snapshot(collection_name, snapshot_name)

Download collection snapshot

Download specified snapshot from a collection as a file

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    snapshot_name = 'snapshot_name_example' # str | Name of the snapshot to download

    try:
        # Download collection snapshot
        api_response = api_instance.get_snapshot(collection_name, snapshot_name)
        print("The response of CollectionsApi->get_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->get_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection | 
 **snapshot_name** | **str**| Name of the snapshot to download | 

### Return type

**bytearray**

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Snapshot file |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shard_snapshots**
> ListSnapshots200Response list_shard_snapshots(collection_name, shard_id)

List shards snapshots for a collection

Get list of snapshots for a shard of a collection

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.list_snapshots200_response import ListSnapshots200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    shard_id = 56 # int | Id of the shard

    try:
        # List shards snapshots for a collection
        api_response = api_instance.list_shard_snapshots(collection_name, shard_id)
        print("The response of CollectionsApi->list_shard_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->list_shard_snapshots: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection | 
 **shard_id** | **int**| Id of the shard | 

### Return type

[**ListSnapshots200Response**](ListSnapshots200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshots**
> ListSnapshots200Response list_snapshots(collection_name)

List collection snapshots

Get list of snapshots for a collection

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.list_snapshots200_response import ListSnapshots200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection

    try:
        # List collection snapshots
        api_response = api_instance.list_snapshots(collection_name)
        print("The response of CollectionsApi->list_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->list_snapshots: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection | 

### Return type

[**ListSnapshots200Response**](ListSnapshots200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recover_from_snapshot**
> CreateShardKey200Response recover_from_snapshot(collection_name, wait=wait, snapshot_recover=snapshot_recover)

Recover from a snapshot

Recover local collection data from a snapshot. This will overwrite any data, stored on this node, for the collection. If collection does not exist - it will be created.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.models.snapshot_recover import SnapshotRecover
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)
    snapshot_recover = qdrant_openapi.SnapshotRecover() # SnapshotRecover | Snapshot to recover from (optional)

    try:
        # Recover from a snapshot
        api_response = api_instance.recover_from_snapshot(collection_name, wait=wait, snapshot_recover=snapshot_recover)
        print("The response of CollectionsApi->recover_from_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->recover_from_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection | 
 **wait** | **bool**| If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. | [optional] 
 **snapshot_recover** | [**SnapshotRecover**](SnapshotRecover.md)| Snapshot to recover from | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**202** | operation is accepted |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recover_from_uploaded_snapshot**
> CreateShardKey200Response recover_from_uploaded_snapshot(collection_name, wait=wait, priority=priority, snapshot=snapshot)

Recover from an uploaded snapshot

Recover local collection data from an uploaded snapshot. This will overwrite any data, stored on this node, for the collection. If collection does not exist - it will be created.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.models.snapshot_priority import SnapshotPriority
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)
    priority = qdrant_openapi.SnapshotPriority() # SnapshotPriority | Defines source of truth for snapshot recovery (optional)
    snapshot = None # bytearray |  (optional)

    try:
        # Recover from an uploaded snapshot
        api_response = api_instance.recover_from_uploaded_snapshot(collection_name, wait=wait, priority=priority, snapshot=snapshot)
        print("The response of CollectionsApi->recover_from_uploaded_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->recover_from_uploaded_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection | 
 **wait** | **bool**| If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. | [optional] 
 **priority** | [**SnapshotPriority**](.md)| Defines source of truth for snapshot recovery | [optional] 
 **snapshot** | **bytearray**|  | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**202** | operation is accepted |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recover_shard_from_snapshot**
> CreateShardKey200Response recover_shard_from_snapshot(collection_name, shard_id, wait=wait, shard_snapshot_recover=shard_snapshot_recover)

Recover from a snapshot

Recover shard of a local collection data from a snapshot. This will overwrite any data, stored in this shard, for the collection.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.models.shard_snapshot_recover import ShardSnapshotRecover
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    shard_id = 56 # int | Id of the shard to recover
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)
    shard_snapshot_recover = qdrant_openapi.ShardSnapshotRecover() # ShardSnapshotRecover | Snapshot to recover from (optional)

    try:
        # Recover from a snapshot
        api_response = api_instance.recover_shard_from_snapshot(collection_name, shard_id, wait=wait, shard_snapshot_recover=shard_snapshot_recover)
        print("The response of CollectionsApi->recover_shard_from_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->recover_shard_from_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection | 
 **shard_id** | **int**| Id of the shard to recover | 
 **wait** | **bool**| If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. | [optional] 
 **shard_snapshot_recover** | [**ShardSnapshotRecover**](ShardSnapshotRecover.md)| Snapshot to recover from | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**202** | operation is accepted |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recover_shard_from_uploaded_snapshot**
> CreateShardKey200Response recover_shard_from_uploaded_snapshot(collection_name, shard_id, wait=wait, priority=priority, snapshot=snapshot)

Recover shard from an uploaded snapshot

Recover shard of a local collection from an uploaded snapshot. This will overwrite any data, stored on this node, for the collection shard.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.models.snapshot_priority import SnapshotPriority
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    shard_id = 56 # int | Id of the shard to recover
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)
    priority = qdrant_openapi.SnapshotPriority() # SnapshotPriority | Defines source of truth for snapshot recovery (optional)
    snapshot = None # bytearray |  (optional)

    try:
        # Recover shard from an uploaded snapshot
        api_response = api_instance.recover_shard_from_uploaded_snapshot(collection_name, shard_id, wait=wait, priority=priority, snapshot=snapshot)
        print("The response of CollectionsApi->recover_shard_from_uploaded_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->recover_shard_from_uploaded_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection | 
 **shard_id** | **int**| Id of the shard to recover | 
 **wait** | **bool**| If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. | [optional] 
 **priority** | [**SnapshotPriority**](.md)| Defines source of truth for snapshot recovery | [optional] 
 **snapshot** | **bytearray**|  | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**202** | operation is accepted |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_aliases**
> CreateShardKey200Response update_aliases(timeout=timeout, change_aliases_operation=change_aliases_operation)

Update aliases of the collections

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.change_aliases_operation import ChangeAliasesOperation
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    timeout = 56 # int | Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  (optional)
    change_aliases_operation = qdrant_openapi.ChangeAliasesOperation() # ChangeAliasesOperation | Alias update operations (optional)

    try:
        # Update aliases of the collections
        api_response = api_instance.update_aliases(timeout=timeout, change_aliases_operation=change_aliases_operation)
        print("The response of CollectionsApi->update_aliases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->update_aliases: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  | [optional] 
 **change_aliases_operation** | [**ChangeAliasesOperation**](ChangeAliasesOperation.md)| Alias update operations | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collection**
> CreateShardKey200Response update_collection(collection_name, timeout=timeout, update_collection=update_collection)

Update collection parameters

Update parameters of the existing collection

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.models.update_collection import UpdateCollection
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to update
    timeout = 56 # int | Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  (optional)
    update_collection = qdrant_openapi.UpdateCollection() # UpdateCollection | New parameters (optional)

    try:
        # Update collection parameters
        api_response = api_instance.update_collection(collection_name, timeout=timeout, update_collection=update_collection)
        print("The response of CollectionsApi->update_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->update_collection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to update | 
 **timeout** | **int**| Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  | [optional] 
 **update_collection** | [**UpdateCollection**](UpdateCollection.md)| New parameters | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collection_cluster**
> CreateShardKey200Response update_collection_cluster(collection_name, timeout=timeout, cluster_operations=cluster_operations)

Update collection cluster setup

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.cluster_operations import ClusterOperations
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.CollectionsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection on which to to apply the cluster update operation
    timeout = 56 # int | Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  (optional)
    cluster_operations = qdrant_openapi.ClusterOperations() # ClusterOperations | Collection cluster update operations (optional)

    try:
        # Update collection cluster setup
        api_response = api_instance.update_collection_cluster(collection_name, timeout=timeout, cluster_operations=cluster_operations)
        print("The response of CollectionsApi->update_collection_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->update_collection_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection on which to to apply the cluster update operation | 
 **timeout** | **int**| Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  | [optional] 
 **cluster_operations** | [**ClusterOperations**](ClusterOperations.md)| Collection cluster update operations | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

