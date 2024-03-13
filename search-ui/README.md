# Task 5
This README is designed for task 5. 

## Assumptions
1. No security concerns were considered 
2. User has `sudo` and `docker` rights 
3. Users are only doing simple searches by looking for the terms within the documents across predefined fields `generated_text`, `duration`, `age`, `gender`, and `accent`.

## Steps
1. Edit `prod.env` to change the `<YOUR PUBLIC IP>` to elasticsearch IP  
1.1 If the browser you are accessing can access the machine hosting the elasticsearch containers, you can replace `<YOUR PUBLIC IP>` with `es-node1`  
1.2 Else, replace it with the `PUBLIC IP` of your machine
2. Run `docker compose up -d` to run the relevant components
