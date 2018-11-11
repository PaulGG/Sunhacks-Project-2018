<template>  
<div>  
  <section class="hero is-danger is-bold">
    <div class="hero-body">
      <div class="container has-text-centered">
        <h2 class="title">Pick A Restaurant</h2>
      </div>
    </div>
  </section>
  <a class="button is-rounded" @click="log()">Go!</a>
  <section class="section has-background-grey-dark is-large">
      <div class="columns">
        <div class="column" v-for="restaurant in restaurants" v-bind:key="restaurant.id">
          <div class="card" @click="clickMethod()">
            <center>
              <p class="title">{{ restaurant.name}}</p>
              <!--<p class='subtitle'>{{ restaurant.created_at }}</p>-->
              <!--<p><img v-bind:src="restaurant.imgSrc" v-bind:alt="restaurant.name" width="100px" height="100px" style="border-radius: 20px;"/></p>-->
            </center>
          </div>
        </div>
      </div>
  </section>
</div>  
</template>  
<script>
import { mapState } from 'vuex'
export default { 
    /*
  data() {
    return {
      restaurants: [{
      id: 1,
      name: 'McDonalds',
      created_at: new Date(),
      imgSrc: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/McDonald%27s_Golden_Arches.svg/240px-McDonald%27s_Golden_Arches.svg.png'
      }, {
      id: 2,
      name: 'Taco Bell',
      created_at: new Date(),
      imgSrc: 'https://www.tacobell.com/medias/Taco-Bell-Logo-Bell-Only2.svg?context=bWFzdGVyfGltYWdlc3wyNTk0fGltYWdlL3N2Zyt4bWx8aW1hZ2VzL2gxNi9oM2YvODgyNTMyNjE3NDIzOC5zdmd8MTg2NWZhODE0YTA1ZWNiZWMyMzc5YmQ3MDQzN2U1OTJjYmUwMzFhNTAzMGRhNWNjODFkMGIyOTE1OTJmZTE0MQ'
      }, {
      id: 3,
      name: 'Burger King',
      created_at: new Date(),
      imgSrc: 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Burger_King_Logo.svg/1024px-Burger_King_Logo.svg.png'
      }]
    }
  },*/
  methods: {
    clickMethod() {
      //TODO change functionality to be not wrong
      //this.$router.push('/')
      //beforeMount()
    }, 
    log() {
      console.log(restaurants)
    }
  } 

}
</script>

<style>
  @import 'Select.css';
</style>
