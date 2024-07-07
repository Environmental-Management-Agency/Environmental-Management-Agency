// frontend/components/container/actions/index.js
import axios from 'axios';

export function fetchData() {
    return axios.get('/api/monitoring/')
        .then(response => response.data)
        .catch(error => console.error(error));
}

// frontend/components/container/reducers/index.js
const initialState = {
    data: [],
};

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case 'FETCH_DATA_SUCCESS':
            return { ...state, data: action.data };
        default:
            return state;
    }
}

// frontend/utils/api.js
import axios from 'axios';

const api = axios.create({
    baseURL: '/api/',
});

export default api;
