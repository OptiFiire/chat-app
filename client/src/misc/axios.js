import axios from 'axios';

const token = localStorage.getItem('auth_token') || 'null';

const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000'
});

if (token !== 'null') axiosInstance.defaults.headers.common['Authorization'] = `Token ${token}`

export default axiosInstance;
