#!/usr/bin/env python

#
# Generated Tue Aug  3 20:39:25 2010 by parse_xsd.py version 0.3.
#

import saml2
from saml2 import SamlBase

import xmldsig as ds

NAMESPACE = 'http://www.w3.org/2001/04/xmlenc#'

class KeySizeType(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:KeySizeType element """

    c_tag = 'KeySizeType'
    c_namespace = NAMESPACE
    c_value_type = {'base': 'integer'}
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()

def key_size_type_from_string(xml_string):
    return saml2.create_class_from_xml_string(KeySizeType, xml_string)

class CipherValue(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:CipherValue element """

    c_tag = 'CipherValue'
    c_namespace = NAMESPACE
    c_value_type = 'base64Binary'
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()

def cipher_value_from_string(xml_string):
    return saml2.create_class_from_xml_string(CipherValue, xml_string)

class TransformsType(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:TransformsType element """

    c_tag = 'TransformsType'
    c_namespace = NAMESPACE
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()
    c_children['{http://www.w3.org/2000/09/xmldsig#}Transform'] = ('transform', [ds.Transform])
    c_cardinality['transform'] = {"min":1}
    c_child_order.extend(['transform'])

    def __init__(self,
            transform=None,
            text=None,
            extension_elements=None,
            extension_attributes=None,
        ):
        SamlBase.__init__(self, 
                text=text,
                extension_elements=extension_elements,
                extension_attributes=extension_attributes,
                )
        self.transform=transform or []

def transforms_type_from_string(xml_string):
    return saml2.create_class_from_xml_string(TransformsType, xml_string)

class KA_Nonce(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:KA_Nonce element """

    c_tag = 'KA_Nonce'
    c_namespace = NAMESPACE
    c_value_type = 'base64Binary'
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()

def k_a__nonce_from_string(xml_string):
    return saml2.create_class_from_xml_string(KA_Nonce, xml_string)

class OriginatorKeyInfo(ds.KeyInfoType):
    """The http://www.w3.org/2001/04/xmlenc#:OriginatorKeyInfo element """

    c_tag = 'OriginatorKeyInfo'
    c_namespace = NAMESPACE
    c_children = ds.KeyInfoType.c_children.copy()
    c_attributes = ds.KeyInfoType.c_attributes.copy()
    c_child_order = ds.KeyInfoType.c_child_order[:]
    c_cardinality = ds.KeyInfoType.c_cardinality.copy()

def originator_key_info_from_string(xml_string):
    return saml2.create_class_from_xml_string(OriginatorKeyInfo, xml_string)

class RecipientKeyInfo(ds.KeyInfoType):
    """The http://www.w3.org/2001/04/xmlenc#:RecipientKeyInfo element """

    c_tag = 'RecipientKeyInfo'
    c_namespace = NAMESPACE
    c_children = ds.KeyInfoType.c_children.copy()
    c_attributes = ds.KeyInfoType.c_attributes.copy()
    c_child_order = ds.KeyInfoType.c_child_order[:]
    c_cardinality = ds.KeyInfoType.c_cardinality.copy()

def recipient_key_info_from_string(xml_string):
    return saml2.create_class_from_xml_string(RecipientKeyInfo, xml_string)

class AgreementMethodType(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:AgreementMethodType element """

    c_tag = 'AgreementMethodType'
    c_namespace = NAMESPACE
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()
    c_children['{http://www.w3.org/2001/04/xmlenc#}KA_Nonce'] = ('k_a__nonce', KA_Nonce)
    c_cardinality['k_a__nonce'] = {"min":0, "max":1}
    c_children['{http://www.w3.org/2000/09/xmldsig#}OriginatorKeyInfo'] = ('originator_key_info', ds.KeyInfoType)
    c_cardinality['originator_key_info'] = {"min":0, "max":1}
    c_children['{http://www.w3.org/2000/09/xmldsig#}RecipientKeyInfo'] = ('recipient_key_info', ds.KeyInfoType)
    c_cardinality['recipient_key_info'] = {"min":0, "max":1}
    c_attributes['Algorithm'] = ('algorithm', 'anyURI', True)
    c_child_order.extend(['k_a__nonce', 'originator_key_info', 'recipient_key_info'])

    def __init__(self,
            k_a__nonce=None,
            originator_key_info=None,
            recipient_key_info=None,
            algorithm=None,
            text=None,
            extension_elements=None,
            extension_attributes=None,
        ):
        SamlBase.__init__(self, 
                text=text,
                extension_elements=extension_elements,
                extension_attributes=extension_attributes,
                )
        self.k_a__nonce=k_a__nonce
        self.originator_key_info=originator_key_info
        self.recipient_key_info=recipient_key_info
        self.algorithm=algorithm

def agreement_method_type_from_string(xml_string):
    return saml2.create_class_from_xml_string(AgreementMethodType, xml_string)

class ReferenceType(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:ReferenceType element """

    c_tag = 'ReferenceType'
    c_namespace = NAMESPACE
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()
    c_attributes['URI'] = ('uri', 'anyURI', True)

    def __init__(self,
            uri=None,
            text=None,
            extension_elements=None,
            extension_attributes=None,
        ):
        SamlBase.__init__(self, 
                text=text,
                extension_elements=extension_elements,
                extension_attributes=extension_attributes,
                )
        self.uri=uri

def reference_type_from_string(xml_string):
    return saml2.create_class_from_xml_string(ReferenceType, xml_string)

class EncryptionPropertyType(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptionPropertyType element """

    c_tag = 'EncryptionPropertyType'
    c_namespace = NAMESPACE
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()
    c_attributes['Target'] = ('target', 'anyURI', False)
    c_attributes['Id'] = ('id', 'ID', False)

    def __init__(self,
            target=None,
            id=None,
            text=None,
            extension_elements=None,
            extension_attributes=None,
        ):
        SamlBase.__init__(self, 
                text=text,
                extension_elements=extension_elements,
                extension_attributes=extension_attributes,
                )
        self.target=target
        self.id=id

def encryption_property_type_from_string(xml_string):
    return saml2.create_class_from_xml_string(EncryptionPropertyType, xml_string)

class KeySize(KeySizeType):
    """The http://www.w3.org/2001/04/xmlenc#:KeySize element """

    c_tag = 'KeySize'
    c_namespace = NAMESPACE
    c_children = KeySizeType.c_children.copy()
    c_attributes = KeySizeType.c_attributes.copy()
    c_child_order = KeySizeType.c_child_order[:]
    c_cardinality = KeySizeType.c_cardinality.copy()

def key_size_from_string(xml_string):
    return saml2.create_class_from_xml_string(KeySize, xml_string)

class OAEPparams(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:OAEPparams element """

    c_tag = 'OAEPparams'
    c_namespace = NAMESPACE
    c_value_type = 'base64Binary'
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()

def oae_pparams_from_string(xml_string):
    return saml2.create_class_from_xml_string(OAEPparams, xml_string)

class EncryptionMethodType(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptionMethodType element """

    c_tag = 'EncryptionMethodType'
    c_namespace = NAMESPACE
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()
    c_children['{http://www.w3.org/2001/04/xmlenc#}KeySize'] = ('key_size', KeySize)
    c_cardinality['key_size'] = {"min":0, "max":1}
    c_children['{http://www.w3.org/2001/04/xmlenc#}OAEPparams'] = ('oae_pparams', OAEPparams)
    c_cardinality['oae_pparams'] = {"min":0, "max":1}
    c_attributes['Algorithm'] = ('algorithm', 'anyURI', True)
    c_child_order.extend(['key_size', 'oae_pparams'])

    def __init__(self,
            key_size=None,
            oae_pparams=None,
            algorithm=None,
            text=None,
            extension_elements=None,
            extension_attributes=None,
        ):
        SamlBase.__init__(self, 
                text=text,
                extension_elements=extension_elements,
                extension_attributes=extension_attributes,
                )
        self.key_size=key_size
        self.oae_pparams=oae_pparams
        self.algorithm=algorithm

def encryption_method_type_from_string(xml_string):
    return saml2.create_class_from_xml_string(EncryptionMethodType, xml_string)

class Transforms(TransformsType):
    """The http://www.w3.org/2001/04/xmlenc#:Transforms element """

    c_tag = 'Transforms'
    c_namespace = NAMESPACE
    c_children = TransformsType.c_children.copy()
    c_attributes = TransformsType.c_attributes.copy()
    c_child_order = TransformsType.c_child_order[:]
    c_cardinality = TransformsType.c_cardinality.copy()

def transforms_from_string(xml_string):
    return saml2.create_class_from_xml_string(Transforms, xml_string)

class CipherReferenceType(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:CipherReferenceType element """

    c_tag = 'CipherReferenceType'
    c_namespace = NAMESPACE
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()
    c_children['{http://www.w3.org/2001/04/xmlenc#}Transforms'] = ('transforms', Transforms)
    c_cardinality['transforms'] = {"min":0, "max":1}
    c_attributes['URI'] = ('uri', 'anyURI', True)
    c_child_order.extend(['transforms'])

    def __init__(self,
            transforms=None,
            uri=None,
            text=None,
            extension_elements=None,
            extension_attributes=None,
        ):
        SamlBase.__init__(self, 
                text=text,
                extension_elements=extension_elements,
                extension_attributes=extension_attributes,
                )
        self.transforms=transforms
        self.uri=uri

def cipher_reference_type_from_string(xml_string):
    return saml2.create_class_from_xml_string(CipherReferenceType, xml_string)

class EncryptionMethod(EncryptionMethodType):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptionMethod element """

    c_tag = 'EncryptionMethod'
    c_namespace = NAMESPACE
    c_children = EncryptionMethodType.c_children.copy()
    c_attributes = EncryptionMethodType.c_attributes.copy()
    c_child_order = EncryptionMethodType.c_child_order[:]
    c_cardinality = EncryptionMethodType.c_cardinality.copy()

def encryption_method_from_string(xml_string):
    return saml2.create_class_from_xml_string(EncryptionMethod, xml_string)


class AgreementMethod(AgreementMethodType):
    """The http://www.w3.org/2001/04/xmlenc#:AgreementMethod element """

    c_tag = 'AgreementMethod'
    c_namespace = NAMESPACE
    c_children = AgreementMethodType.c_children.copy()
    c_attributes = AgreementMethodType.c_attributes.copy()
    c_child_order = AgreementMethodType.c_child_order[:]
    c_cardinality = AgreementMethodType.c_cardinality.copy()

def agreement_method_from_string(xml_string):
    return saml2.create_class_from_xml_string(AgreementMethod, xml_string)

class DataReference(ReferenceType):
    """The http://www.w3.org/2001/04/xmlenc#:DataReference element """

    c_tag = 'DataReference'
    c_namespace = NAMESPACE
    c_children = ReferenceType.c_children.copy()
    c_attributes = ReferenceType.c_attributes.copy()
    c_child_order = ReferenceType.c_child_order[:]
    c_cardinality = ReferenceType.c_cardinality.copy()

def data_reference_from_string(xml_string):
    return saml2.create_class_from_xml_string(DataReference, xml_string)

class KeyReference(ReferenceType):
    """The http://www.w3.org/2001/04/xmlenc#:KeyReference element """

    c_tag = 'KeyReference'
    c_namespace = NAMESPACE
    c_children = ReferenceType.c_children.copy()
    c_attributes = ReferenceType.c_attributes.copy()
    c_child_order = ReferenceType.c_child_order[:]
    c_cardinality = ReferenceType.c_cardinality.copy()

def key_reference_from_string(xml_string):
    return saml2.create_class_from_xml_string(KeyReference, xml_string)

class ReferenceList(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:ReferenceList element """

    c_tag = 'ReferenceList'
    c_namespace = NAMESPACE
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()
    c_children['{http://www.w3.org/2001/04/xmlenc#}DataReference'] = ('data_reference', [DataReference])
    c_cardinality['data_reference'] = {"min":0}
    c_children['{http://www.w3.org/2001/04/xmlenc#}KeyReference'] = ('key_reference', [KeyReference])
    c_cardinality['key_reference'] = {"min":0}
    c_child_order.extend(['data_reference', 'key_reference'])

    def __init__(self,
            data_reference=None,
            key_reference=None,
            text=None,
            extension_elements=None,
            extension_attributes=None,
        ):
        SamlBase.__init__(self, 
                text=text,
                extension_elements=extension_elements,
                extension_attributes=extension_attributes,
                )
        self.data_reference=data_reference or []
        self.key_reference=key_reference or []

def reference_list_from_string(xml_string):
    return saml2.create_class_from_xml_string(ReferenceList, xml_string)

class EncryptionProperty(EncryptionPropertyType):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptionProperty element """

    c_tag = 'EncryptionProperty'
    c_namespace = NAMESPACE
    c_children = EncryptionPropertyType.c_children.copy()
    c_attributes = EncryptionPropertyType.c_attributes.copy()
    c_child_order = EncryptionPropertyType.c_child_order[:]
    c_cardinality = EncryptionPropertyType.c_cardinality.copy()

def encryption_property_from_string(xml_string):
    return saml2.create_class_from_xml_string(EncryptionProperty, xml_string)

class CipherReference(CipherReferenceType):
    """The http://www.w3.org/2001/04/xmlenc#:CipherReference element """

    c_tag = 'CipherReference'
    c_namespace = NAMESPACE
    c_children = CipherReferenceType.c_children.copy()
    c_attributes = CipherReferenceType.c_attributes.copy()
    c_child_order = CipherReferenceType.c_child_order[:]
    c_cardinality = CipherReferenceType.c_cardinality.copy()

def cipher_reference_from_string(xml_string):
    return saml2.create_class_from_xml_string(CipherReference, xml_string)

class EncryptionPropertiesType(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptionPropertiesType element """

    c_tag = 'EncryptionPropertiesType'
    c_namespace = NAMESPACE
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()
    c_children['{http://www.w3.org/2001/04/xmlenc#}EncryptionProperty'] = ('encryption_property', [EncryptionProperty])
    c_cardinality['encryption_property'] = {"min":1}
    c_attributes['Id'] = ('id', 'ID', False)
    c_child_order.extend(['encryption_property'])

    def __init__(self,
            encryption_property=None,
            id=None,
            text=None,
            extension_elements=None,
            extension_attributes=None,
        ):
        SamlBase.__init__(self, 
                text=text,
                extension_elements=extension_elements,
                extension_attributes=extension_attributes,
                )
        self.encryption_property=encryption_property or []
        self.id=id

def encryption_properties_type_from_string(xml_string):
    return saml2.create_class_from_xml_string(EncryptionPropertiesType, xml_string)

class CipherDataType(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:CipherDataType element """

    c_tag = 'CipherDataType'
    c_namespace = NAMESPACE
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()
    c_children['{http://www.w3.org/2001/04/xmlenc#}CipherValue'] = ('cipher_value', CipherValue)
    c_cardinality['cipher_value'] = {"min":0, "max":1}
    c_children['{http://www.w3.org/2001/04/xmlenc#}CipherReference'] = ('cipher_reference', CipherReference)
    c_cardinality['cipher_reference'] = {"min":0, "max":1}
    c_child_order.extend(['cipher_value', 'cipher_reference'])

    def __init__(self,
            cipher_value=None,
            cipher_reference=None,
            text=None,
            extension_elements=None,
            extension_attributes=None,
        ):
        SamlBase.__init__(self, 
                text=text,
                extension_elements=extension_elements,
                extension_attributes=extension_attributes,
                )
        self.cipher_value=cipher_value
        self.cipher_reference=cipher_reference

def cipher_data_type_from_string(xml_string):
    return saml2.create_class_from_xml_string(CipherDataType, xml_string)

class EncryptionProperties(EncryptionPropertiesType):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptionProperties element """

    c_tag = 'EncryptionProperties'
    c_namespace = NAMESPACE
    c_children = EncryptionPropertiesType.c_children.copy()
    c_attributes = EncryptionPropertiesType.c_attributes.copy()
    c_child_order = EncryptionPropertiesType.c_child_order[:]
    c_cardinality = EncryptionPropertiesType.c_cardinality.copy()

def encryption_properties_from_string(xml_string):
    return saml2.create_class_from_xml_string(EncryptionProperties, xml_string)

class CipherData(CipherDataType):
    """The http://www.w3.org/2001/04/xmlenc#:CipherData element """

    c_tag = 'CipherData'
    c_namespace = NAMESPACE
    c_children = CipherDataType.c_children.copy()
    c_attributes = CipherDataType.c_attributes.copy()
    c_child_order = CipherDataType.c_child_order[:]
    c_cardinality = CipherDataType.c_cardinality.copy()

def cipher_data_from_string(xml_string):
    return saml2.create_class_from_xml_string(CipherData, xml_string)

class EncryptedType(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptedType element """

    c_tag = 'EncryptedType'
    c_namespace = NAMESPACE
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()
    c_children['{http://www.w3.org/2001/04/xmlenc#}EncryptionMethod'] = ('encryption_method', EncryptionMethod)
    c_cardinality['encryption_method'] = {"min":0, "max":1}
    c_children['{http://www.w3.org/2000/09/xmldsig#}KeyInfo'] = ('key_info', ds.KeyInfo)
    c_cardinality['key_info'] = {"min":0, "max":1}
    c_children['{http://www.w3.org/2001/04/xmlenc#}CipherData'] = ('cipher_data', CipherData)
    c_children['{http://www.w3.org/2001/04/xmlenc#}EncryptionProperties'] = ('encryption_properties', EncryptionProperties)
    c_cardinality['encryption_properties'] = {"min":0, "max":1}
    c_attributes['Id'] = ('id', 'ID', False)
    c_attributes['Type'] = ('type', 'anyURI', False)
    c_attributes['MimeType'] = ('mime_type', 'string', False)
    c_attributes['Encoding'] = ('encoding', 'anyURI', False)
    c_child_order.extend(['encryption_method', 'key_info', 'cipher_data', 'encryption_properties'])

    def __init__(self,
            encryption_method=None,
            key_info=None,
            cipher_data=None,
            encryption_properties=None,
            id=None,
            type=None,
            mime_type=None,
            encoding=None,
            text=None,
            extension_elements=None,
            extension_attributes=None,
        ):
        SamlBase.__init__(self, 
                text=text,
                extension_elements=extension_elements,
                extension_attributes=extension_attributes,
                )
        self.encryption_method=encryption_method
        self.key_info=key_info
        self.cipher_data=cipher_data
        self.encryption_properties=encryption_properties
        self.id=id
        self.type=type
        self.mime_type=mime_type
        self.encoding=encoding

def encrypted_type_from_string(xml_string):
    return saml2.create_class_from_xml_string(EncryptedType, xml_string)

class EncryptedDataType(EncryptedType):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptedDataType element """

    c_tag = 'EncryptedDataType'
    c_namespace = NAMESPACE
    c_children = EncryptedType.c_children.copy()
    c_attributes = EncryptedType.c_attributes.copy()
    c_child_order = EncryptedType.c_child_order[:]
    c_cardinality = EncryptedType.c_cardinality.copy()

def encrypted_data_type_from_string(xml_string):
    return saml2.create_class_from_xml_string(EncryptedDataType, xml_string)

class CarriedKeyName(SamlBase):
    """The http://www.w3.org/2001/04/xmlenc#:CarriedKeyName element """

    c_tag = 'CarriedKeyName'
    c_namespace = NAMESPACE
    c_value_type = 'string'
    c_children = SamlBase.c_children.copy()
    c_attributes = SamlBase.c_attributes.copy()
    c_child_order = SamlBase.c_child_order[:]
    c_cardinality = SamlBase.c_cardinality.copy()

def carried_key_name_from_string(xml_string):
    return saml2.create_class_from_xml_string(CarriedKeyName, xml_string)

class EncryptedKeyType(EncryptedType):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptedKeyType element """

    c_tag = 'EncryptedKeyType'
    c_namespace = NAMESPACE
    c_children = EncryptedType.c_children.copy()
    c_attributes = EncryptedType.c_attributes.copy()
    c_child_order = EncryptedType.c_child_order[:]
    c_cardinality = EncryptedType.c_cardinality.copy()
    c_children['{http://www.w3.org/2001/04/xmlenc#}ReferenceList'] = ('reference_list', ReferenceList)
    c_cardinality['reference_list'] = {"min":0, "max":1}
    c_children['{http://www.w3.org/2001/04/xmlenc#}CarriedKeyName'] = ('carried_key_name', CarriedKeyName)
    c_cardinality['carried_key_name'] = {"min":0, "max":1}
    c_attributes['Recipient'] = ('recipient', 'string', False)
    c_child_order.extend(['reference_list', 'carried_key_name'])

    def __init__(self,
            reference_list=None,
            carried_key_name=None,
            recipient=None,
            encryption_method=None,
            key_info=None,
            cipher_data=None,
            encryption_properties=None,
            id=None,
            type=None,
            mime_type=None,
            encoding=None,
            text=None,
            extension_elements=None,
            extension_attributes=None,
        ):
        EncryptedType.__init__(self, 
                encryption_method=encryption_method,
                key_info=key_info,
                cipher_data=cipher_data,
                encryption_properties=encryption_properties,
                id=id,
                type=type,
                mime_type=mime_type,
                encoding=encoding,
                text=text,
                extension_elements=extension_elements,
                extension_attributes=extension_attributes,
                )
        self.reference_list=reference_list
        self.carried_key_name=carried_key_name
        self.recipient=recipient

def encrypted_key_type_from_string(xml_string):
    return saml2.create_class_from_xml_string(EncryptedKeyType, xml_string)

class EncryptedData(EncryptedDataType):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptedData element """

    c_tag = 'EncryptedData'
    c_namespace = NAMESPACE
    c_children = EncryptedDataType.c_children.copy()
    c_attributes = EncryptedDataType.c_attributes.copy()
    c_child_order = EncryptedDataType.c_child_order[:]
    c_cardinality = EncryptedDataType.c_cardinality.copy()

def encrypted_data_from_string(xml_string):
    return saml2.create_class_from_xml_string(EncryptedData, xml_string)

class EncryptedKey(EncryptedKeyType):
    """The http://www.w3.org/2001/04/xmlenc#:EncryptedKey element """

    c_tag = 'EncryptedKey'
    c_namespace = NAMESPACE
    c_children = EncryptedKeyType.c_children.copy()
    c_attributes = EncryptedKeyType.c_attributes.copy()
    c_child_order = EncryptedKeyType.c_child_order[:]
    c_cardinality = EncryptedKeyType.c_cardinality.copy()

def encrypted_key_from_string(xml_string):
    return saml2.create_class_from_xml_string(EncryptedKey, xml_string)

ELEMENT_FROM_STRING = {
    EncryptedType.c_tag: encrypted_type_from_string,
    EncryptionMethodType.c_tag: encryption_method_type_from_string,
    KeySizeType.c_tag: key_size_type_from_string,
    CipherData.c_tag: cipher_data_from_string,
    CipherDataType.c_tag: cipher_data_type_from_string,
    CipherReference.c_tag: cipher_reference_from_string,
    CipherReferenceType.c_tag: cipher_reference_type_from_string,
    TransformsType.c_tag: transforms_type_from_string,
    EncryptedData.c_tag: encrypted_data_from_string,
    EncryptedDataType.c_tag: encrypted_data_type_from_string,
    EncryptedKey.c_tag: encrypted_key_from_string,
    EncryptedKeyType.c_tag: encrypted_key_type_from_string,
    AgreementMethod.c_tag: agreement_method_from_string,
    AgreementMethodType.c_tag: agreement_method_type_from_string,
    ReferenceList.c_tag: reference_list_from_string,
    ReferenceType.c_tag: reference_type_from_string,
    EncryptionProperties.c_tag: encryption_properties_from_string,
    EncryptionPropertiesType.c_tag: encryption_properties_type_from_string,
    EncryptionProperty.c_tag: encryption_property_from_string,
    EncryptionPropertyType.c_tag: encryption_property_type_from_string,
    CipherValue.c_tag: cipher_value_from_string,
    KA_Nonce.c_tag: k_a__nonce_from_string,
    OriginatorKeyInfo.c_tag: originator_key_info_from_string,
    RecipientKeyInfo.c_tag: recipient_key_info_from_string,
    KeySize.c_tag: key_size_from_string,
    OAEPparams.c_tag: oae_pparams_from_string,
    Transforms.c_tag: transforms_from_string,
    EncryptionMethod.c_tag: encryption_method_from_string,
    DataReference.c_tag: data_reference_from_string,
    KeyReference.c_tag: key_reference_from_string,
    CarriedKeyName.c_tag: carried_key_name_from_string,
}

ELEMENT_BY_TAG = {
    'EncryptedType': EncryptedType,
    'EncryptionMethodType': EncryptionMethodType,
    'KeySizeType': KeySizeType,
    'CipherData': CipherData,
    'CipherDataType': CipherDataType,
    'CipherReference': CipherReference,
    'CipherReferenceType': CipherReferenceType,
    'TransformsType': TransformsType,
    'EncryptedData': EncryptedData,
    'EncryptedDataType': EncryptedDataType,
    'EncryptedKey': EncryptedKey,
    'EncryptedKeyType': EncryptedKeyType,
    'AgreementMethod': AgreementMethod,
    'AgreementMethodType': AgreementMethodType,
    'ReferenceList': ReferenceList,
    'ReferenceType': ReferenceType,
    'EncryptionProperties': EncryptionProperties,
    'EncryptionPropertiesType': EncryptionPropertiesType,
    'EncryptionProperty': EncryptionProperty,
    'EncryptionPropertyType': EncryptionPropertyType,
    'CipherValue': CipherValue,
    'KA_Nonce': KA_Nonce,
    'OriginatorKeyInfo': OriginatorKeyInfo,
    'RecipientKeyInfo': RecipientKeyInfo,
    'KeySize': KeySize,
    'OAEPparams': OAEPparams,
    'Transforms': Transforms,
    'EncryptionMethod': EncryptionMethod,
    'DataReference': DataReference,
    'KeyReference': KeyReference,
    'CarriedKeyName': CarriedKeyName,
}

def factory(tag, **kwargs):
    return ELEMENT_BY_TAG[tag](**kwargs)

