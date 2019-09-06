from controller import *

# create the Robot instance.
robot = Robot()

lf_dir = Motor('lf_dir_motor')
lf_run = Motor('lf_run_motor')

lb_dir = Motor('lb_dir_motor')
lb_run = Motor('lb_run_motor')

rf_dir = Motor('rf_dir_motor')
rf_run = Motor('rf_run_motor')

rb_dir = Motor('rb_dir_motor')
rb_run = Motor('rb_run_motor')
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  led = robot.getLED('ledname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)
# lf_dir.setVelocity(10)
# lb_dir.setVelocity(10)
# rf_dir.setVelocity(10)
# rb_dir.setVelocity(10)

tr_ = 180/3.1415926

def robo_run(dir,dis,speed):   
    dis_angle = -dis/0.05
    lf_run.setVelocity(speed)    
    lf_dir.setPosition(-dir/tr_)   
    lf_run.setPosition(dis_angle)
    
    lb_run.setVelocity(speed)
    lb_dir.setPosition(dir/tr_)   
    lb_run.setPosition(dis_angle)
    
    rf_run.setVelocity(speed)
    rf_dir.setPosition(dir/tr_)
    rf_run.setPosition(-dis_angle)
    
    rb_run.setVelocity(speed)
    rb_dir.setPosition(-dir/tr_)
    rb_run.setPosition(-dis_angle)

    
    
robo_run(45,20,20)
robo_run(45,20,20)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  led.set(1)
    print('#####')
    pass

# Enter here exit cleanup code.
