# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from computer_vision_driver/CvInfo.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class CvInfo(genpy.Message):
  _md5sum = "8723a30b7f69c63ec944a866a7c37339"
  _type = "computer_vision_driver/CvInfo"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 cameraNumber
int32 taskNumber
int32 givenColor
int32 givenShape
float32 givenLength
float32 givenDistance
"""
  __slots__ = ['cameraNumber','taskNumber','givenColor','givenShape','givenLength','givenDistance']
  _slot_types = ['int32','int32','int32','int32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       cameraNumber,taskNumber,givenColor,givenShape,givenLength,givenDistance

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(CvInfo, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.cameraNumber is None:
        self.cameraNumber = 0
      if self.taskNumber is None:
        self.taskNumber = 0
      if self.givenColor is None:
        self.givenColor = 0
      if self.givenShape is None:
        self.givenShape = 0
      if self.givenLength is None:
        self.givenLength = 0.
      if self.givenDistance is None:
        self.givenDistance = 0.
    else:
      self.cameraNumber = 0
      self.taskNumber = 0
      self.givenColor = 0
      self.givenShape = 0
      self.givenLength = 0.
      self.givenDistance = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_4i2f().pack(_x.cameraNumber, _x.taskNumber, _x.givenColor, _x.givenShape, _x.givenLength, _x.givenDistance))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.cameraNumber, _x.taskNumber, _x.givenColor, _x.givenShape, _x.givenLength, _x.givenDistance,) = _get_struct_4i2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4i2f().pack(_x.cameraNumber, _x.taskNumber, _x.givenColor, _x.givenShape, _x.givenLength, _x.givenDistance))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.cameraNumber, _x.taskNumber, _x.givenColor, _x.givenShape, _x.givenLength, _x.givenDistance,) = _get_struct_4i2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4i2f = None
def _get_struct_4i2f():
    global _struct_4i2f
    if _struct_4i2f is None:
        _struct_4i2f = struct.Struct("<4i2f")
    return _struct_4i2f