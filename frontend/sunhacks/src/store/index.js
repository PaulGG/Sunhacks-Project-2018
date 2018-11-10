import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {  
    // single source of data
    restaurants: []
}
  
const actions = {  
    // asynchronous operations
    loadRestaurants(context) {
        // return something
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