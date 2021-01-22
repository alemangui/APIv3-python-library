# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SendSmtpEmail(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'sender': 'SendSmtpEmailSender',
        'to': 'list[SendSmtpEmailTo]',
        'bcc': 'list[SendSmtpEmailBcc]',
        'cc': 'list[SendSmtpEmailCc]',
        'html_content': 'str',
        'text_content': 'str',
        'subject': 'str',
        'reply_to': 'SendSmtpEmailReplyTo',
        'attachment': 'list[SendSmtpEmailAttachment]',
        'headers': 'object',
        'template_id': 'int',
        'params': 'object',
        'message_versions': 'list[SendSmtpEmailMessageVersions]',
        'tags': 'list[str]'
    }

    attribute_map = {
        'sender': 'sender',
        'to': 'to',
        'bcc': 'bcc',
        'cc': 'cc',
        'html_content': 'htmlContent',
        'text_content': 'textContent',
        'subject': 'subject',
        'reply_to': 'replyTo',
        'attachment': 'attachment',
        'headers': 'headers',
        'template_id': 'templateId',
        'params': 'params',
        'message_versions': 'messageVersions',
        'tags': 'tags'
    }

    def __init__(self, sender=None, to=None, bcc=None, cc=None, html_content=None, text_content=None, subject=None, reply_to=None, attachment=None, headers=None, template_id=None, params=None, message_versions=None, tags=None):  # noqa: E501
        """SendSmtpEmail - a model defined in Swagger"""  # noqa: E501

        self._sender = None
        self._to = None
        self._bcc = None
        self._cc = None
        self._html_content = None
        self._text_content = None
        self._subject = None
        self._reply_to = None
        self._attachment = None
        self._headers = None
        self._template_id = None
        self._params = None
        self._message_versions = None
        self._tags = None
        self.discriminator = None

        if sender is not None:
            self.sender = sender
        if to is not None:
            self.to = to
        if bcc is not None:
            self.bcc = bcc
        if cc is not None:
            self.cc = cc
        if html_content is not None:
            self.html_content = html_content
        if text_content is not None:
            self.text_content = text_content
        if subject is not None:
            self.subject = subject
        if reply_to is not None:
            self.reply_to = reply_to
        if attachment is not None:
            self.attachment = attachment
        if headers is not None:
            self.headers = headers
        if template_id is not None:
            self.template_id = template_id
        if params is not None:
            self.params = params
        if message_versions is not None:
            self.message_versions = message_versions
        if tags is not None:
            self.tags = tags

    @property
    def sender(self):
        """Gets the sender of this SendSmtpEmail.  # noqa: E501


        :return: The sender of this SendSmtpEmail.  # noqa: E501
        :rtype: SendSmtpEmailSender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this SendSmtpEmail.


        :param sender: The sender of this SendSmtpEmail.  # noqa: E501
        :type: SendSmtpEmailSender
        """

        self._sender = sender

    @property
    def to(self):
        """Gets the to of this SendSmtpEmail.  # noqa: E501

        Mandatory if messageVersions are not passed, ignored if messageVersions are passed. List of email addresses and names (optional) of the recipients. For example, [{\"name\":\"Jimmy\", \"email\":\"jimmy98@example.com\"}, {\"name\":\"Joe\", \"email\":\"joe@example.com\"}]  # noqa: E501

        :return: The to of this SendSmtpEmail.  # noqa: E501
        :rtype: list[SendSmtpEmailTo]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SendSmtpEmail.

        Mandatory if messageVersions are not passed, ignored if messageVersions are passed. List of email addresses and names (optional) of the recipients. For example, [{\"name\":\"Jimmy\", \"email\":\"jimmy98@example.com\"}, {\"name\":\"Joe\", \"email\":\"joe@example.com\"}]  # noqa: E501

        :param to: The to of this SendSmtpEmail.  # noqa: E501
        :type: list[SendSmtpEmailTo]
        """

        self._to = to

    @property
    def bcc(self):
        """Gets the bcc of this SendSmtpEmail.  # noqa: E501

        List of email addresses and names (optional) of the recipients in bcc  # noqa: E501

        :return: The bcc of this SendSmtpEmail.  # noqa: E501
        :rtype: list[SendSmtpEmailBcc]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this SendSmtpEmail.

        List of email addresses and names (optional) of the recipients in bcc  # noqa: E501

        :param bcc: The bcc of this SendSmtpEmail.  # noqa: E501
        :type: list[SendSmtpEmailBcc]
        """

        self._bcc = bcc

    @property
    def cc(self):
        """Gets the cc of this SendSmtpEmail.  # noqa: E501

        List of email addresses and names (optional) of the recipients in cc  # noqa: E501

        :return: The cc of this SendSmtpEmail.  # noqa: E501
        :rtype: list[SendSmtpEmailCc]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this SendSmtpEmail.

        List of email addresses and names (optional) of the recipients in cc  # noqa: E501

        :param cc: The cc of this SendSmtpEmail.  # noqa: E501
        :type: list[SendSmtpEmailCc]
        """

        self._cc = cc

    @property
    def html_content(self):
        """Gets the html_content of this SendSmtpEmail.  # noqa: E501

        HTML body of the message ( Mandatory if 'templateId' is not passed, ignored if 'templateId' is passed )  # noqa: E501

        :return: The html_content of this SendSmtpEmail.  # noqa: E501
        :rtype: str
        """
        return self._html_content

    @html_content.setter
    def html_content(self, html_content):
        """Sets the html_content of this SendSmtpEmail.

        HTML body of the message ( Mandatory if 'templateId' is not passed, ignored if 'templateId' is passed )  # noqa: E501

        :param html_content: The html_content of this SendSmtpEmail.  # noqa: E501
        :type: str
        """

        self._html_content = html_content

    @property
    def text_content(self):
        """Gets the text_content of this SendSmtpEmail.  # noqa: E501

        Plain Text body of the message ( Ignored if 'templateId' is passed )  # noqa: E501

        :return: The text_content of this SendSmtpEmail.  # noqa: E501
        :rtype: str
        """
        return self._text_content

    @text_content.setter
    def text_content(self, text_content):
        """Sets the text_content of this SendSmtpEmail.

        Plain Text body of the message ( Ignored if 'templateId' is passed )  # noqa: E501

        :param text_content: The text_content of this SendSmtpEmail.  # noqa: E501
        :type: str
        """

        self._text_content = text_content

    @property
    def subject(self):
        """Gets the subject of this SendSmtpEmail.  # noqa: E501

        Subject of the message. Mandatory if 'templateId' is not passed  # noqa: E501

        :return: The subject of this SendSmtpEmail.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SendSmtpEmail.

        Subject of the message. Mandatory if 'templateId' is not passed  # noqa: E501

        :param subject: The subject of this SendSmtpEmail.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def reply_to(self):
        """Gets the reply_to of this SendSmtpEmail.  # noqa: E501


        :return: The reply_to of this SendSmtpEmail.  # noqa: E501
        :rtype: SendSmtpEmailReplyTo
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this SendSmtpEmail.


        :param reply_to: The reply_to of this SendSmtpEmail.  # noqa: E501
        :type: SendSmtpEmailReplyTo
        """

        self._reply_to = reply_to

    @property
    def attachment(self):
        """Gets the attachment of this SendSmtpEmail.  # noqa: E501

        Pass the absolute URL (no local file) or the base64 content of the attachment along with the attachment name (Mandatory if attachment content is passed). For example, `[{\"url\":\"https://attachment.domain.com/myAttachmentFromUrl.jpg\", \"name\":\"myAttachmentFromUrl.jpg\"}, {\"content\":\"base64 example content\", \"name\":\"myAttachmentFromBase64.jpg\"}]`. Allowed extensions for attachment file: xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub, eps, odt, mp3, m4a, m4v, wma, ogg, flac, wav, aif, aifc, aiff, mp4, mov, avi, mkv, mpeg, mpg and wmv ( If 'templateId' is passed and is in New Template Language format then both attachment url and content are accepted. If template is in Old template Language format, then 'attachment' is ignored )  # noqa: E501

        :return: The attachment of this SendSmtpEmail.  # noqa: E501
        :rtype: list[SendSmtpEmailAttachment]
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this SendSmtpEmail.

        Pass the absolute URL (no local file) or the base64 content of the attachment along with the attachment name (Mandatory if attachment content is passed). For example, `[{\"url\":\"https://attachment.domain.com/myAttachmentFromUrl.jpg\", \"name\":\"myAttachmentFromUrl.jpg\"}, {\"content\":\"base64 example content\", \"name\":\"myAttachmentFromBase64.jpg\"}]`. Allowed extensions for attachment file: xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub, eps, odt, mp3, m4a, m4v, wma, ogg, flac, wav, aif, aifc, aiff, mp4, mov, avi, mkv, mpeg, mpg and wmv ( If 'templateId' is passed and is in New Template Language format then both attachment url and content are accepted. If template is in Old template Language format, then 'attachment' is ignored )  # noqa: E501

        :param attachment: The attachment of this SendSmtpEmail.  # noqa: E501
        :type: list[SendSmtpEmailAttachment]
        """

        self._attachment = attachment

    @property
    def headers(self):
        """Gets the headers of this SendSmtpEmail.  # noqa: E501

        Pass the set of custom headers (not the standard headers) that shall be sent along the mail headers in the original email. 'sender.ip' header can be set (only for dedicated ip users) to mention the IP to be used for sending transactional emails. Headers are allowed in `This-Case-Only` (i.e. words separated by hyphen with first letter of each word in capital letter), they will be converted to such case styling if not in this format in the request payload. For example, `{\"sender.ip\":\"1.2.3.4\", \"X-Mailin-custom\":\"some_custom_header\"}`.  # noqa: E501

        :return: The headers of this SendSmtpEmail.  # noqa: E501
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this SendSmtpEmail.

        Pass the set of custom headers (not the standard headers) that shall be sent along the mail headers in the original email. 'sender.ip' header can be set (only for dedicated ip users) to mention the IP to be used for sending transactional emails. Headers are allowed in `This-Case-Only` (i.e. words separated by hyphen with first letter of each word in capital letter), they will be converted to such case styling if not in this format in the request payload. For example, `{\"sender.ip\":\"1.2.3.4\", \"X-Mailin-custom\":\"some_custom_header\"}`.  # noqa: E501

        :param headers: The headers of this SendSmtpEmail.  # noqa: E501
        :type: object
        """

        self._headers = headers

    @property
    def template_id(self):
        """Gets the template_id of this SendSmtpEmail.  # noqa: E501

        Id of the template. Mandatory if messageVersions are passed  # noqa: E501

        :return: The template_id of this SendSmtpEmail.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this SendSmtpEmail.

        Id of the template. Mandatory if messageVersions are passed  # noqa: E501

        :param template_id: The template_id of this SendSmtpEmail.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def params(self):
        """Gets the params of this SendSmtpEmail.  # noqa: E501

        Pass the set of attributes to customize the template. For example, {\"FNAME\":\"Joe\", \"LNAME\":\"Doe\"}. It's considered only if template is in New Template Language format.  # noqa: E501

        :return: The params of this SendSmtpEmail.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this SendSmtpEmail.

        Pass the set of attributes to customize the template. For example, {\"FNAME\":\"Joe\", \"LNAME\":\"Doe\"}. It's considered only if template is in New Template Language format.  # noqa: E501

        :param params: The params of this SendSmtpEmail.  # noqa: E501
        :type: object
        """

        self._params = params

    @property
    def message_versions(self):
        """Gets the message_versions of this SendSmtpEmail.  # noqa: E501

        You can customize and send out multiple versions of a templateId. Some global parameters such as **to(mandatory), bcc, cc, replyTo, subject** can also be customized specific to each version. The size of individual params in all the messageVersions shall not exceed 100 KB limit and that of cumulative params shall not exceed 1000 KB. This feature is currently in its beta version. You can follow this **step-by-step guide** on how to use **messageVersions** to batch send emails - https://developers.sendinblue.com/docs/batch-send-transactional-emails  # noqa: E501

        :return: The message_versions of this SendSmtpEmail.  # noqa: E501
        :rtype: list[SendSmtpEmailMessageVersions]
        """
        return self._message_versions

    @message_versions.setter
    def message_versions(self, message_versions):
        """Sets the message_versions of this SendSmtpEmail.

        You can customize and send out multiple versions of a templateId. Some global parameters such as **to(mandatory), bcc, cc, replyTo, subject** can also be customized specific to each version. The size of individual params in all the messageVersions shall not exceed 100 KB limit and that of cumulative params shall not exceed 1000 KB. This feature is currently in its beta version. You can follow this **step-by-step guide** on how to use **messageVersions** to batch send emails - https://developers.sendinblue.com/docs/batch-send-transactional-emails  # noqa: E501

        :param message_versions: The message_versions of this SendSmtpEmail.  # noqa: E501
        :type: list[SendSmtpEmailMessageVersions]
        """

        self._message_versions = message_versions

    @property
    def tags(self):
        """Gets the tags of this SendSmtpEmail.  # noqa: E501

        Tag your emails to find them more easily  # noqa: E501

        :return: The tags of this SendSmtpEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SendSmtpEmail.

        Tag your emails to find them more easily  # noqa: E501

        :param tags: The tags of this SendSmtpEmail.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SendSmtpEmail, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SendSmtpEmail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
