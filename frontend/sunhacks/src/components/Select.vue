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
          <div class="card mouseover" @click="clickMethod(restaurant.id)">
            <center>
              <p class="title">{{ restaurant.name }}</p>
              <p class='subtitle'>Rating: {{ restaurant.rating }}</p>
              <p class='subtitle'>Review Count: {{restaurant.review_count}}</p>
              <figure class="image is-128x128">
                <img v-bind:src="restaurant.image_url" v-bind:alt="restaurant.name"/>
              </figure>
            </center>
            <footer class="card-footer">
              <p class='card-footer-item'>Address: {{ restaurant.display_address_line_1 }} {{ restaurant.display_address_line_2 }}</p>
              <p class='card-footer-item'>Phone: {{restaurant.display_phone}}</p>
              <p class="card-footer-item">
                <span>
                  View on <a v-bind:href="restaurant.url">Yelp</a>
                </span>
              </p>
            </footer>
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
      radius: null,
      whichModal: null,
      showModal: false
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
    if (this.address == null) {
      this.$router.replace("/")
    }
    axios.get(`http://localhost:8080/api/restaurant/lookup/${this.$data.address}/${this.$data.radius}/${this.$data.price}`)
    .then(response => {
      this.restaurants = response.data
    })
    .catch(e => {
      this.errors.push(e)
    })
  },
  methods: {
    clickMethod(id) {
      
    }
  }
}
</script>

-<style>
  @import 'Select.css';
</style>
