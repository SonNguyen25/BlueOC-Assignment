import PostsList from "./app/posts/PostsList";
import PostForm from "./app/posts/PostForm"

// Main App, display app name and relevant posts functionalities/components
function App() {

  return (
    <div className="App">
      <h1>React-Redux Application</h1>
      <PostForm/>
      <PostsList/>
    </div>
  );
}

export default App;
