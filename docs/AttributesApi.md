# sib_api_v3_sdk.AttributesApi

All URIs are relative to *https://api.sendinblue.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_attribute**](AttributesApi.md#create_attribute) | **POST** /contacts/attributes/{attributeCategory}/{attributeName} | Create contact attribute
[**delete_attribute**](AttributesApi.md#delete_attribute) | **DELETE** /contacts/attributes/{attributeCategory}/{attributeName} | Delete an attribute
[**get_attributes**](AttributesApi.md#get_attributes) | **GET** /contacts/attributes | List all attributes
[**update_attribute**](AttributesApi.md#update_attribute) | **PUT** /contacts/attributes/{attributeCategory}/{attributeName} | Update contact attribute

# **create_attribute**
> create_attribute(body, attribute_category, attribute_name)

Create contact attribute

### Example
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.AttributesApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.CreateAttribute() # CreateAttribute | Values to create an attribute
attribute_category = 'attribute_category_example' # str | Category of the attribute
attribute_name = 'attribute_name_example' # str | Name of the attribute

try:
    # Create contact attribute
    api_instance.create_attribute(body, attribute_category, attribute_name)
except ApiException as e:
    print("Exception when calling AttributesApi->create_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAttribute**](CreateAttribute.md)| Values to create an attribute | 
 **attribute_category** | **str**| Category of the attribute | 
 **attribute_name** | **str**| Name of the attribute | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attribute**
> delete_attribute(attribute_category, attribute_name)

Delete an attribute

### Example
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.AttributesApi(sib_api_v3_sdk.ApiClient(configuration))
attribute_category = 'attribute_category_example' # str | Category of the attribute
attribute_name = 'attribute_name_example' # str | Name of the existing attribute

try:
    # Delete an attribute
    api_instance.delete_attribute(attribute_category, attribute_name)
except ApiException as e:
    print("Exception when calling AttributesApi->delete_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_category** | **str**| Category of the attribute | 
 **attribute_name** | **str**| Name of the existing attribute | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes**
> GetAttributes get_attributes()

List all attributes

### Example
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.AttributesApi(sib_api_v3_sdk.ApiClient(configuration))

try:
    # List all attributes
    api_response = api_instance.get_attributes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_attributes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAttributes**](GetAttributes.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute**
> update_attribute(body, attribute_category, attribute_name)

Update contact attribute

### Example
```python
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.AttributesApi(sib_api_v3_sdk.ApiClient(configuration))
body = sib_api_v3_sdk.UpdateAttribute() # UpdateAttribute | Values to update an attribute
attribute_category = 'attribute_category_example' # str | Category of the attribute
attribute_name = 'attribute_name_example' # str | Name of the existing attribute

try:
    # Update contact attribute
    api_instance.update_attribute(body, attribute_category, attribute_name)
except ApiException as e:
    print("Exception when calling AttributesApi->update_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAttribute**](UpdateAttribute.md)| Values to update an attribute | 
 **attribute_category** | **str**| Category of the attribute | 
 **attribute_name** | **str**| Name of the existing attribute | 

### Return type

void (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

