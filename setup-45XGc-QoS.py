#!/usr/bin/python
# Generate commands to configure the 45XGc switch used in the CloudLab m510
# cluster for Homa evaluation. To be more specific, we instruct the switch
# to use 802.1p PCP value as packet priority and enable strict-priority queue
# on all 45 ports.

# Enter system view
cmds = ["system-view ;"]

# Configure global priority maps
cmds.append("qos map-table dot1p-lp ;import 0 export 1 ;import 1 export 0 ;import 2 export 2 ;")

# Configure each 10Gb interface
enter_interface_view = "interface Ten-GigabitEthernet1/0/%d ;"
for i in range(45):
    cmds.append(enter_interface_view % (i + 1))
    # Use 802.1p PCP value to decide the local precedence and enable
    # strict-priority queuing
    cmds.append("qos trust dot1p ;qos sp ;")
    cmds.append("quit ;")

# Quit system view
cmds.append("quit ;")
print ''.join(cmds)
