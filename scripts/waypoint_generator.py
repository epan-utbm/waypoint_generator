#!/usr/bin/env python

import yaml
import rospy
import geometry_msgs.msg as geometry_msgs

class WaypointGenerator(object):

    def __init__(self, filename):
        self._sub_pose = rospy.Subscriber('/goal', geometry_msgs.PoseStamped, self._process_pose, queue_size=1)
        self._waypoints = []
        self._filename = filename

    def _process_pose(self, msg):
        p = msg.pose

        data = {}
        data['frame_id'] = msg.header.frame_id
        data['pose'] = {}
        data['pose']['position'] = {'x': p.position.x, 'y': p.position.y, 'z': p.position.z}
        data['pose']['orientation'] = {'x': p.orientation.x, 'y': p.orientation.y, 'z': p.orientation.z, 'w':p.orientation.w}
        data['name'] = '%s_%s' % (p.position.x, p.position.y)
        
        self._waypoints.append(data)
        rospy.loginfo("Clicked : (%s, %s, %s)" % (p.position.x, p.position.y, p.position.z))

    def _write_file(self):
        ways = {}
        ways['waypoints'] = self._waypoints
        with open(self._filename, 'w') as f:
            f.write(yaml.dump(ways, default_flow_style=False))

    def spin(self):
        rospy.spin()
        self._write_file()


if __name__ == '__main__':

    rospy.init_node('waypoint_generator')
    filename = rospy.get_param('~filename', 'waypoints.yaml')
    
    g = WaypointGenerator(filename)
    rospy.loginfo('Initialized')
    g.spin()
    rospy.loginfo('ByeBye')
