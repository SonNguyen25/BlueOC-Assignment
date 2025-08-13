import { configureStore } from "@reduxjs/toolkit";
import postsReducer from "../posts/reducer"

// Redux store configuration
const store = configureStore({
  reducer: {
    postsReducer,
  }
});

export default store;