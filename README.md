# title-creating-by-interests

## Just an API that generates titles based on input interests.

don't forget edit the dockerfile adding your OPENAI_API_KEY

then use those command

just docker build -t fastapi-openai-app .  
docker run -p 80:80 fastapi-openai-app

you can use this APT to get a title according the interests.

http://0.0.0.0/creat_title/{interests1}-{interests2}-{interests3}......
