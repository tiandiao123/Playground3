from . import FieldTypeAttribute

class Descriptor(FieldTypeAttribute):
    """
    This class exists soley for type hierarchy. Descriptors
    are attributes that have no functional operations.
    """
    pass

class StandardDescriptors:
    Size     = Descriptor()
    Optional = Descriptor()
    Required = Descriptor()
    ExplicitTag = Descriptor()