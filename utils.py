def dataconvert(data):
    """
    converts 12-bytes of data read from the serial port
    into x,y,z,roll,pitch,yaw (inch,inch,inch,deg,deg,deg)
    for a single bird
    """
    xLS, xMS = data[0], data[1]
    yLS, yMS = data[2], data[3]
    zLS, zMS = data[4], data[5]
    yawLS, yawMS = data[6], data[7]
    pitchLS, pitchMS = data[8], data[9]
    rollLS, rollMS = data[10], data[11]
    #
    xLS = ord(xLS) - 128  # change leading bit to zero
    xLS = xLS << 1  # shift bits left
    x = ((xLS + (ord(xMS) * 256)) << 1)
    y = (((ord(yLS) << 1) + (ord(yMS) * 256)) << 1)
    z = (((ord(zLS) << 1) + (ord(zMS) * 256)) << 1)
    yaw = (((ord(yawLS) << 1) + (ord(yawMS) * 256)) << 1)
    pitch = (((ord(pitchLS) << 1) + (ord(pitchMS) * 256)) << 1)
    roll = (((ord(rollLS) << 1) + (ord(rollMS) * 256)) << 1)
    if x > 32767: x -= 65536
    if y > 32767: y -= 65536
    if z > 32767: z -= 65536
    if yaw > 32767: yaw -= 65536
    if pitch > 32767: pitch -= 65536
    if roll > 32767: roll -= 65536
    # convert to inch and deg
    x = x * 144.0 / 32768.0
    y = y * 144.0 / 32768.0
    z = z * 144.0 / 32768.0
    yaw = yaw * 180.0 / 32768.0
    pitch = pitch * 180.0 / 32768.0
    roll = roll * 180.0 / 32768.0
    return x, y, z, roll, pitch, yaw
