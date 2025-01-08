import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000/api', // Replace with your API base URL
  timeout: 10000, // Request timeout in milliseconds
});

export default {
  install(app) {
    app.config.globalProperties.$api = axiosInstance;
    app.provide('api', axiosInstance);
  },
};