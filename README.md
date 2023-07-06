### Команды:
- cоздание образа из Dockerfile:
`docker build -t ros-app-build .`

- запуск контейнера из созданного образа:
`docker run -it -v ./ros-app:/app -p 5000:5000 ros-app-build`

- подключение к запущеному контейнеру:
`docker exec -it <CONTAINER_ID> bash`

- добавить переменные окружения ROS (выполняется внутри контейнера):
`. ./devel/setup.bash `

- запуск ROS ноды talker (выполняется внутри контейнера):
`python3 src/talker-node/talker.py`

- запуск ROS ноды listiner (выполняется внутри контейнера):
`python3 src/listiner-node/listiner.py`

- POST запрос к /api/log (json вида: {"data":"random data"} ):
`curl --header "Content-Type: application/json" --header "Accept: application/json"   --request POST   --data '{"data":"random data"}' http://localhost:5000/api/log`


![](https://github.com/99v/ros-app/blob/main/screen.png?raw=true)

