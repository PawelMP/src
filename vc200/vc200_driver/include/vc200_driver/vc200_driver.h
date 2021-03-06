#pragma once

#include <hardware_interface/imu_sensor_interface.h>
#include <hardware_interface/joint_command_interface.h>
#include <hardware_interface/joint_state_interface.h>
#include <ros/ros.h>

#include <thread>
#include <vector>

#include "stalker_driver/STInterfaceClientUDP.h"
#include "vc200_driver/configuration.h"
#include "vc200_driver/imu.h"
#include "vc200_driver/motor_controller.h"
#include "vc200_driver/statistics.h"
#include "vc200_driver/timers.h"
#include "vc200_driver/laser_ruler.h"
#include "vc200_driver/ultrasound.h"                                            //Added by Filip
#include "vc200_driver/minilidar.h"

namespace vc200_driver {
class VC200Driver {
 public:
  VC200Driver();
  ~VC200Driver();

  bool init(ros::NodeHandle &nh, ros::NodeHandle &priv_nh);

  std::vector<hardware_interface::JointHandle> getPositionJoints();
  std::vector<hardware_interface::JointHandle> getVelocityJoints();
  std::vector<hardware_interface::JointHandle> getEffortJoints();
  std::vector<hardware_interface::ImuSensorHandle> getImuJoints();
  void readData();
  void writeData();
  void run();
  void stop();
  std::unique_ptr<LaserRuler> laserRulerPtr_;
  std::unique_ptr<Ultrasound> ultrasoundPtr_;  
  std::unique_ptr<Minilidar> minilidarPtr_; 
 private:
  std::unique_ptr<IMU> imuSensorsPtr_;
  std::unique_ptr<MotorController> motorControllerPtr_;
  std::unique_ptr<Statistics> statsPtr_;
  std::unique_ptr<Configurator> confPtr_;
  std::unique_ptr<Timers> timersPtr_;
                                  //Added by Filip

  std::shared_ptr<STInterface::STInterfaceClientUDP> stClientPtr_;
  bool connected_;
  bool running_;
  std::thread updaterThread_;
  void updater();
};
}  // namespace vc200_driver
