# Week 4: Docker
## Weekly tasks
1. Introduction to Docker 
    * Concepts to Learn:
        * [Docker Docs](https://docs.docker.com/)
        * [Docker compose Docs](https://docs.docker.com/compose/)
        * [Docker Crash Course for Absolute Beginners](https://youtu.be/pg19Z8LL06w?si=TAve162Q5pLZZnN0)
        * [Ultimate Docker Compose Tutorial](https://youtu.be/SXwC9fSwct8?si=a4TsO34R3ObTT8uZ)
        * [Networking](https://youtu.be/fBRgw5dyBd4?si=lXdkxBzxYOPMIlMM)
        
## HomeWORK
### Docker
1. Install docker and docker-compose-plugin on server `week4`. Add your user to `docker` group. 
2. Create docker network
    1. Set `week4` as a name.
    2. Set `bridge` as driver.
    3. Set `172.20.0.0/16` as subnet.
    4. Set `172.20.0.1` as gateway.
3. Write `Dockerfile` on server to build image nginx. It is important to build nginx image not to use already existed. 
    1. Use Ubuntu as base image
    2. As nginx default page image has to return "DevOps Internship" message as nginx's default web page.
    3. Run newly created image on server as `week4-nginx` named container with 8080:80 binded port.
    4. Deploy newly created image to remote image registry as `REGISTRY/name-surname:week4-nginx`.    
4. Pull gitlab repository to server `week4` and write dockerfile for tictactoe project.
    1. Build and push image to `REGISTRY/name-surname:week4-tictactoe`.
    2. Run newly created image as `week4-tictactoe` named container 
    3. `week4-tictactoe` container to `week4` network.
    EXTRA: Image should be optimized as possible (as less image size as possible).
5. Work with docker compose folder. You have to write dockerfile for `application` folder it is python application runs on port `5000`. Dockerfile for `database` is already provided no need to edit anything there. Declare `week4` network as external in `docker-compose.yml`.
    database service name: `postgres`
    application service name: `application`
    1. Write docker compose file and run it as `week4`.
       1. Application started
       2. Database started
    2. Service: application
       1. Should be networks: `default`, `week4`
    3. Service: database
       1. Should be in networks: `week4`
    4. Bind `application` to port `5000`.

#### Important!
    Be carefull with environmental variables. 
    Default values you can find in application/main.py 
    
