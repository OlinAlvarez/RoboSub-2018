// Auto-generated. Do not edit!

// (in-package computer_vision_driver.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class CvInfo {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.cameraNumber = null;
      this.taskNumber = null;
      this.givenColor = null;
      this.givenShape = null;
      this.givenLength = null;
      this.givenDistance = null;
    }
    else {
      if (initObj.hasOwnProperty('cameraNumber')) {
        this.cameraNumber = initObj.cameraNumber
      }
      else {
        this.cameraNumber = 0;
      }
      if (initObj.hasOwnProperty('taskNumber')) {
        this.taskNumber = initObj.taskNumber
      }
      else {
        this.taskNumber = 0;
      }
      if (initObj.hasOwnProperty('givenColor')) {
        this.givenColor = initObj.givenColor
      }
      else {
        this.givenColor = 0;
      }
      if (initObj.hasOwnProperty('givenShape')) {
        this.givenShape = initObj.givenShape
      }
      else {
        this.givenShape = 0;
      }
      if (initObj.hasOwnProperty('givenLength')) {
        this.givenLength = initObj.givenLength
      }
      else {
        this.givenLength = 0.0;
      }
      if (initObj.hasOwnProperty('givenDistance')) {
        this.givenDistance = initObj.givenDistance
      }
      else {
        this.givenDistance = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CvInfo
    // Serialize message field [cameraNumber]
    bufferOffset = _serializer.int32(obj.cameraNumber, buffer, bufferOffset);
    // Serialize message field [taskNumber]
    bufferOffset = _serializer.int32(obj.taskNumber, buffer, bufferOffset);
    // Serialize message field [givenColor]
    bufferOffset = _serializer.int32(obj.givenColor, buffer, bufferOffset);
    // Serialize message field [givenShape]
    bufferOffset = _serializer.int32(obj.givenShape, buffer, bufferOffset);
    // Serialize message field [givenLength]
    bufferOffset = _serializer.float32(obj.givenLength, buffer, bufferOffset);
    // Serialize message field [givenDistance]
    bufferOffset = _serializer.float32(obj.givenDistance, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CvInfo
    let len;
    let data = new CvInfo(null);
    // Deserialize message field [cameraNumber]
    data.cameraNumber = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [taskNumber]
    data.taskNumber = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [givenColor]
    data.givenColor = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [givenShape]
    data.givenShape = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [givenLength]
    data.givenLength = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [givenDistance]
    data.givenDistance = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'computer_vision_driver/CvInfo';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8723a30b7f69c63ec944a866a7c37339';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 cameraNumber
    int32 taskNumber
    int32 givenColor
    int32 givenShape
    float32 givenLength
    float32 givenDistance
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CvInfo(null);
    if (msg.cameraNumber !== undefined) {
      resolved.cameraNumber = msg.cameraNumber;
    }
    else {
      resolved.cameraNumber = 0
    }

    if (msg.taskNumber !== undefined) {
      resolved.taskNumber = msg.taskNumber;
    }
    else {
      resolved.taskNumber = 0
    }

    if (msg.givenColor !== undefined) {
      resolved.givenColor = msg.givenColor;
    }
    else {
      resolved.givenColor = 0
    }

    if (msg.givenShape !== undefined) {
      resolved.givenShape = msg.givenShape;
    }
    else {
      resolved.givenShape = 0
    }

    if (msg.givenLength !== undefined) {
      resolved.givenLength = msg.givenLength;
    }
    else {
      resolved.givenLength = 0.0
    }

    if (msg.givenDistance !== undefined) {
      resolved.givenDistance = msg.givenDistance;
    }
    else {
      resolved.givenDistance = 0.0
    }

    return resolved;
    }
};

module.exports = CvInfo;
