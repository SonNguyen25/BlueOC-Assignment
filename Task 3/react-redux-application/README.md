# Task 3: React-Redux Application

## Overview of the Application:
An app that fetches posts from the given API `https://jsonplaceholder.typicode.com/posts`, displays them and allows the user to add post(s) locally. 

## Built With:
It is built with Vite, React, and Redux for state management.

## Getting Started:
Run these commands into your terminal depending on what you want to do:
### Prerequesites:
- npm
```
npm install npm@latest -g
```
- Node: 20.19.0+

You can check by running:
```
node -v
npm -v
```

### Installation
```
# Clone the repo
git clone https://github.com/SonNguyen25/BlueOC-Assignment.git

# Go into the directory
cd 'Task 3/react-redux-application'

#Install dependencies
npm install
```

### Run The Application
```
npm run dev
```
After running the command, open the printed URL in the terminal.

### Production
```
npm run build

npm run preview
```
Running the commands above in order to build the project and preview its production build. After running the command, open the printed URL in the terminal.

## Project Structure
```
src/                   
  main.jsx                 
  App.jsx                  

  app/
    store/index.js         

  app/posts/
    reducer.js            
    PostForm.jsx           # dispatches addPost (local)
    PostsList.jsx          # fetches on idle and display posts
```

## How It Works
On initial load, PostsList dispatches fetchPosts() when status === 'idle'. If the status is 'pending' or there is an error, a message will be displayed on screen, else on success, posts are stored in Redux and rendered on page. PostForm illustrates a form for the user to add a post by filling in the post's title and body. When submmited, it will dispatch addPost which add to the list of posts locally in Redux.
There are also extraReducers used to handles asynchronous API calls' status (given to us by Redux's createAsyncThunk) for fetchPosts, which includes: 'pending', 'succeeded', and 'failed'. Other than that, setPost(post) updates the current state of the post to be added, and addPost(post) add a local post by giving it a specified id.
