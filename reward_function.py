import math
import numpy as np
def reward_function(params):

    FUTURE_STEP = 7
    MID_STEP = 4
    TURN_THRESHOLD = 10     # degrees
    DIST_THRESHOLD = 1.2    # metres
    SPEED_THRESHOLD = 1.8   # m/s (or 2.0)


    def judgment_angle(waypoints, closest_waypoints, future_step):

        point_prev = waypoints[closest_waypoints[0]]
        point_next = waypoints[closest_waypoints[1]]
        point_future = waypoints[min(len(waypoints) - 1,  closest_waypoints[1] + future_step)]
        print("future_step: " + str(future_step) + ", point_future: " + str(point_future))

        heading_current = math.degrees(math.atan2(point_prev[1] - point_next[1], point_prev[0] - point_next[0]))
        heading_future = math.degrees(math.atan2(point_prev[1] - point_future[1], point_prev[0]-point_future[0]))

        diff_heading = abs(heading_current - heading_future)

        if diff_heading > 180:
            diff_heading = 360 - diff_heading

        dist_future = np.linalg.norm([point_next[0] - point_future[0], point_next[1] - point_future[1]])  

        return diff_heading, dist_future


    def select_speed(waypoints, closest_waypoints, future_step, mid_step):

        diff_heading, dist_future = judgment_angle(waypoints, closest_waypoints, future_step)
        print("diff_heading: " + str(diff_heading) + ", dist_future: " + str(dist_future))

        if diff_heading < TURN_THRESHOLD:
            go_fast = True
        else:
            if dist_future < DIST_THRESHOLD:
                go_fast = False
            else:
                diff_heading_mid, dist_mid = judgment_angle(waypoints, closest_waypoints, mid_step)

                if diff_heading_mid < TURN_THRESHOLD:
                    go_fast = True
                else:
                    go_fast = False

        return go_fast


    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    closest_waypoints = params['closest_waypoints']
    distance_from_center = params['distance_from_center']
    is_offtrack = params['is_offtrack']
    progress = params['progress']
    speed = params['speed']
    steps = params['steps']
    track_width = params['track_width']
    waypoints = params['waypoints']
    is_left_of_center = params['is_left_of_center']
    steering_angle = params['steering_angle']

    if is_offtrack:
        reward = 1e-4
        
        return float(reward)
        
    if not all_wheels_on_track and is_left_of_center and steering_angle >= 0:
        reward = 1e-4
        
        return float(reward)
        
    if not all_wheels_on_track and not is_left_of_center and steering_angle <= 0:
        reward = 1e-4
        
        return float(reward)
        
    

    reward = 1 - (distance_from_center/(track_width/2))**(1/4)
    reward += (progress/steps) * 1.5

    go_fast = select_speed(waypoints, closest_waypoints, FUTURE_STEP, MID_STEP)
    
    if is_left_of_center :
        reward += 0.3

    if go_fast and speed > SPEED_THRESHOLD and -7 < steering_angle < 7:
        reward += 2.0

    elif not go_fast and speed < SPEED_THRESHOLD:
        reward += 1.0  
    
    reward *= 0.1 #Reduce the total reward

      
    return float(reward)
