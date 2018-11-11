import axios from 'axios'

const API_URL = "http://localhost:8080/api"

export function getRestaurants(zipcode) {
    return axios.get(`${API_URL}/restaurant/zip/${zipcode}`)
}

export function getRestaurant(id) {
    return axios.get(`${API_URL}/restaurants/id/${zipcode}`)
}

