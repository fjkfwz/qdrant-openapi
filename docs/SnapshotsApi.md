# qdrant_openapi.SnapshotsApi

All URIs are relative to *http://localhost:6333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_full_snapshot**](SnapshotsApi.md#create_full_snapshot) | **POST** /snapshots | Create storage snapshot
[**create_shard_snapshot**](SnapshotsApi.md#create_shard_snapshot) | **POST** /collections/{collection_name}/shards/{shard_id}/snapshots | Create shard snapshot
[**create_snapshot**](SnapshotsApi.md#create_snapshot) | **POST** /collections/{collection_name}/snapshots | Create collection snapshot
[**delete_full_snapshot**](SnapshotsApi.md#delete_full_snapshot) | **DELETE** /snapshots/{snapshot_name} | Delete storage snapshot
[**delete_shard_snapshot**](SnapshotsApi.md#delete_shard_snapshot) | **DELETE** /collections/{collection_name}/shards/{shard_id}/snapshots/{snapshot_name} | Delete shard snapshot
[**delete_snapshot**](SnapshotsApi.md#delete_snapshot) | **DELETE** /collections/{collection_name}/snapshots/{snapshot_name} | Delete collection snapshot
[**get_full_snapshot**](SnapshotsApi.md#get_full_snapshot) | **GET** /snapshots/{snapshot_name} | Download storage snapshot
[**get_shard_snapshot**](SnapshotsApi.md#get_shard_snapshot) | **GET** /collections/{collection_name}/shards/{shard_id}/snapshots/{snapshot_name} | Download collection snapshot
[**get_snapshot**](SnapshotsApi.md#get_snapshot) | **GET** /collections/{collection_name}/snapshots/{snapshot_name} | Download collection snapshot
[**list_full_snapshots**](SnapshotsApi.md#list_full_snapshots) | **GET** /snapshots | List of storage snapshots
[**list_shard_snapshots**](SnapshotsApi.md#list_shard_snapshots) | **GET** /collections/{collection_name}/shards/{shard_id}/snapshots | List shards snapshots for a collection
[**list_snapshots**](SnapshotsApi.md#list_snapshots) | **GET** /collections/{collection_name}/snapshots | List collection snapshots
[**recover_from_snapshot**](SnapshotsApi.md#recover_from_snapshot) | **PUT** /collections/{collection_name}/snapshots/recover | Recover from a snapshot
[**recover_from_uploaded_snapshot**](SnapshotsApi.md#recover_from_uploaded_snapshot) | **POST** /collections/{collection_name}/snapshots/upload | Recover from an uploaded snapshot
[**recover_shard_from_snapshot**](SnapshotsApi.md#recover_shard_from_snapshot) | **PUT** /collections/{collection_name}/shards/{shard_id}/snapshots/recover | Recover from a snapshot
[**recover_shard_from_uploaded_snapshot**](SnapshotsApi.md#recover_shard_from_uploaded_snapshot) | **POST** /collections/{collection_name}/shards/{shard_id}/snapshots/upload | Recover shard from an uploaded snapshot


# **create_full_snapshot**
> CreateSnapshot200Response create_full_snapshot(wait=wait)

Create storage snapshot

Create new snapshot of the whole storage

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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)

    try:
        # Create storage snapshot
        api_response = api_instance.create_full_snapshot(wait=wait)
        print("The response of SnapshotsApi->create_full_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->create_full_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection for which to create a snapshot
    shard_id = 56 # int | Id of the shard
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)

    try:
        # Create shard snapshot
        api_response = api_instance.create_shard_snapshot(collection_name, shard_id, wait=wait)
        print("The response of SnapshotsApi->create_shard_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->create_shard_snapshot: %s\n" % e)
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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection for which to create a snapshot
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)

    try:
        # Create collection snapshot
        api_response = api_instance.create_snapshot(collection_name, wait=wait)
        print("The response of SnapshotsApi->create_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->create_snapshot: %s\n" % e)
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

# **delete_full_snapshot**
> CreateShardKey200Response delete_full_snapshot(snapshot_name, wait=wait)

Delete storage snapshot

Delete snapshot of the whole storage

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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    snapshot_name = 'snapshot_name_example' # str | Name of the full snapshot to delete
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)

    try:
        # Delete storage snapshot
        api_response = api_instance.delete_full_snapshot(snapshot_name, wait=wait)
        print("The response of SnapshotsApi->delete_full_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->delete_full_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_name** | **str**| Name of the full snapshot to delete | 
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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection for which to delete a snapshot
    shard_id = 56 # int | Id of the shard
    snapshot_name = 'snapshot_name_example' # str | Name of the snapshot to delete
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)

    try:
        # Delete shard snapshot
        api_response = api_instance.delete_shard_snapshot(collection_name, shard_id, snapshot_name, wait=wait)
        print("The response of SnapshotsApi->delete_shard_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->delete_shard_snapshot: %s\n" % e)
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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection for which to delete a snapshot
    snapshot_name = 'snapshot_name_example' # str | Name of the snapshot to delete
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)

    try:
        # Delete collection snapshot
        api_response = api_instance.delete_snapshot(collection_name, snapshot_name, wait=wait)
        print("The response of SnapshotsApi->delete_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->delete_snapshot: %s\n" % e)
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

# **get_full_snapshot**
> bytearray get_full_snapshot(snapshot_name)

Download storage snapshot

Download specified snapshot of the whole storage as a file

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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    snapshot_name = 'snapshot_name_example' # str | Name of the snapshot to download

    try:
        # Download storage snapshot
        api_response = api_instance.get_full_snapshot(snapshot_name)
        print("The response of SnapshotsApi->get_full_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->get_full_snapshot: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    shard_id = 56 # int | Id of the shard
    snapshot_name = 'snapshot_name_example' # str | Name of the snapshot to download

    try:
        # Download collection snapshot
        api_response = api_instance.get_shard_snapshot(collection_name, shard_id, snapshot_name)
        print("The response of SnapshotsApi->get_shard_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->get_shard_snapshot: %s\n" % e)
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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    snapshot_name = 'snapshot_name_example' # str | Name of the snapshot to download

    try:
        # Download collection snapshot
        api_response = api_instance.get_snapshot(collection_name, snapshot_name)
        print("The response of SnapshotsApi->get_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->get_snapshot: %s\n" % e)
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

# **list_full_snapshots**
> ListSnapshots200Response list_full_snapshots()

List of storage snapshots

Get list of snapshots of the whole storage

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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)

    try:
        # List of storage snapshots
        api_response = api_instance.list_full_snapshots()
        print("The response of SnapshotsApi->list_full_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->list_full_snapshots: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    shard_id = 56 # int | Id of the shard

    try:
        # List shards snapshots for a collection
        api_response = api_instance.list_shard_snapshots(collection_name, shard_id)
        print("The response of SnapshotsApi->list_shard_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->list_shard_snapshots: %s\n" % e)
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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection

    try:
        # List collection snapshots
        api_response = api_instance.list_snapshots(collection_name)
        print("The response of SnapshotsApi->list_snapshots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->list_snapshots: %s\n" % e)
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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)
    snapshot_recover = qdrant_openapi.SnapshotRecover() # SnapshotRecover | Snapshot to recover from (optional)

    try:
        # Recover from a snapshot
        api_response = api_instance.recover_from_snapshot(collection_name, wait=wait, snapshot_recover=snapshot_recover)
        print("The response of SnapshotsApi->recover_from_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->recover_from_snapshot: %s\n" % e)
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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)
    priority = qdrant_openapi.SnapshotPriority() # SnapshotPriority | Defines source of truth for snapshot recovery (optional)
    snapshot = None # bytearray |  (optional)

    try:
        # Recover from an uploaded snapshot
        api_response = api_instance.recover_from_uploaded_snapshot(collection_name, wait=wait, priority=priority, snapshot=snapshot)
        print("The response of SnapshotsApi->recover_from_uploaded_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->recover_from_uploaded_snapshot: %s\n" % e)
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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    shard_id = 56 # int | Id of the shard to recover
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)
    shard_snapshot_recover = qdrant_openapi.ShardSnapshotRecover() # ShardSnapshotRecover | Snapshot to recover from (optional)

    try:
        # Recover from a snapshot
        api_response = api_instance.recover_shard_from_snapshot(collection_name, shard_id, wait=wait, shard_snapshot_recover=shard_snapshot_recover)
        print("The response of SnapshotsApi->recover_shard_from_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->recover_shard_from_snapshot: %s\n" % e)
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
    api_instance = qdrant_openapi.SnapshotsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection
    shard_id = 56 # int | Id of the shard to recover
    wait = True # bool | If true, wait for changes to actually happen. If false - let changes happen in background. Default is true. (optional)
    priority = qdrant_openapi.SnapshotPriority() # SnapshotPriority | Defines source of truth for snapshot recovery (optional)
    snapshot = None # bytearray |  (optional)

    try:
        # Recover shard from an uploaded snapshot
        api_response = api_instance.recover_shard_from_uploaded_snapshot(collection_name, shard_id, wait=wait, priority=priority, snapshot=snapshot)
        print("The response of SnapshotsApi->recover_shard_from_uploaded_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->recover_shard_from_uploaded_snapshot: %s\n" % e)
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

