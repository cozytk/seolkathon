# build
docker build --cache-from taekkim/seolkathon -t taekkim/seolkathon --build-arg YOUR_ENV=production .

# run
docker run -p 8080:8080 -it taekkim/seolkathon /bin/bash
