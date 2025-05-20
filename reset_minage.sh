send_command() {
  local command=$1
  local time=$2

  screen -R Epicraft -X stuff "$command $(printf '\r')"
  sleep "$time"
}

send_command "say Stopping server in 30 seconds to reset the Mining World" 27
send_command "say Explosion in 3" 1
send_command "say Explosion in 2" 1
send_command "say Explosion in 1" 1
send_command "stop" 30
screen -R Epicraft -X stuff "$(printf '\x03')"
sleep 5
send_command "" 1
python3 /home/ubuntu/Epicraft/reset_minage/main.py >> /home/ubuntu/Epicraft/reset_minage/logs.log
sleep 20
send_command "./run.sh" 120
send_command "chunky world dim_x:dimx" 3
send_command "chunky corners 2000 2000 -2000 -2000" 3
send_command "chunky start" 3 
