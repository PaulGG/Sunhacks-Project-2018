import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {  
    // single source of data
    restaurants: []
}

import {getRestaurant, getRestaurants} from '@/api'
  
const actions = {  
    // asynchronous operations
    loadRestaurants(context, zipcode) {
        return getRestaurants(zipcode).then((response) => context.commit('setRestaurants', { restaurants: response }))
    }, 
    loadRestaurant(context, id) {
        return getRestaurant(id).then((response) => context.commit('setRestaurant', {restaurant: response}))
    }

}
  
const mutations = {  
    // isolated data mutations
    setRestaurants(state, payload) {
        state.restaurants = payload.restaurants
    }
}
  
const getters = {  
    // reusable data accessors
}
  
const store = new Vuex.Store({  
    state,
    actions,
    mutations,
    getters
})
  
export default store  