import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import store from './app/store/index.js'
import { Provider } from 'react-redux'

// Wrap application with Redux Provider
createRoot(document.getElementById('root')).render(
  <Provider store={store}>
    <App />
  </Provider>
)
