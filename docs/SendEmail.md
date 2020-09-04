# SendEmail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_to** | **list[str]** | List of the email addresses of the recipients. For example: **[&#x27;abc@example.com&#x27;, &#x27;asd@example.com&#x27;]**  | 
**email_bcc** | **list[str]** | List of the email addresses of the recipients in bcc | [optional] 
**email_cc** | **list[str]** | List of the email addresses of the recipients in cc | [optional] 
**reply_to** | **str** | Email address which shall be used by campaign recipients to reply back | [optional] 
**attachment_url** | **str** | Absolute url of the attachment (**no local file**). Extensions allowed: #### xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps  | [optional] 
**attachment** | [**list[SendEmailAttachment]**](SendEmailAttachment.md) | Pass the list of content (base64 encoded) and name of the attachment. For example: **[{\&quot;content\&quot;:\&quot;base64 encoded content 1\&quot;, \&quot;name\&quot;:\&quot;attcahment1\&quot;}, {\&quot;content\&quot;:\&quot;base64 encoded content 2\&quot;, \&quot;name\&quot;:\&quot;attcahment2\&quot;}]**  | [optional] 
**headers** | [**dict(str, Object)**](Object.md) | Pass the set of headers that shall be sent along the mail headers in the original email. **&#x27;sender.ip&#x27;** header can be set (**only for dedicated ip users**) to mention the IP to be used for sending transactional emails. Headers are allowed in &#x60;This-Case-Only&#x60; (i.e. words separated by hyphen with first letter of each word in capital letter), they will be converted to such case styling if not in this format in the request payload. For example, **{\&quot;Content-Type\&quot;:\&quot;text/html\&quot;, \&quot;charset\&quot;:\&quot;iso-8859-1\&quot;, \&quot;sender.ip\&quot;:\&quot;1.2.3.4\&quot;}**  | [optional] 
**attributes** | [**dict(str, Object)**](Object.md) | Pass the set of attributes to customize the template. For example, **{\&quot;FNAME\&quot;:\&quot;Joe\&quot;, \&quot;LNAME\&quot;:\&quot;Doe\&quot;}**  | [optional] 
**tags** | **list[str]** | Tag your emails to find them more easily | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

