<template>  
<div>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.1/css/bulma.min.css" rel="stylesheet" />  
    <section class="hero is-danger is-bold is-medium">
    <div class="hero-body">
      <div class="container has-text-centered">
        <h2 class="title">Welcome to Give-me-eat.com!</h2>
        <h3 clas="subtitle">Tired of not knowing where to go to eat?  We've got you covered!  Enter your location below and we'll give you some options for where to eat.</h3>
      </div>
    </div>
  </section>
  <section class="section">
        <div class="card">
            <center>
                <p class="title">Enter Information:</p>
                <div class="columns is-centered is-vcentered">
                    <div class="column is-narrow is-centered">
                        <input v-model="zipmessage" placeholder="Enter Address/ZIP">
                        <p>{{zipmessage}}</p>
                    </div>
                    <div class="column is-centered">
                        <div class="select">
                            <select v-model="radius">
                                <option value="1">1 mile</option>
                                <option value="2">2 miles</option>
                                <option value="5">5 miles</option>
                                <option value="10">10 miles</option>
                                <option value="15">15 miles</option>
                                <option value="20">20 miles</option>
                                <option value="25">25 miles</option>
                            </select>
                        </div>
                        <div class="select">
                            <select v-model="price">
                                <option value="1">$</option>
                                <option value="2">$$</option>
                                <option value="3">$$$</option>
                                <option value="4">$$$$</option>
                            </select>
                        </div>
                    </div>
                    <div class="column is-one-fifth">
                        <a class="button is-rounded" @click="changePage()">Go!</a>
                    </div>
                </div>
            </center>
        </div>
  </section>
</div>  
</template>  

<script>
export default{
    data() {
        return {
            zipmessage: "",
            price: 1,
            radius: 5
        }
    },
    methods: {
        changePage() {
            this.$router.push({
                name: "Select",
                params: { address: this.$data.zipmessage, price: this.$data.price, radius: this.$data.radius}
            });
        }
    }
}
</script>

<style>
  @import 'Home.css';
  
</style>
