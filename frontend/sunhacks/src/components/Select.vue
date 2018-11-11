<template>  
<div>  
  <section class="hero red is-bold">
    <div class="hero-body">
      <div class="container has-text-centered">
        <h2 class="redtitle">Pick A Restaurant</h2>
      </div>
    </div>
  </section>
  <section class="section has-background-grey-dark is-large">
      <div class="columns" v-if="restaurants && restaurants.length">
        <div class="column" v-for="restaurant in restaurants" v-bind:key="restaurant.id">
          <div class="card" @click="clickMethod()">
            <center>
              <p class="title">{{ restaurant.name }}</p>
              <p class='subtitle'>Rating: {{ restaurant.rating }}</p>
              <p class='subtitle'>Review Count: {{restaurant.review_count}}</p>
              <p><img v-bind:src="restaurant.image_url" v-bind:alt="restaurant.name" width="200px" height="200px" style="border-radius: 20px;"/></p>
            </center>
          </div>
        </div>
      </div>
  </section>
</div>  
</template> 
<script>
import router from '../router'

import axios from 'axios'
export default {
  data() {
    return {
      restaurants: [],
      errors: [],
      address: null,
      price: null,
      radius: null
    }
    sharedData : ""
  },
  created() {
    this.address = this.$route.params.address
    this.price = this.$route.params.price
    this.radius = this.$route.params.radius
    console.log(this.$data.address)
    console.log(this.$data.price)
    console.log(this.$data.radius)
    axios.get(`http://localhost:8080/api/restaurant/lookup/${this.$data.address}/${this.$data.radius}/${this.$data.price}`)
    .then(response => {
      this.restaurants = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })
  },
  methods: {
    clickMethod() {
      //TODO change functionality to be not wrong
      //this.$router.push('/')
      //beforeMount()
    }
  }
}
</script>

-<style>
  @import 'Select.css';
</style>
