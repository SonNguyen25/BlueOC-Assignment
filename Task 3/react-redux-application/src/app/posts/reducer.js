import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

const API = "https://jsonplaceholder.typicode.com/posts";

// Fetch all posts from API
export const fetchPosts = createAsyncThunk("posts/fetchPosts", async () => {
  const response = await axios.get(API);
  return response.data;
});

// Initial state for post slice
const initialState = {
  posts: [],
  post: {
    title: "New Post",
    body: "New Body",
  },
  status: "idle",
  error: null,
};

const postSlice = createSlice({
  name: "posts",
  initialState,
  // Reducers to handle state changes
  reducers: {
    addPost: (state, action) => {
      state.posts = [
        {
          ...action.payload,
          _id: new Date().getTime().toString(),
          userId: action.payload?.userId ?? 1,
        },
        ...state.posts,
      ];
    },
    setPost: (state, action) => {
      state.post = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchPosts.pending, (state) => {
        state.status = "pending";
      })
      .addCase(fetchPosts.fulfilled, (state, action) => {
        state.status = "succeeded";
        state.posts = action.payload;
      })
      .addCase(fetchPosts.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.error.message || "Failed to fetch posts from API";
      });
  },
});

export const { addPost, setPost } = postSlice.actions;
export default postSlice.reducer;
