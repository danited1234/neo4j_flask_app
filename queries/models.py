from neomodel import (StructuredNode, StringProperty, FloatProperty, IntegerProperty, 
                      BooleanProperty, RelationshipTo)

class RegistrationToken(StructuredNode):
    role = StringProperty(required=True)
    token = StringProperty(required=True)
    id_str = StringProperty(required=True)
    created_at = FloatProperty(required=True)
    updated_at = FloatProperty(required=True)

class File(StructuredNode):
    is_active = BooleanProperty()
    file_name = StringProperty()
    created_at = FloatProperty()
    user_file_name = StringProperty()
    page_no = IntegerProperty()
    file_path_loc = StringProperty()
    is_deleted = BooleanProperty()
    updated_at = FloatProperty()
    size = IntegerProperty()
    id_str = StringProperty()
    width = IntegerProperty()
    _is_DL_processed = BooleanProperty()
    height = IntegerProperty()


class PDFFile(File):
    __label__ = "PDF_file"


class ImageFile(File):
    __label__ = "Image_file"


class Project(StructuredNode):
    is_active = BooleanProperty(required=True)
    is_deleted = BooleanProperty(required=True)
    updated_at = FloatProperty(required=True)
    id_str = StringProperty()
    name = StringProperty()
    created_at = FloatProperty()

    has_files = RelationshipTo(File, "HAS_FILES")


class User(StructuredNode):
    role = StringProperty()
    signup_method = StringProperty()
    _is_authenticated = BooleanProperty()
    updated_at = FloatProperty()
    _is_active = BooleanProperty()
    id_str = StringProperty()
    name = StringProperty()
    created_at = FloatProperty()
    last_name = StringProperty()
    currency = StringProperty()
    language = StringProperty()
    email = StringProperty()