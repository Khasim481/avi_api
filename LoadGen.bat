echo "Load generator.."

start cmd /k kubectl run -i --tty load-generator-open --rm --image=busybox --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://avi-api.com/get_all_flight_states; done"
start cmd /k kubectl run -i --tty load-generator-country  --rm --image=busybox --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://avi-api.com/country_air_space?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226; done"
start cmd /k kubectl run -i --tty load-generator-flight --rm  --image=busybox --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://avi-api.com/track_flight/4b1814; done"
