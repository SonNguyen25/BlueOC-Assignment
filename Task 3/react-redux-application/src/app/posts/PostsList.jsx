import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchPosts } from "./reducer";

// Show the list of available posts fetched from Redux store, and fetch from API when idle
function PostsList() {
  // Select current list of posts, status, and error from Redux store
  const postsList = useSelector((state) => state.postsReducer.posts);
  const status = useSelector((state) => state.postsReducer.status);
  const error = useSelector((state) => state.postsReducer.error);
  const dispatch = useDispatch();

  // Fetch list of posts from API call when status is idle (initial state)
  useEffect(() => {
    if (status === "idle") {
      dispatch(fetchPosts());
    }
  }, [status, dispatch]);

  // If status is pending, then display an informative line
  if (status === "pending") return <p>"Fetching Posts, Please Wait"</p>;

  // If status is failed, show the error message
  if (status === "failed") return <p>{error}</p>;

  // If status is succeeded, then display all the posts
  return (
    <ul className="list-group">
      {postsList.map((p) => (
        <li key={p.id}>
          <h2>{p.title}</h2>
          <p>{p.body}</p>
        </li>
      ))}
    </ul>
  );
}
export default PostsList;
