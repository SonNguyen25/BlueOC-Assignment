import { useDispatch, useSelector } from "react-redux";
import { addPost, setPost } from "./reducer";

// Represents a form for user to create a new post and therefore add it to the Redux store
function PostForm() {
    // Select current post and status from Redux store
  const post = useSelector((state) => state.postsReducer.post);
  const status = useSelector((state) => state.postsReducer.status);
  const dispatch = useDispatch();

  // Dispatch upon submitting, prevent default to prevent page refresh from submission
  const onSubmit = (e) => {
    e.preventDefault();
    dispatch(addPost(post));
    dispatch(setPost({ title: "New Post", body: "New Body" }));
  };

  return (
    <form onSubmit={onSubmit} style={{ display: "grid", gap: 10, margin: 16 }}>
      <input
        value={post.title}
        onChange={(e) => dispatch(setPost({ ...post, title: e.target.value }))}
        disabled={status === "pending"}
        placeholder="Title"
      />
      <textarea
        value={post.body}
        onChange={(e) => dispatch(setPost({ ...post, body: e.target.value }))}
        disabled={status === "pending"}
        placeholder="Body"
      />
      <button type="submit" disabled={status === "pending"}>
        Add Post
      </button>
    </form>
  );
}
export default PostForm;
