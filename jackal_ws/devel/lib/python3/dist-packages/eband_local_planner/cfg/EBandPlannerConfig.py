## *********************************************************
##
## File autogenerated for the eband_local_planner package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'xy_goal_tolerance', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'Distance tolerance for reaching the goal pose', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'yaw_goal_tolerance', 'type': 'double', 'default': 0.05, 'level': 0, 'description': 'Orientation tolerance for reaching the desired goal pose', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'rot_stopped_vel', 'type': 'double', 'default': 0.01, 'level': 0, 'description': 'Angular velocity lower bound that determines if the robot should stop to avoid limit-cycles or locks', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'trans_stopped_vel', 'type': 'double', 'default': 0.01, 'level': 0, 'description': 'Linear velocity lower bound that determines if the robot should stop to avoid limit-cycles or locks', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'marker_lifetime', 'type': 'double', 'default': 0.5, 'level': 0, 'description': 'Lifetime of eband visualization markers', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'eband_min_relative_overlap', 'type': 'double', 'default': 0.7, 'level': 0, 'description': 'Min distance that denotes connectivity between consecutive bubbles', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'eband_tiny_bubble_distance', 'type': 'double', 'default': 0.01, 'level': 0, 'description': 'Bubble geometric bound regarding tiny bubble distance', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'eband_tiny_bubble_expansion', 'type': 'double', 'default': 0.01, 'level': 0, 'description': 'Bubble geometric bound regarding tiny bubble expansion', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'eband_internal_force_gain', 'type': 'double', 'default': 1.0, 'level': 0, 'description': 'Force gain of forces between consecutive bubbles that tend to stretch the elastic band', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'eband_external_force_gain', 'type': 'double', 'default': 2.0, 'level': 0, 'description': 'Force gain of forces that tend to move the bubbles away from obstacles', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'num_iterations_eband_optimization', 'type': 'int', 'default': 3, 'level': 0, 'description': 'Number of iterations for eband optimization', 'min': 1, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'eband_equilibrium_approx_max_recursion_depth', 'type': 'int', 'default': 4, 'level': 0, 'description': 'Number of iterations for reaching the equilibrium between internal and external forces', 'min': 1, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'eband_equilibrium_relative_overshoot', 'type': 'double', 'default': 0.75, 'level': 0, 'description': 'Maximum relative equlibrium overshoot', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'eband_significant_force_lower_bound', 'type': 'double', 'default': 0.15, 'level': 0, 'description': 'Minimum magnitude of force that is considered significant and used in the calculations', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'costmap_weight', 'type': 'double', 'default': 10.0, 'level': 0, 'description': 'Costmap weight factor used in the calculation of distance to obstacles', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'max_vel_lin', 'type': 'double', 'default': 0.75, 'level': 0, 'description': 'Maximum linear velocity', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'max_vel_th', 'type': 'double', 'default': 1.0, 'level': 0, 'description': 'Maximum angular velocity', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'min_vel_lin', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'Minimum linear velocity', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'min_vel_th', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Minimum angular velocity', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'min_in_place_vel_th', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Minimum in-place angular velocity', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'in_place_trans_vel', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'Minimum in place linear velocity', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'k_prop', 'type': 'double', 'default': 4.0, 'level': 0, 'description': 'Proportional gain of the PID controller', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'k_damp', 'type': 'double', 'default': 3.5, 'level': 0, 'description': 'Damping gain of the PID controller', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'Ctrl_Rate', 'type': 'double', 'default': 10.0, 'level': 0, 'description': 'Control rate', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'max_acceleration', 'type': 'double', 'default': 0.5, 'level': 0, 'description': 'Maximum allowable acceleration', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'virtual_mass', 'type': 'double', 'default': 0.75, 'level': 0, 'description': 'Virtual mass', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'max_translational_acceleration', 'type': 'double', 'default': 0.5, 'level': 0, 'description': 'Maximum linear acceleration', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'max_rotational_acceleration', 'type': 'double', 'default': 1.5, 'level': 0, 'description': 'Maximum angular acceleration', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'rotation_correction_threshold', 'type': 'double', 'default': 0.5, 'level': 0, 'description': 'Rotation correction threshold', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'differential_drive', 'type': 'bool', 'default': True, 'level': 0, 'description': 'Denotes whether to use the differential drive hack', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'bubble_velocity_multiplier', 'type': 'double', 'default': 2.0, 'level': 0, 'description': 'Multiplier of bubble radius', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'rotation_threshold_multiplier', 'type': 'double', 'default': 1.0, 'level': 0, 'description': 'Multiplier of rotation threshold', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'disallow_hysteresis', 'type': 'bool', 'default': False, 'level': 0, 'description': 'Determines whether to try getting closer to the goal, in case of going past the tolerance', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

