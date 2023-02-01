from math import sin, cos, radians


def rotate_coordinates_helper(coordinates, rotation_angle):
    rotated_shape_points = []
    for point in coordinates:
        rotated_point = rotate_point(point, rotation_angle)
        rotated_shape_points.append(rotated_point)
    return rotated_shape_points


def rotate_point(point, angle, center_point=(0, 0)):
    """Rotates a point around center_point(origin by default)
    Angle is in degrees.
    Rotation is counter-clockwise
    """
    angle_rad = radians(angle % 360)
    # Shift the point so that center_point becomes the origin
    new_point = (point[0] - center_point[0], point[1] - center_point[1])
    new_point = (new_point[0] * cos(angle_rad) - new_point[1] * sin(angle_rad),
                 new_point[0] * sin(angle_rad) + new_point[1] * cos(angle_rad))
    # Reverse the shifting we have done
    new_point = (new_point[0] + center_point[0], new_point[1] + center_point[1])
    return new_point


def scale_coordinates_helper(coordinates, scale_factor):
    scaled_shape_points = []
    for point in coordinates:
        scaled_point = scale_point(point, scale_factor, (0, 0))
        scaled_shape_points.append(scaled_point)
    return scaled_shape_points


def scale_point(point, scale: float, focal_point):
    # Scaling a shape around the focal point.
    return (point[0] - focal_point[0]) * scale + focal_point[0], \
           (point[1] - focal_point[1]) * scale + focal_point[1]


def hex_color_to_BGR(color: str):
    return int("0x" + color[5:7], 16), int("0x" + color[3:5], 16), int("0x" + color[1:3], 16)
