import axios from "axios";

const apiLink = "http://127.0.0.1:8000/";
const loginPage = "/account/login/";

let setLoadingCallback = null;

const api = axios.create({
  baseURL: apiLink,
  timeout: 20000,
});

let isRefreshing = false;
let failedQueue = [];

const processQueue = (error, token = null) => {
  failedQueue.forEach((prom) => {
    if (token) {
      prom.resolve(token);
    } else {
      prom.reject(error);
    }
  });

  failedQueue = [];
};

// Function to check the validity of the refresh token
const isRefreshTokenValid = (refreshToken) => {
  if (!refreshToken) return false;

  try {
    const payload = JSON.parse(atob(refreshToken.split('.')[1]));
    const expirationTime = payload.exp * 1000; // Convert expiration time to milliseconds
    return Date.now() < expirationTime;
  } catch (error) {
    return false;
  }
};

// Interceptor to add the Access Token to each request
api.interceptors.request.use((config) => {
  if (setLoadingCallback && !config.noL) {
    setLoadingCallback(true);
  }

  const accessToken = localStorage.getItem("access_token");
  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }
  return config;
});

// Interceptor to handle errors
api.interceptors.response.use(
  (response) => {
    if (setLoadingCallback && !response.config.noL) {
      setLoadingCallback(false);
    }
    return response;
  },
  async (error) => {
    const originalRequest = error.config;

    if (setLoadingCallback && !originalRequest.noL) {
      setLoadingCallback(false);
    }

    if (
      error.response &&
      (error.response.status === 401 || error.response.status === 403) &&
      !originalRequest._retry
    ) {
      originalRequest._retry = true;

      const refreshToken = localStorage.getItem("refresh_token");

      if (refreshToken && isRefreshTokenValid(refreshToken)) {
        if (!isRefreshing) {
          isRefreshing = true;

          try {
            // Send a request to refresh the Access Token
            const response = await axios.post(
              `${apiLink}/auth/token/refresh/`,
              { refresh: refreshToken }
            );

            const newAccessToken = response.data.access;
            localStorage.setItem("accessToken", newAccessToken);

            // Process failed requests
            processQueue(null, newAccessToken);

            isRefreshing = false;

            // Resend the original request
            originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
            return api(originalRequest);
          } catch (refreshError) {
            // If the refresh request fails, clear tokens and redirect
            processQueue(refreshError, null);
            isRefreshing = false;

            localStorage.clear();
            window.location.href = loginPage;
            return Promise.reject(refreshError);
          }
        }

        // Manage failed requests during refresh
        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject });
        })
          .then((token) => {
            originalRequest.headers.Authorization = `Bearer ${token}`;
            return api(originalRequest);
          })
          .catch((err) => {
            return Promise.reject(err);
          });
      } else {
        // If there's no refresh token or it's expired, clear tokens and redirect
        localStorage.clear();
        window.location.href = loginPage;
      }
    }

    // Handle other errors
    if (
      error.response &&
      error.response.data &&
      (error.response.data.detail === "Authentication credentials were not provided." ||
        error.response.data.code === "token_not_valid" ||
        error.response.data.code === "user_not_found"
      )
    ) {
      const refreshToken = localStorage.getItem("refreshToken");

      if (!refreshToken || !isRefreshTokenValid(refreshToken)) {
        localStorage.clear();
        window.location.href = loginPage;
      }
    }

    return Promise.reject(error);
  }
);

// Function to set the loading callback for managing loading screens
export const setLoadingHandler = (callback) => {
  setLoadingCallback = callback;
};

export default api;