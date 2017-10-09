// Auto-generated. Do not edit!

// (in-package computer_vision.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class FrontCamera {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.frontCamForwardDistance = null;
      this.frontCamHorizontalDistance = null;
      this.frontCamVerticalDistance = null;
    }
    else {
      if (initObj.hasOwnProperty('frontCamForwardDistance')) {
        this.frontCamForwardDistance = initObj.frontCamForwardDistance
      }
      else {
        this.frontCamForwardDistance = 0.0;
      }
      if (initObj.hasOwnProperty('frontCamHorizontalDistance')) {
        this.frontCamHorizontalDistance = initObj.frontCamHorizontalDistance
      }
      else {
        this.frontCamHorizontalDistance = 0.0;
      }
      if (initObj.hasOwnProperty('frontCamVerticalDistance')) {
        this.frontCamVerticalDistance = initObj.frontCamVerticalDistance
      }
      else {
        this.frontCamVerticalDistance = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FrontCamera
    // Serialize message field [frontCamForwardDistance]
    bufferOffset = _serializer.float32(obj.frontCamForwardDistance, buffer, bufferOffset);
    // Serialize message field [frontCamHorizontalDistance]
    bufferOffset = _serializer.float32(obj.frontCamHorizontalDistance, buffer, bufferOffset);
    // Serialize message field [frontCamVerticalDistance]
    bufferOffset = _serializer.float32(obj.frontCamVerticalDistance, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FrontCamera
    let len;
    let data = new FrontCamera(null);
    // Deserialize message field [frontCamForwardDistance]
    data.frontCamForwardDistance = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [frontCamHorizontalDistance]
    data.frontCamHorizontalDistance = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [frontCamVerticalDistance]
    data.frontCamVerticalDistance = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'computer_vision/FrontCamera';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '65f5794fdf87a86db880b10f7ba78110';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 frontCamForwardDistance
    float32 frontCamHorizontalDistance
    float32 frontCamVerticalDistance
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FrontCamera(null);
    if (msg.frontCamForwardDistance !== undefined) {
      resolved.frontCamForwardDistance = msg.frontCamForwardDistance;
    }
    else {
      resolved.frontCamForwardDistance = 0.0
    }

    if (msg.frontCamHorizontalDistance !== undefined) {
      resolved.frontCamHorizontalDistance = msg.frontCamHorizontalDistance;
    }
    else {
      resolved.frontCamHorizontalDistance = 0.0
    }

    if (msg.frontCamVerticalDistance !== undefined) {
      resolved.frontCamVerticalDistance = msg.frontCamVerticalDistance;
    }
    else {
      resolved.frontCamVerticalDistance = 0.0
    }

    return resolved;
    }
};

module.exports = FrontCamera;
